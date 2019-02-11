import os
import sys
import datetime as dt
import numpy as np
import math
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from netCDF4 import Dataset
import datetime
from dateutil.parser import parse

# try to auto-configure the path. This will work in the case
# that you have checked out the doc and data repositories
# at same level. Make sure this is done **before** importing shyft
shyft_data_path = os.path.abspath("../../../workspace/shyft-data")
if os.path.exists(shyft_data_path) and 'SHYFT_DATA' not in os.environ:
    os.environ['SHYFT_DATA']=shyft_data_path

# shyft should be available either by it's install in python
# or by PYTHONPATH set by user prior to starting notebook.
# If you have cloned the repositories according to guidelines:
shyft_path=os.path.abspath('../../../workspace/shyft')
sys.path.insert(0,shyft_path)
print(sys.path)

import shyft

from shyft import shyftdata_dir
from shyft import api

# Weather station data Golden, Colorado

latitude = 60.5935
longitude = 7.5245
elevation = 1204.0
lat_rad = latitude*math.pi/180
slope_deg = 0.0
aspect_deg = 0.0
slope = slope_deg*math.pi/180
aspect = aspect_deg*math.pi/180
albedo = 0.2
turbidity = 1.0

tempP1 = 20.0 # [degC], real data should be used
rhP1 = 50.0 #[%], real data should be used
gsc = 1367
utc = api.Calendar()

print(" --------------------------------------------------------- ")
print(" --- Single method test: must match the reference fig.1b, 3e,3g,3f --- ")
print(" --- ref.: Allen, R. G.; Trezza, R. & Tasumi, M. -----------")
print(" Analytical integrated functions for daily solar radiation on ")
print(" slopes Agricultural and Forest Meteorology, 2006, 139, 55-73")
print(" --- Here we present plot with SW_radiation (Rso), W/m^2 --- ")
print(" --- Station: Finse, Norway --- ")
print(" --- Latitude: ",latitude," --- ")
print(" --- Longitude: ",longitude," --- ")
print(" --- Elevation (estimated): ",elevation," --- ")
print(" --------------------------------------------------------- ")


# preparing data
import csv

with open('csv_finse_initial.csv', mode='r') as csv_file:
    # csv_reader = csv.DictReader(csv_file)
    csv_reader = csv.DictReader(csv_file)
    # mylist = list(csv_reader)
    line_count = 0
    timestr = []
    timearr = []
    timepyobj=[]
    lw_down = []
    lw_up = []
    atmp = []
    rh_2 = []
    sw_down = []
    sw_up =[]
    sw_net = []
    air_temp_2 = []
    air_temp_10 = []

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        # print(f'\t{row} .')
        else:
            # if row["time"]:
            timestr.append(row["time"])
            timeobj = parse(row["time"])
            timepyobj.append(timeobj)
            time = utc.time(timeobj.year, timeobj.month, timeobj.day, timeobj.hour,
                            timeobj.minute, timeobj.second)
            # print(time)
            timearr.append(time)
            if not row["Rl_downwell"]:
                lwd=0.0
            else:
                lwd = float(row["Rl_downwell"])
            lw_down.append(lwd)
            if not row["Rl_upwell"]:
                lwu=0.0
            else:
                lwu = float(row["Rl_upwell"])
            lw_up.append(row["Rl_upwell"])
            if not row["AT_mbar"]:
                atp=0.0
            else:
                atp = float(row["AT_mbar"])
            atmp.append(atp)
            if not row["U_1477"]:
                rh=0.0
            else:
                rh = float(row["U_1477"])
            rh_2.append(rh)
            if not row["Rs_downwell"]:
                swd = 0.0
            else:
                swd = float(row["Rs_downwell"])
            sw_down.append(swd)
            if not row["Rs_upwell"]:
                swu = 0.0
            else:
                swu = float(row["Rs_upwell"])
            sw_up.append(swu)
            sw_net.append(swd-swu)
            if not row["T_a_1477"]:
                at = 0.0
            else:
                at = float(row["T_a_1477"])
            air_temp_2.append(at)
            line_count += 1
    print(f'Processed {line_count} lines.')
    # print(timestr)
    print(len(timestr))
    # print(sw_down)


# # fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2, figsize=(7,5))
# fig, ax1 = plt.subplots(figsize=(7,5))
# fig.suptitle('Finse, Norway, measured data')
# myFmt=mdates.DateFormatter('%Y-%M-%D %H:%M:%S')
# ax1.plot(timepyobj,sw_down, 'r--', label='sw-downwell')
# ax1.set_ylabel('Rsm, [W/m^2]')
# ax1.set_xlabel('Date-time')
# plt.gcf().autofmt_xdate()
# # plt.gca().xaxis.set_major_formatter(myFmt)
#
# # ax1.legend(loc="upper left")
# # plt.legend(loc="lower center")
# # ax1.axis([0,365,-20,600])
# ax1.grid(True)
# # ax2.plot( sw_up, 'r--', label='sw-upwell')
# # ax2.set_ylabel('Rsm, [W/m^2]')
# # ax2.set_xlabel('number')
# # ax1.legend(loc="upper left")
# # plt.legend(loc="lower center")
# # ax2.axis([0,365,-20,600])
# # ax2.grid(True)
# # plt.show()

# processing data: I want to get only values for measurements between 2016-10-01 to 2016-10-22
idxstart=timestr.index('2016-10-01 00:00:00')
idxend=timestr.index('2016-10-23 00:00:00')
idxstep=2
times=timearr[idxstart:idxend:idxstep]
timespy=timepyobj[idxstart:idxend:idxstep]
print(times)
sw_down_oct16=sw_down[idxstart:idxend:idxstep]
print(sw_down_oct16)
sw_up_oct16=sw_up[idxstart:idxend:idxstep]
sw_net_oct16=sw_net[idxstart:idxend:idxstep]
lw_down_oct16=lw_down[idxstart:idxend:idxstep]
lw_up_oct16=lw_up[idxstart:idxend:idxstep]
air_temp_2_oct16=air_temp_2[idxstart:idxend:idxstep]
rh_2_oct16=rh_2[idxstart:idxend:idxstep]
atmp_oct16=atmp[idxstart:idxend:idxstep]
print(len(times))

fig, ax1 = plt.subplots(figsize=(7,5))
fig.suptitle('Finse, Norway, measured data October 2016')
myFmt=mdates.DateFormatter('%Y-%M-%D %H:%M:%S')
ax1.plot(timespy,sw_net_oct16, 'r--', label='sw-net')
ax1.set_ylabel('Rsm, [W/m^2]')
ax1.set_xlabel('Date-time')
plt.gcf().autofmt_xdate()
ax1.grid(True)
plt.show()

# Will try to work withn data 2016-10-01 to 2016-10-22
n = 22 # nr of days
day = np.arange(n) # day of year

t_start = utc.time(2016, 10, 1) # starting at the beginning of the measurements 2010-10-01
dtdays = api.deltahours(24) # returns daily timestep in seconds
dt = api.deltahours(1) # returns daily timestep in seconds

# Let's now create Shyft time series from the supplied lists of precipitation and temperature.
# First, we need a time axis, which is defined by a starting time, a time step and the number of time steps.
tadays = api.TimeAxis(t_start, dtdays, n) # days
# print(len(tadays))
ta = api.TimeAxis(t_start, dt, n*24) # hours
# print(len(ta))


radparamy = api.RadiationParameter(albedo,turbidity)
radcaly = api.RadiationCalculator(radparamy)
radcaly1 = api.RadiationCalculator(radparamy)
radcaly24 = api.RadiationCalculator(radparamy)
radcaly3 = api.RadiationCalculator(radparamy)
radresy =api.RadiationResponse()
radresy1 =api.RadiationResponse()
radresy24 =api.RadiationResponse()
radresy3 =api.RadiationResponse()



