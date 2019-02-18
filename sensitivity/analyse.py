from sensitivity import run_radiation

latitude_deg = 44.0
slope_deg = 90.0
aspect_deg = 180.0
albedo = 0.05
turbidity = 1.0
elevation = 150.0
temperature = 20.0 # [degC], real data should be used
rhumidity = 50.0 #[%], real data should be used
gsc = 1367

run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity)