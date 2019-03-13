def run_pm(ws_Th, ws_eah, ws_Rsh, ws_windspeedh,ws_rhh, rnet, height_veg=0.12,dt=1, n=30,lai=2.0,rl = 144.0,height_ws = 3, height_t = 1.68, elevation = 1462.4):
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
    # print(len(tah))



    # print(ws_rhh)

    # ET_os_h = [0.61, 0.48, 0.14, 0.22, 0.12, 0.04, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.10, 0.19, 0.32, 0.46, 0.60, 0.72, 0.73, 0.79, 0.74, 0.62, 0.44, 0.35, 0.29, 0.17, 0.10, 0.07]
    # ET_rs_h = [0.82, 0.66, 0.19, 0.35, 0.21, 0.06, 0.02, 0.04, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.12, 0.23, 0.37, 0.52, 0.70, 0.85, 0.88, 0.97, 0.93, 0.81, 0.60, 0.52, 0.42, 0.29, 0.14, 0.10]
    # ET_os_h = [0.61, 0.48, 0.14, 0.22, 0.12, 0.04, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.10, 0.19, 0.32, 0.46, 0.60, 0.72, 0.73, 0.79, 0.74, 0.62, 0.44, 0.35, 0.29, 0.17, 0.10]
    # ET_rs_h = [0.82, 0.66, 0.19, 0.35, 0.21, 0.06, 0.02, 0.04, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.12, 0.23, 0.37, 0.52, 0.70, 0.85, 0.88, 0.97, 0.93, 0.81, 0.60, 0.52, 0.42, 0.29, 0.14]

    # SW_orig_h = [2.54, 1.96, 1.31, 0.63,  0.07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.56, 1.24, 1.90, 2.49, 2.97, 3.32, 3.50, 3.51, 3.34, 3.01, 2.54, 1.96, 1.31, 0.63, 0.07]
    # Ra_orig_h = [3.26, 2.52, 1.68, 0.81, 0.09, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.72, 1.59, 2.43, 3.19, 3.81, 4.26, 4.49, 4.51, 4.29, 3.87, 3.26, 2.52, 1.68, 0.81, 0.09]
    # LW_orig_h =[0.284, 0.262, 0.017, 0.017, 0.017, 0.016, 0.015, 0.015, 0.015, 0.014, 0.014, 0.014, 0.014, 0.014, 0.014, 0.223, 0.244, 0.278, 0.299, 0.331, 0.308, 0.0332, 0.315, 0.248, 0.134, 0.084, 0.147, 0.143, 0.143]
    # print(len(Rnet_orig_h))

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
    pmph=api.PenmanMonteithParameter(lai,height_ws,height_t,height_veg, rl)
    pmch=api.PenmanMonteithCalculator(pmph)
    pmrh =api.PenmanMonteithResponse()

    #PriestleyTaylor
    ptp = api.PriestleyTaylorParameter(0.2,1.26)
    ptc = api.PriestleyTaylorCalculator(0.2, 1.26)
    ptr = api.PriestleyTaylorResponse

    ET_ref_sim_h= []

    timeofday = []
    ET_pt_sim_h = []
    LW_sim_h = []
    SW_sim_h = []
    Ra_sim_h = []
    Rnet_sim_h = []

    for i in range(n-1):
        # print(i)
        # print("======================")
        # print("time: ", tah.time(i))
        timeofday.append(ta.time(i))
        # print("Th: ", temph_ts.v[i])
        # print("RHh: ", rhh_ts.v[i])
        # radch.net_radiation_step_asce_st(radrh, latitude, ta.time(i), step,slope_deg, aspect_deg, temph_ts.v[i], rhh_ts.v[i], elevation, rsh_ts.v[i]/c_MJm2h2Wm2 )
        # radch.net_radiation_step_asce_st(radrh, latitude, ta.time(i), step, slope_deg, aspect_deg, temph_ts.v[i],
        #                                  rhh_ts.v[i], elevation, 0.0)
        # radch.net_radiation_step_asce(radrh, latitude, tah.time(i), tah.time(i + 1), slope_deg, aspect_deg, temph_ts.v[i],rhh_ts.v[i], elevation, rsh_ts.v[i] / c_MJm2h2Wm2)
        # print("Ra: ", radrh.ra*c_MJm2h2Wm2)
        # Ra_sim_h.append(radrh.ra*c_MJm2h2Wm2*24)
        # print("Rs input:", rsh_ts.v[i]/c_MJm2h2Wm2)
        # print("Rso: ", radrh.sw_t)
        # SW_sim_h.append(radrh.sw_t*c_MJm2h2Wm2)
        # print("LW: ", -radrh.net_lw*c_MJm2h2Wm2)
        # LW_sim_h.append(-radrh.net_lw*c_MJm2h2Wm2)
        # print("RNet: ", radrh.net*c_MJm2h2Wm2 )
        # Rnet_sim_h.append(radrh.net*c_MJm2h2Wm2)
        pmch.reference_evapotranspiration_asce_st(pmrh, step,rnet[i], temph_ts.v[i],temph_ts.v[i],
                                                  rhh_ts.v[i], elevation, windspeedh_ts.v[i])
        # pmch.reference_evapotranspiration_asce_st(pmrh,step,radrh.net*c_MJm2h2Wm2,temph_ts.v[i],rhh_ts.v[i],elevation,windspeedh_ts.v[i])
        # pmch.reference_evapotranspiration_asce_full(pmrh,radrh.net_radiation*c_MJm2h2Wm2*(0.75+0.00002*elevation),temph_ts.v[i],rhh_ts.v[i],elevation,windspeedh_ts.v[i])
        # pmch.reference_evapotranspiration_asce_full(pmrh, radrh.net_radiation * c_MJm2h2Wm2,temph_ts.v[i], rhh_ts.v[i], elevation, windspeedh_ts.v[i])
        # pmch.reference_evapotranspiration_asce_full(pmrh, Rnet_orig_h[i], temph_ts.v[i], rhh_ts.v[i], elevation,windspeedh_ts.v[i])

        # print("======================")
        # print("ET_ref: ", pmrh.et_ref)
        ET_ref_sim_h.append(pmrh.et_ref)
        # print("======================")
        # ET_pt_sim_h.append(ptc.potential_evapotranspiration(temph_ts.v[i], radrh.sw_radiation, rhh_ts.v[i]*0.01)*3600) # the PT calculates [mm/s]
        ET_pt_sim_h.append(ptc.potential_evapotranspiration(temph_ts.v[i], rnet[i]/c_MJm2h2Wm2,rhh_ts.v[i] * 0.01) * 3600)  # the PT calculates [mm/s]
        # print(ET_pt_sim_h[i])

    return ET_ref_sim_h