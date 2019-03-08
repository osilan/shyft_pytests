import run_radiation
import plot_results
from matplotlib import pyplot as plt

latitude_deg = 44.0
slope_deg = 0.0
aspect_deg = 0.0
orient=" South. "
if aspect_deg>=180:
    orient=" North. "
albedo = 0.05
turbidity = 1.0
elevation = 150.0
temperature = 20.0 # [degC], real data should be used
rhumidity = 50.0 #[%], real data should be used
gsc = 1367

# ymax = 450
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Temperature dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k')
# labloc = ("upper left","lower center", "upper center")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
#
# temperature_array = [-40.0, -30.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0]
# i=0
# for temperature in temperature_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity, '1-hour')
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(temperature), colors[i],labloc[1])
#     i+=1
# plt.show()
# #
# slope_array = [0.0, 30.0, 45.0, 60.0, 75.0, 90.0]
# ymax = 400
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, "+orient+ "Slope dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k')
# labloc = ("upper left","lower center", "upper center")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for slope in slope_array:
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,'1-hour')
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(slope), colors[i],labloc[1]) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
# #
# lat_array = [0.0, 30.0, 45.0, 60.0, 75.0, 90.0]
# slope_deg = 0.0
# ymax = 450
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Surface slope: "+str(slope_deg)+orient+ "Latitude dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for lat in lat_array:
#     result = run_radiation.run_radiation(lat, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,'instant')
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(lat), colors[i],labloc[1],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
# rhumidity_array = [0.0, 20.0, 30.0, 40.0,50.0, 60.0, 70.0,80.0, 90.0, 100.0]
# slope_deg = 90.0
# ymax = 450
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Rhumidity dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for rhum in rhumidity_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhum)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(rhum), colors[i],labloc[1],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
# elevation_array = [-100.0, -20.0,0.0, 20.0, 100.0,400.0, 600.0, 800.0, 1000.0, 1800.0, 5000.0, 8800.0]
# slope_deg = 90.0
# ymax = 350
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Elevation dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for elev in elevation_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elev, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(elev), colors[i],labloc[3],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
albedo_array = [0.01, 0.05, 0.1, 0.25, 0.5, 0.99]
slope_deg = 0.0
ymax = 700
ymin = -20
yname = 'Rso, [W/m^2]'
xname = 'DOY'
plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Albedo dependency"
labels = ('Ra','Rso')
colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
labloc = ("upper left","lower center", "upper center","lower left")

fig1, ax1 = plt.subplots(figsize=(7, 5))
i = 0
for albedo in albedo_array:
    result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,'24-hour')
    plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(albedo), colors[i],labloc[3],ymin) # 1h
    i+=1
plt.show()
ymax = 30
ymin = -20
yname = 'NetLW, [W/m^2]'
xname = 'DOY'
i=0
fig2, ax2 = plt.subplots(figsize=(7, 5))
for albedo in albedo_array:
    result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,'24-hour','dingman')
    plot_results.plot_results(result[0], result[4], fig2, ax2, ymax, xname, yname, plotname, str(albedo), colors[i],labloc[3],ymin) # 1h
    print(result[4])
    result1 = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature,
                                         rhumidity, '1-hour', 'dingman')
    plot_results.plot_results(result1[0], result1[4], fig2, ax2, ymax, xname, yname, plotname, str(albedo), colors[i],
                              labloc[3], ymin)  # 1h
    i+=1
plt.show()
i=0
ymax = 30
ymin = -50
fig3, ax3 = plt.subplots(figsize=(7, 5))
for albedo in albedo_array:
    result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature,
                                         rhumidity, '1-hour', 'dingman')
    plot_results.plot_results(result[0], result[4], fig3, ax3, ymax, xname, yname, plotname, str(albedo), colors[i],
                              labloc[3], ymin)  # 1h
    print(result[4])
    i+=1
plt.show()
#
# turbidity_array = [0.01, 0.05, 0.1, 0.25, 0.5, 1.0]
# slope_deg = 0.0
# ymax = 450
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Turbidity dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for turbidity in turbidity_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(turbidity), colors[i],labloc[0],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
# elevation_array = [-100.0, -20.0,0.0, 20.0, 100.0,400.0, 600.0, 800.0, 1000.0, 1800.0, 5000.0, 8800.0]
# slope_deg = 90.0
# ymax = 350
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Elevation (corrected (0.75+0.00002*elevation) from ASCE-EWRI) dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for elev in elevation_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elev, albedo, turbidity, temperature, rhumidity)
#     corr_result = []
#     for r in result[2]:
#         corr_result.append(r*(0.75+0.00002*elev))
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], corr_result, fig1, ax1, ymax, xname, yname, plotname, str(elev), colors[i],labloc[3],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()


# slope_array = [0.0, 45.0, 90.0]
# slope_array = [90.0]
# slope_deg = 90.0
# aspect_deg = 180.0
# orient=" South. "
# if aspect_deg>=180:
#     orient=" North. "
# ymax = 120
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, "+"Slope: " + str(slope_deg) + orient
# labels = ('Ra','Rso')
#
# colors1 = ('r--','k--','b--', 'y--','g--')
# colors = ('r','k','b','y','g')
# labloc = ("upper left","lower center","upper left", "lower center", "upper center")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for slope in slope_array:
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature,rhumidity, '1-hour')
#     plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, 'Ra-1h', colors1[1],labloc[2])
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, 'Rso-1h', colors[1],labloc[2])
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature,
#                                          rhumidity, '3-hour')
#     plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, 'Ra-3h', colors1[2],
#                               labloc[2])
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, 'Rso-3h', colors[2],
#                               labloc[2])
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature,
#                                          rhumidity, '24-hour')
#     plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, 'Ra-24h', colors1[3],
#                               labloc[2])
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, 'Rso-24h', colors[3],
#                               labloc[2])
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature,
#                                          rhumidity, 'instant')
#     plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, 'Ra-inst', colors1[0],
#                               labloc[2])
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, 'Rso-inst', colors[0],
#                               labloc[2])
#     i+=1
# plt.show()


