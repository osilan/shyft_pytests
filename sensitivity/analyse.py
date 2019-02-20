import run_radiation
import plot_results
from matplotlib import pyplot as plt

latitude_deg = 44.0
slope_deg = 90.0
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

# ymax = 300
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
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(temperature), colors[i],labloc[2]) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
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
#     result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(slope), colors[i],labloc[1]) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
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
#     result = run_radiation.run_radiation(lat, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(lat), colors[i],labloc[1],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()

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
# albedo_array = [0.01, 0.05, 0.1, 0.25, 0.5, 0.99]
# slope_deg = 90.0
# ymax = 350
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Albedo dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for albedo in albedo_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(albedo), colors[i],labloc[3],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()
#
# turbidity_array = [0.01, 0.05, 0.1, 0.25, 0.5, 1.0]
# slope_deg = 90.0
# ymax = 350
# ymin = -20
# yname = 'Rso, [W/m^2]'
# xname = 'DOY'
# plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Albedo dependency"
# labels = ('Ra','Rso')
# colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
# labloc = ("upper left","lower center", "upper center","lower left")
#
# fig1, ax1 = plt.subplots(figsize=(7, 5))
# i = 0
# for turbidity in turbidity_array:
#     result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
#     # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
#     plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(turbidity), colors[i],labloc[3],ymin) # 1h
#     # colors = ('b--','b')
#     # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
#     # colors = ('k--','k')
#     # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
#     i+=1
# plt.show()

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

aspect_array = [0.0, 90.0, 180] # S, EW, N
slope_deg = 45.0
ymax = 350
ymin = -20
yname = 'Rso, [W/m^2]'
xname = 'DOY'
plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Aspect dependency"
labels = ('Ra','Rso')
colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
labloc = ("upper left","lower center", "upper center","lower left")

fig1, ax1 = plt.subplots(figsize=(7, 5))
i = 0
for aspect in aspect_array:
    result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect, elevation, albedo, turbidity, temperature, rhumidity)
    # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
    plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(aspect), colors[i],labloc[3],ymin) # 1h
    # colors = ('b--','b')
    # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
    # colors = ('k--','k')
    # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
    i+=1
plt.show()