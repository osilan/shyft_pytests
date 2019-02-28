import run_pm
import plot_results
from matplotlib import pyplot as plt
import math

latitude_deg = 44.0
slope_deg = 90.0
aspect_deg = 0.0
orient = " South. "
if aspect_deg>=180:
    orient = " North. "
albedo = 0.05
turbidity = 1.0
elevation = 150.0
temperature = 20.0 # [degC], real data should be used
rhumidity = 50.0 #[%], real data should be used
gsc = 1367

# Data from weather station
ws_Th = [30.9, 31.2, 29.1, 28.3, 26.0, 22.9, 20.1, 19.9, 18.4, 16.5, 15.4, 15.5, 13.5, 13.2, 16.2, 20.0, 22.9, 26.4,
         28.2, 29.8, 30.9, 31.8, 32.5, 32.9, 32.4, 30.2, 30.6, 28.3, 25.9, 23.9]
ws_eah = [1.09, 1.15, 1.21, 1.21, 1.13, 1.20, 1.35, 1.35, 1.32, 1.26, 1.34, 1.31, 1.26, 1.24, 1.31, 1.36, 1.39, 1.25,
          1.17, 1.03, 1.02, 0.98, 0.87, 0.86, 0.93, 1.14, 1.27, 1.27, 1.17, 1.20]
ws_Rsh = [2.24, 1.65, 0.34, 0.32, 0.08, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.46, 1.09, 1.74, 2.34, 2.84,
          3.25, 3.21, 3.34, 2.96, 2.25, 1.35, 0.88, 0.79, 0.27, 0.03, 0.0]
ws_windspeedh = [4.07, 3.58, 1.15, 3.04, 2.21, 1.04, 0.58, 0.95, 0.30, 0.50, 1.00, 0.68, 0.69, 0.29, 1.24, 1.28, 0.88,
                 0.72, 1.52, 1.97, 2.07, 2.76, 2.90, 3.10, 2.77, 3.41, 2.78, 2.95, 3.27, 2.86]

def rhh_fun(Th, eah):
    rhh = []
    for i in range(len(Th)):
        svp_tmean = 0.6108 * math.exp(17.27 * Th[i] / (Th[i] + 237.3))
        rhh.append(eah[i] * 100 / svp_tmean)
    return rhh

ws_rhh = rhh_fun(ws_Th, ws_eah)


# Temperature impact
ws_Th_p20 = []
ws_Th_m20 = []
ws_Th_p50 = []
ws_Th_m50 = []
for t in ws_Th:
    ws_Th_p20.append(t + t * 0.2)
    ws_Th_m20.append(t - t * 0.2)
    ws_Th_p50.append(t + t * 0.5)
    ws_Th_m50.append(t - t * 0.5)

result = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
plt.plot(result,'g',label='Initial ws_Th')
result2 = run_pm.run_pm(ws_Th_m20, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
plt.plot(result2,'m--',label='-20%')
result4 = run_pm.run_pm(ws_Th_m50, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
plt.plot(result4,'b--',label='-50%')
result1 = run_pm.run_pm(ws_Th_p20, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
plt.plot(result1,'y-.',label='+20%')
result3 = run_pm.run_pm(ws_Th_p50, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
plt.plot(result3,'r-.',label='+50%')

plt.legend(loc="upper left")


plt.grid(True)
plt.show()


# windspeed impact
# ws_wsh_p20 = []
# ws_wsh_m20 = []
# ws_wsh_p50 = []
# ws_wsh_m50 = []
# for ws in ws_windspeedh:
#     ws_wsh_p20.append(ws + ws * 0.2)
#     ws_wsh_m20.append(ws - ws * 0.2)
#     ws_wsh_p50.append(ws + ws * 0.5)
#     ws_wsh_m50.append(ws - ws * 0.5)
#
# result = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh)
# plt.plot(result,'g',label='Initial ws_wsh')
# result2 = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_wsh_m20,ws_rhh)
# plt.plot(result2,'m--',label='-20%')
# result4 = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_wsh_m50,ws_rhh)
# plt.plot(result4,'b--',label='-50%')
# result1 = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_wsh_p20,ws_rhh)
# plt.plot(result1,'y-.',label='+20%')
# result3 = run_pm.run_pm(ws_Th, ws_eah, ws_Rsh, ws_wsh_p50,ws_rhh)
# plt.plot(result3,'r-.',label='+50%')
#
# plt.legend(loc="upper left")
#
#
# plt.grid(True)
# plt.show()

