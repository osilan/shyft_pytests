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

ymax = 300
yname = 'Rso, [W/m^2]'
xname = 'DOY'
plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Temperature dependency"
labels = ('Ra','Rso')
colors = ('r--','r', 'b--','b','g--','g','k--','k')
labloc = ("upper left","lower center", "upper center")

fig1, ax1 = plt.subplots(figsize=(7, 5))

temperature_array = [-40.0, -30.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0]
i=0
for temperature in temperature_array:
    result = run_radiation.run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
    # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
    plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(temperature), colors[i],labloc[2]) # 1h
    # colors = ('b--','b')
    # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
    # colors = ('k--','k')
    # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
    i+=1
plt.show()

slope_array = [0.0, 30.0, 45.0, 60.0, 75.0, 90.0]
ymax = 400
yname = 'Rso, [W/m^2]'
xname = 'DOY'
plotname = "Eugene, OR, "+orient+ "Slope dependency"
labels = ('Ra','Rso')
colors = ('r--','r', 'b--','b','g--','g','k--','k')
labloc = ("upper left","lower center", "upper center")

fig1, ax1 = plt.subplots(figsize=(7, 5))
i = 0
for slope in slope_array:
    result = run_radiation.run_radiation(latitude_deg, slope, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
    # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
    plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(slope), colors[i],labloc[1]) # 1h
    # colors = ('b--','b')
    # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
    # colors = ('k--','k')
    # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
    i+=1
plt.show()

lat_array = [0.0, 30.0, 45.0, 60.0, 75.0, 90.0]
slope_deg = 0.0
ymax = 450
ymin = -20
yname = 'Rso, [W/m^2]'
xname = 'DOY'
plotname = "Eugene, OR, surface slope: "+str(slope_deg)+orient+ "Latitude dependency"
labels = ('Ra','Rso')
colors = ('r--','r', 'b--','b','g--','g','k--','k','m--','m','y--','y')
labloc = ("upper left","lower center", "upper center")

fig1, ax1 = plt.subplots(figsize=(7, 5))
i = 0
for lat in lat_array:
    result = run_radiation.run_radiation(lat, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)
    # plot_results.plot_results(result[0], result[1], fig1, ax1, ymax, xname, yname, plotname, labels[0], colors[0])  # 1h
    plot_results.plot_results(result[0], result[2], fig1, ax1, ymax, xname, yname, plotname, str(lat), colors[i],labloc[1],ymin) # 1h
    # colors = ('b--','b')
    # plot_results.plot_results(result[0],result[3],result[4], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 3h
    # colors = ('k--','k')
    # plot_results.plot_results(result[0],result[5],result[6], fig1, ax1, ymax, xname, yname, plotname, labels, colors[i]) # 24h
    i+=1
plt.show()