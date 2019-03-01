def run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity, flag = 'instant'):

    """Module creates shyft radiation model with different timesteps and run it for a defined period of time. """

    import numpy as np
    import math

    from shyft import api


    # single method test

    # here I will try to reproduce the Fig.1b from Allen2006 (reference)
    utc = api.Calendar()

    n = 365 # nr of time steps: 1 year, daily data
    t_start = utc.time(2002, 1, 1) # starting at the beginning of the year 1970

    # converting station data
    tempP1 = temperature # [degC], real data should be used
    rhP1 = rhumidity #[%], real data should be used
    rsm = 0.0

    radparam = api.RadiationParameter(albedo,turbidity)
    radcal_inst = api.RadiationCalculator(radparam)
    radcal_1h = api.RadiationCalculator(radparam)
    radcal_24h = api.RadiationCalculator(radparam)
    radcal_3h = api.RadiationCalculator(radparam)
    radres_inst = api.RadiationResponse()
    radres_1h = api.RadiationResponse()
    radres_24h = api.RadiationResponse()
    radres_3h = api.RadiationResponse()

    dayi = 0
    doy = api.DoubleVector()
    # running 24-h timestep
    step = api.deltahours(24)
    tadays = api.TimeAxis(t_start, step, n + 1)  # days
    k = 1
    while (k <= n):
        doy.append(dayi)
        k += 1
        dayi += 1
    rv_sw = []
    rv_ra = []
    if flag=='24-hour':
        dayi = 0
        doy = api.DoubleVector()

        # running 24-h timestep
        step = api.deltahours(24)
        tadays = api.TimeAxis(t_start, step, n+1)  # days
        k = 1
        while (k<=n):
            time1 = tadays.time(k-1)
            radcal_24h.net_radiation_step(radres_24h, latitude_deg, time1, step, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
            rv_sw.append(radres_24h.sw_radiation)
            rv_ra.append(radres_24h.ra)
            print(radres_24h.ra)
            doy.append(dayi)
            k+=1
            dayi += 1
        # doy.append(dayi)
    elif flag=='3-hour':

        # running 3h timestep
        step = api.deltahours(3)
        ta3 = api.TimeAxis(t_start, step, n * 8)  # hours, 1h timestep
        swrad_3h = []
        rarad_3h = []
        k = 1
        while (k<n*8):
            time0 = ta3.time(k-1)
            radcal_3h.net_radiation_step(radres_3h, latitude_deg, time0, step, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
            swrad_3h.append(radres_3h.sw_radiation)
            rarad_3h.append(radres_3h.ra)
            k+=1
        rv_sw = [sum(swrad_3h[i:i + 8]) for i in range(0, len(swrad_3h), 8)]
        rv_ra = [sum(rarad_3h[i:i + 8]) for i in range(0, len(rarad_3h), 8)]
    elif flag=='1-hour':
        # runing 1h timestep
        step = api.deltahours(1)
        ta = api.TimeAxis(t_start, step, n * 24)  # hours, 1h timestep
        swrad_1h = []
        rarad_1h = []
        rahrad_1h = []
        k = 1
        while (k<n*24):
            time1 = ta.time(k-1)
            radcal_1h.net_radiation_step(radres_1h, latitude_deg, time1, step, slope_deg, aspect_deg, tempP1, rhP1, elevation,rsm)
            swrad_1h.append(radres_1h.sw_radiation)
            rarad_1h.append(radres_1h.ra)
            rahrad_1h.append(radres_1h.rah)
            k += 1
        rv_sw = [sum(swrad_1h[i:i + 24]) for i in range(0, len(swrad_1h), 24)]
        rv_ra = [sum(rarad_1h[i:i + 24]) for i in range(0, len(rarad_1h), 24)]
    elif flag=='instant':
        # running instantaneous with dmin timstep
        minutes = 60
        dmin = 1
        step = api.deltaminutes(dmin)
        tamin = api.TimeAxis(t_start,step , n * 24 * minutes)
        swrad_inst = []
        rarad_inst = []
        rahrad_inst = []
        doy1 = []
        k = 0
        while (k < n*24*minutes):
            timemin = tamin.time(k)
            radcal_inst.net_radiation(radres_inst, latitude_deg, timemin, slope_deg, aspect_deg, tempP1, rhP1,
                                      elevation, rsm)
            swrad_inst.append(radres_inst.sw_radiation)
            rarad_inst.append(radres_inst.ra)
            rahrad_inst.append(radres_inst.rah)
            doy1.append(k)
            k += 1
        rv_sw = [sum(swrad_inst[i:i+24*minutes])//(24*minutes) for i in range(0,len(swrad_inst),24*minutes)]
        rv_ra = [sum(rarad_inst[i:i + 24 * minutes]) // (24 * minutes) for i in range(0, len(rarad_inst), 24 * minutes)]
    else:
        return 'Nothing todo. Please, specify timestep'



    return doy, rv_ra, rv_sw

