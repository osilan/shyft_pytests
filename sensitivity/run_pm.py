def run_pm(ws_Th, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh, rnet, height_veg=0.12,dt=1, n=30,rl = 144.0,height_ws = 3, height_t = 1.68, elevation = 1462.4, method='asce-ewri'):
    """Run Penman-Monteith evapotranspiration model from SHyFT"""

    import numpy as np
    import math
    import shyft
    from shyft import api

    utc = api.Calendar()

    c_MJm2d2Wm2 = 0.086400
    c_MJm2h2Wm2 = 0.0036

    #for radiation model
    latitude = 40.4
    slope_deg = 0.0
    aspect_deg = 0.0




    # n = 30 # nr of time steps: 1 year, daily data
    t_starth = utc.time(2000, 6, 1,16,0,0,0) # starting at the beginning of the year 1970
    step = api.deltahours(dt)


    # Let's now create Shyft time series from the supplied lists of precipitation and temperature.
    # First, we need a time axis, which is defined by a starting time, a time step and the number of time steps.
    ta = api.TimeAxis(t_starth, step, n) # days

    # First, we convert the lists to shyft internal vectors of double values:
    temph_dv = api.DoubleVector.from_numpy(ws_Th)
    eah_dv = api.DoubleVector.from_numpy(ws_eah)
    rsh_dv = api.DoubleVector.from_numpy(ws_Rsh)
    windspeedh_dv = api.DoubleVector.from_numpy(ws_windspeedh)

    rhh_dv = api.DoubleVector.from_numpy(ws_rhh)

    # Finally, we create shyft time-series as follows:
    # (Note: This step is not necessarily required to run the single methods.
    #  We could also just work with the double vector objects and the time axis)
    instant = api.point_interpretation_policy.POINT_INSTANT_VALUE
    average = api.point_interpretation_policy.POINT_AVERAGE_VALUE

    temph_ts = api.TimeSeries(ta, temph_dv, point_fx=instant)
    eah_ts = api.TimeSeries(ta, eah_dv, point_fx=instant)
    rsh_ts = api.TimeSeries(ta, rsh_dv, point_fx=instant)
    windspeedh_ts = api.TimeSeries(ta, windspeedh_dv, point_fx=instant)


    #recalculated inputs:
    rhh_ts = api.TimeSeries(ta, rhh_dv, point_fx=instant)


    radph = api.RadiationParameter(0.26,1.0)
    radch = api.RadiationCalculator(radph)
    radrh =api.RadiationResponse()
    # pmph=api.PenmanMonteithParameter(lai,height_ws,height_t)
    pmph=api.PenmanMonteithParameter(height_veg,height_ws,height_t, rl)
    pmch=api.PenmanMonteithCalculator(pmph)
    pmrh =api.PenmanMonteithResponse()

    #PriestleyTaylor
    ptp = api.PriestleyTaylorParameter(0.2,1.26)
    ptc = api.PriestleyTaylorCalculator(0.2, 1.26)
    ptr = api.PriestleyTaylorResponse

    ET_ref_sim_h= []

    if method=='asce-ewri':

        for i in range(n-1):
             pmch.reference_evapotranspiration_asce_st(pmrh, step,rnet[i], temph_ts.v[i],temph_ts.v[i],
                                                      rhh_ts.v[i], elevation, windspeedh_ts.v[i])
             ET_ref_sim_h.append(pmrh.et_ref)

    else:
        for i in range(n - 1):
            pmch.reference_evapotranspiration_asce_full(pmrh, step,rnet[i], temph_ts.v[i], temph_ts.v[i], rhh_ts.v[i],
                                                        elevation, windspeedh_ts.v[i])
            ET_ref_sim_h.append(pmrh.et_ref)


    return ET_ref_sim_h