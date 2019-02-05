import os
import sys
import datetime as dt
import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from netCDF4 import Dataset

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

param = api.RadiationParameter(0.2,1.0)
api.RadiationCalculator(param)



# load the data from the example datasets
cell_data = Dataset( os.path.join(shyftdata_dir, 'netcdf/orchestration-testdata/cell_data.nc'))

# plot the coordinates of the cell data provided
# fetch the x- and y-location of the cells
x = cell_data.variables['x'][:]
y = cell_data.variables['y'][:]
z = cell_data.variables['z'][:]
crs = cell_data.variables['crs'][:]
cid = cell_data.variables['catchment_id'][:]

# and make a quick catchment map...
# using a scatter plot of the cells
fig, ax = plt.subplots(figsize=(15,5))
cm = plt.cm.get_cmap('rainbow')
elv_col = ax.scatter(x, y, c=z, marker='.', s=40, lw=0, cmap=cm)
# cm = plt.cm.get_cmap('gist_gray')
# cid_col = ax.scatter(x, y, c=cid, marker='.', s=40, lw=0, alpha=0.4, cmap=cm)
plt.colorbar(elv_col).set_label('catchment elevation [m]')
# plt.colorbar(cid_col).set_label('catchment indices [id]')
plt.title('Nea Nidelva Catchment')
plt.show()
# print(set(cid))
print(cell_data.variables.keys())

# let's first create a container that will hold all of our module domain cells

cell_data_vector = api.GeoCellDataVector()

# get dimensions from netcdf file
num_cells = cell_data.dimensions['cell'].size


for i in range(num_cells):
    gp = api.GeoPoint(x[i],y[i],z[i])
    cid = cell_data.variables['catchment_id'][i]
    cell_area = cell_data.variables['area'][i]

    glac = cell_data.variables['glacier-fraction'][i]
    lake = cell_data.variables['lake-fraction'][i]
    rsvr = cell_data.variables['reservoir-fraction'][i]
    frst = cell_data.variables['forest-fraction'][i]
    unsp = 1 - (glac + lake + rsvr + frst)

    land_cover_frac = api.LandTypeFractions(float(glac), float(lake), float(rsvr), float(frst), float(unsp))

    rad_fx = 0.9
    # note, for now we need to make sure we cast some types to pure python, not numpy
    geo_cell_data = api.GeoCellData(gp, float(cell_area), int(cid), rad_fx, land_cover_frac)

    cell_data_vector.append(geo_cell_data)

# put it all together to initialize a model, we'll use PTGSK

params = api.pt_gs_k.PTGSKParameter()
model = api.pt_gs_k.PTGSKModel(cell_data_vector, params)


re = api.ARegionEnvironment()

# map the variable names in the netcdf file to source types
source_map = {'precipitation': ('precipitation.nc',api.PrecipitationSource,re.precipitation),
              'global_radiation': ('radiation.nc',api.RadiationSource,re.radiation),
              'temperature' : ('temperature.nc',api.TemperatureSource,re.temperature),
              'wind_speed' : ('wind_speed.nc', api.WindSpeedSource, re.wind_speed),
              'relative_humidity': ('relative_humidity.nc',api.RelHumSource,re.rel_hum)}

for var,(file_name,source_type,source_vec) in source_map.items():
    nci = Dataset(os.path.join(shyftdata_dir,'netcdf/orchestration-testdata/' + file_name))

    time = api.UtcTimeVector([int(t) for t in nci.variables['time'][:]])
    delta_t = time[1]- time[0] if len(time) > 1 else api.deltahours(1)
    for i in range(nci.dimensions['station'].size):
        x = nci.variables['x'][i]
        y = nci.variables['y'][i]
        z = nci.variables['z'][i]
        gp = api.GeoPoint(float(x), float(y), float(z))
        data = nci.variables[var][:,i]
        time_axis = api.TimeAxis(int(time[0]),delta_t,len(time))
        dts = api.TsFactory().create_time_point_ts(time_axis.total_period(),time,data,api.POINT_AVERAGE_VALUE)
        # add it to the variable source vector
        source_vec.append(source_type(gp,dts))
    nci.close()

# source data, which will be fed to the interpolation
region_environment = re

def plot_station_data(region_environment):
    """plot the data within each source vector of the 'ARegionEnvironment'
    """
    for fv,sv in region_environment.variables:
        n_stn = len(sv)
        fig,ax = plt.subplots(figsize=(15,5))
        for stn in range(n_stn):
            t,d = [dt.datetime.utcfromtimestamp(t_.start) for t_ in sv[stn].ts.time_axis],sv[stn].ts.values
            ax.plot(t,d,label=stn)

        plt.title(fv)
        plt.legend()
        plt.show()

plot_station_data(region_environment)

