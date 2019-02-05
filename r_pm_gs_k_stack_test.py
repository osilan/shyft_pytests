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

# single method test

radparam = api.RadiationParameter(0.2,1.0)
radcal = api.RadiationCalculator(radparam)
response =api.RadiationResponse();
time = api.utctime_now()
radcal.net_radiation(response, 40.4, time, 0.0, 0.0, 20.0, 40.0, 150.0, 0.0);
print(response.net_radiation)

pmparam=api.PenmanMonteithParameter(2.0,2.0,2.0)
pmcalculator=api.PenmanMonteithCalculator(pmparam)

ptgskmodel=api.pt_gs_k.PTGSKModel
print(ptgskmodel.parameter_t)
# ptgskmodel.parameter_t(2.0,2.0)

rpmgskmodel=api.r_pm_gs_k.RPMGSKModel

gsparam=api.GammaSnowParameter
aeparam=api.ActualEvapotranspirationParameter
kparam=api.KirchnerParameter
pcparam=api.PrecipitationCorrectionParameter
# rpmgskmodel.parameter_t(radparam,pmparam,gsparam,aeparam,kparam,pcparam)
# print(rpmgskmodel.parameter_t.lai)