# we now can simply run the routine step by step:
try:
    del net_rad
    del ra_rad
    del rah_rad
except:
    pass

net_rad = api.DoubleVector()
swcalc_step1 = api.DoubleVector()
ra_rad = api.DoubleVector()
ra_rad1 = api.DoubleVector()
rah_rad = api.DoubleVector()
rat_rad = api.DoubleVector()
declin_arr = api.DoubleVector()
radtheorint_arr = api.DoubleVector()
swcalc_step24=api.DoubleVector()
radcalc_step24=api.DoubleVector()

swcalc_step3=api.DoubleVector()
radcalc_step3=api.DoubleVector()

i = 0
j = 1
dayi = 0
doy = api.DoubleVector()
omega1 = 0
omega2 = 0
rsm = 0
rahrad = 0.0

sw_simulated_1h = api.DoubleVector()

while (i<n):
    netrad = 0.0
    swrad1 = 0.0
    swrad3 = 0.0
    rarad = 0.0
    rarad1 = 0.0
    rarad3 = 0.0
    ratheor_int = 0.0
    j = 1
    # rsm = rahrad / 23
    rsm = 0.0
    rahrad = 0.0
    rahrad1 = 0.0
    dd = 1 + 0.033 * math.cos(dayi * 2 * math.pi / 365)
    G = 2 * math.pi / 365 * (dayi - 1)
    declin = 0.006918 - 0.399912 * math.cos(G) + 0.070257 * math.sin(G) - 0.006758 * math.cos(
        2 * G) + 0.000907 * math.sin(2 * G) - 0.002697 * math.cos(3 * G) + 0.00148 * math.sin(3 * G)
    # tmpra = api.DoubleVector()
    while (j<24):
        time1 = ta.time(i*24+j-1)
        time2 = ta.time(i * 24 + j)
        tempP1= air_temp_2_oct16[i * 24 + j]
        print("temperature: ", tempP1)
        rhP1 = rh_2_oct16[i*24+j]
        print("rhumidity: ",rhP1)
        rsm = sw_net_oct16[i*24+j]
        print("measured Rs: ", rsm)
        # print(time1)
        # print(time2)
        # if ((3*j)<24):
        #     time0 = ta.time(i * 24 + j*3-3)
        #     # time3 = ta.time(i * 24 + j * 3 )
        #     if (j>7):
        #         time3 = ta.time(i*24+j*3-1)
        #     else:
        #         time3 = ta.time(i*24+j*3)
        #     # print(time0)
        #     # print(time3)
        #     radcaly3.net_radiation_step(radresy3, latitude, time0, time3, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
        #     swrad3 += radresy3.sw_radiation
        #     rarad3 += radresy3.ra
        # print(time1)
        # print(time)
        # print("--------")
        radcaly.net_radiation(radresy, latitude, time1, slope_deg, aspect_deg,tempP1, rhP1, elevation,rsm)
        radcaly1.net_radiation_step(radresy1, latitude, time1, time2, slope_deg, aspect_deg, tempP1, rhP1, elevation,rsm)

        # omega = 15*(j-12)*math.pi/180
        omega1 = radresy.sun_rise * math.pi / 180
        omega2 = radresy.sun_set * math.pi / 180
        # print(omega)
        # print("omega1:", omega1)
        netrad += radresy.sw_radiation
        swrad1 += radresy1.sw_radiation
        sw_simulated_1h.append(radresy.sw_radiation)

        rarad += radresy.ra
        rahrad += radresy.rah
        rarad1 += radresy1.ra
        rahrad1 += radresy1.rah
        j+=1
    net_rad.append(netrad/23)
    swcalc_step1.append(swrad1)
    # print("--- 1-h step ---")
    # print("swrad1: ",swrad1)
    ra_rad.append(rarad/23)
    ra_rad1.append(rarad1)
    # print("rarad1: ", rarad1)
    # radtheorint_arr.append(ratheor_int/23)
    # print("--- 3-h step ---")
    swcalc_step3.append(swrad3)
    # print("swrad3: ", swrad3)
    radcalc_step3.append(rarad3)
    # print("rarad3: ", rarad3)
    # print(dayi)
    # print("-----------")
    time1 = ta.time(i*24)
    time = ta.time(i*24+23)
    # print("--- 24-h step ---")
    # print(time1)
    # print(time)
    radcaly24.net_radiation_step(radresy24, latitude, time1, time, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
    # print("swstep: ", radresy24.sw_radiation)
    swcalc_step24.append(radresy24.sw_radiation)
    radcalc_step24.append(radresy24.ra)
    # print("-----------")
    # print(ratheor_int/23)
    # print(rarad/23)

    # print(radresy.omega1)
    # print(radresy.omega2)

    declin_arr.append(declin*180/math.pi)
    # print("omega1: ", omega1)
    # print("omega2: ", omega2)
    ra_theor = gsc*dd*(math.sin(declin)*math.sin(lat_rad)*math.cos(slope)*(omega2-omega1)-math.sin(declin)*math.cos(lat_rad)*math.sin(slope)*math.cos(aspect)*(omega2-omega1)+math.cos(declin)*math.cos(lat_rad)*math.cos(slope)*(math.sin(omega2)-math.sin(omega1))+math.cos(declin)*math.sin(lat_rad)*math.sin(slope)*math.cos(aspect)*(math.sin(omega2)-math.sin(omega1))-math.cos(declin)*math.sin(slope)*math.sin(aspect)*(math.cos(omega2)-math.cos(omega1)))
    # ra_theor =  gsc * dd * (
    #             math.sin(declin) * math.sin(lat) * math.cos(slope) * (omega2 - omega1)  + math.cos(declin) * math.cos(lat) * math.cos(
    #         slope) * (math.sin(omega2) - math.sin(omega1)))
    # print(ra_theor/math.pi/2)
    # print(dd)
    rat_rad.append(ra_theor/math.pi/2)
    rah_rad.append(rahrad / 23)
    j = 1
    i+=1
    dayi += 1
    doy.append(dayi)


# Let's plot the data we received from HbvSnow
fig, ax1 = plt.subplots(figsize=(7,5))
# ax2 = ax1.twinx()
# ax1.plot(doy, rat_rad, 'g.-', label='Ratheor-integral')
# ax1.plot(doy, ra_rad, 'r--', label='Ra-instant')
# ax1.plot(doy, net_rad, 'r', label='Rso-instant')
# ax1.plot(doy, radtheorint_arr, 'y', label='Rso')
# ax1.plot(doy, ra_rad1, 'k--', label='Ra-1h-step')
# ax1.plot(doy, swcalc_step1, 'k', label='Rso-1h-step')
# ax1.plot(doy, radcalc_step24, 'y-.', label='Ra-24h-step')
# ax1.plot(doy, swcalc_step24, 'y', label='Rso-24h-step')
ax1.plot(sw_net_oct16[0:506], 'm--', label='Rsm net')
ax1.plot(sw_simulated_1h, 'm', label='SW simulated net')
# plt.gcf().autofmt_xdate()
ax1.set_ylabel('Ra, Rso, [W/m^2]')
# ax2.set_ylabel('extraterrestrial radiation (Ra), [W/m^2]')
ax1.set_xlabel('Day-time')
plt.title("Golden, CO, surface slope 90 N")
plt.legend(loc="upper left")
# plt.legend(loc="lower center")
plt.axis([0,22,-100,500])
plt.grid(True)
plt.show()


print(" --------------------------------------------------------- ")
print(" --- end of single method test ------")
print(" --------------------------------------------------------- ")