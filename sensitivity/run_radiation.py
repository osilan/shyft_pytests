def run_radiation(latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity):

    """Module creates shyft radiation model with different timesteps and run it for a defined period of time. """

    import numpy as np
    import math

    from shyft import api

    # single method test

    # here I will try to reproduce the Fig.1b from Allen2006 (reference)
    utc = api.Calendar()

    n = 365 # nr of time steps: 1 year, daily data
    day = np.arange(n) # day of water year

    t_start = utc.time(2002, 1, 1) # starting at the beginning of the year 1970
    dtdays = api.deltahours(24) # returns daily timestep in seconds
    dt = api.deltahours(1) # returns daily timestep in seconds
    dtminutes = api.deltaminutes(15)
    tamin = api.TimeAxis(t_start, api.deltaminutes(15), n * 24 * 4)

    # Let's now create Shyft time series from the supplied lists of precipitation and temperature.
    # First, we need a time axis, which is defined by a starting time, a time step and the number of time steps.
    tadays = api.TimeAxis(t_start, dtdays, n) # days
    # print(len(tadays))
    ta = api.TimeAxis(t_start, dt, n*24) # hours

    # print(len(ta))

    # converting station data
    lat = latitude_deg*math.pi/180# latitude
    slope = slope_deg*math.pi/180
    aspect = aspect_deg*math.pi/180
    tempP1 = temperature # [degC], real data should be used
    rhP1 = rhumidity #[%], real data should be used
    gsc = 1367

    radparam = api.RadiationParameter(albedo,turbidity)
    radcal_inst = api.RadiationCalculator(radparam)
    radcal_1h = api.RadiationCalculator(radparam)
    radcal_24h = api.RadiationCalculator(radparam)
    radcal_3h = api.RadiationCalculator(radparam)
    radres_inst = api.RadiationResponse()
    radres_1h = api.RadiationResponse()
    radres_24h = api.RadiationResponse()
    radres_3h = api.RadiationResponse()

    try:
        del rv_sw_inst
        del rv_sw_1h
        del rc_sw_3h
        del rv_sw_24h
    except:
        pass

    tempv_sw_inst = []
    tempv_ra_inst = []
    tempv_rah_inst = []
    rv_sw_inst = api.DoubleVector()
    rv_sw_1h = api.DoubleVector()
    rv_ra_inst = api.DoubleVector()
    rv_ra_1h = api.DoubleVector()
    rv_rah_inst = api.DoubleVector()
    rv_sw_24h = api.DoubleVector()
    rv_ra_24h = api.DoubleVector()
    rv_sw_3h = api.DoubleVector()
    rv_ra_3h = api.DoubleVector()

    i = 0
    dayi = 0
    doy = api.DoubleVector()

    while (i<n):

        swrad_1h = 0.0
        swrad_3h = 0.0

        rarad_1h = 0.0
        rarad_3h = 0.0
        j = 1
        rsm = 0.0

        rahrad_1h = 0.0
        while (j<24):
            time1 = ta.time(i*24+j-1)
            time2 = ta.time(i * 24 + j)
            if ((3*j)<24):
                time0 = ta.time(i * 24 + j*3-3)
                if (j>7):
                    time3 = ta.time(i*24+j*3-1)
                else:
                    time3 = ta.time(i*24+j*3)
                radcal_3h.net_radiation_step(radres_3h, latitude_deg, time0, time3, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
                swrad_3h += radres_3h.sw_radiation
                rarad_3h += radres_3h.ra
            radcal_1h.net_radiation_step(radres_1h, latitude_deg, time1, time2, slope_deg, aspect_deg, tempP1, rhP1, elevation,rsm)
            swrad_1h += radres_1h.sw_radiation
            rarad_1h += radres_1h.ra
            rahrad_1h += radres_1h.rah

            k = 0
            swrad_inst = []
            rarad_inst = []
            rahrad_inst = []
            while (k <= 4):
                timemin = tamin.time(i * 24 + j-1 + k)
                print(timemin)
                print(i * 24 + j-1 + k)
                radcal_inst.net_radiation(radres_inst, latitude_deg, timemin, slope_deg, aspect_deg, tempP1, rhP1,elevation, rsm)
                swrad_inst.append(radres_inst.sw_radiation)
                rarad_inst.append(radres_inst.ra)
                rahrad_inst.append(radres_inst.rah)
                k+=1

            j+=1
            tempv_sw_inst.append(sum(swrad_inst)/len(swrad_inst))
            # print(tempv_sw_inst)
            # print(len(tempv_sw_inst))
            tempv_rah_inst.append(sum(rahrad_inst)/len(rahrad_inst))
            tempv_ra_inst.append(sum(rarad_inst) / len(rarad_inst))
            swrad_inst.clear()
            rarad_inst.clear()
            rahrad_inst.clear()

        rv_sw_inst.append(sum(tempv_sw_inst)/len(tempv_sw_inst))
        rv_ra_inst.append(sum(tempv_ra_inst)/len(tempv_ra_inst))
        rv_rah_inst.append(sum(tempv_rah_inst)/len(tempv_rah_inst))
        # print(len(rv_sw_inst))
        tempv_sw_inst.clear()
        tempv_ra_inst.clear()
        tempv_rah_inst.clear()

        rv_sw_1h.append(swrad_1h)
        rv_ra_1h.append(rarad_1h)
        rv_sw_3h.append(swrad_3h)
        rv_ra_3h.append(rarad_3h)
        time1 = ta.time(i*24)
        time = ta.time(i*24+24-1)
        radcal_24h.net_radiation_step(radres_24h, latitude_deg, time1, time, slope_deg, aspect_deg, tempP1, rhP1, elevation, rsm)
        rv_sw_24h.append(radres_24h.sw_radiation)
        rv_ra_24h.append(radres_24h.ra)

        j = 1
        i+=1
        dayi += 1
        doy.append(dayi)



    k = 0
    minutes = 60
    tamin = api.TimeAxis(t_start, api.deltaminutes(1), n * 24 * minutes)

    swrad_inst = []
    rarad_inst = []
    rahrad_inst = []
    doy1 = []
    # doy1.clear()
    while (k < n*24*minutes):

        rsm = 0.0
        timemin = tamin.time(k)
        # print(timemin)
        # print(k)
        radcal_inst.net_radiation(radres_inst, latitude_deg, timemin, slope_deg, aspect_deg, tempP1, rhP1,
                                  elevation, rsm)
        swrad_inst.append(radres_inst.sw_radiation)
        rarad_inst.append(radres_inst.ra)
        rahrad_inst.append(radres_inst.rah)
        doy1.append(k)
        k += 1


    rv_sw_inst = [sum(swrad_inst[i:i+24*minutes])//(24*minutes) for i in range(0,len(swrad_inst),24*minutes)]
    rv_ra_inst = [sum(rarad_inst[i:i + 24 * minutes]) // (24 * minutes) for i in range(0, len(rarad_inst), 24 * minutes)]
    # print(tempv_sw_inst)
    # print(len(tempv_sw_inst))
    # tempv_rah_inst.append(sum(rahrad_inst) / len(rahrad_inst))
    # tempv_ra_inst.append(sum(rarad_inst) / len(rarad_inst))
    # swrad_inst.clear()
    # rarad_inst.clear()
    # rahrad_inst.clear()
    #
    # rv_sw_inst.append(sum(tempv_sw_inst) / len(tempv_sw_inst))
    # rv_ra_inst.append(sum(tempv_ra_inst) / len(tempv_ra_inst))
    # rv_rah_inst.append(sum(tempv_rah_inst) / len(tempv_rah_inst))
    # # print(len(rv_sw_inst))
    # tempv_sw_inst.clear()
    # tempv_ra_inst.clear()
    # tempv_rah_inst.clear()


    return doy, rv_ra_1h, rv_sw_1h, rv_ra_3h, rv_sw_3h, rv_ra_24h, rv_sw_24h, rv_ra_inst, rv_sw_inst

