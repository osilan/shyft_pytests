import os
import datetime as dt
#import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from shyft import api
import time

# importing the shyft modules needed for running a calibration
from shyft.repository.default_state_repository import DefaultStateRepository
from shyft.orchestration.configuration.yaml_configs import YAMLCalibConfig, YAMLSimConfig
from shyft.orchestration.simulators.config_simulator import ConfigCalibrator, ConfigSimulator

start_sim = time.time()
# conduct a configured simulation first.
# config_file_path = '/home/olga/workspace/shyft-data/neanidelv/yaml_config/neanidelva_simulation.yaml'
config_file_path = '/home/olga/workspace/shyft-data/neanidelv/yaml_config-rpmgsk/neanidelva_simulation.yaml'
cfg = YAMLSimConfig(config_file_path, "neanidelva")
simulator = ConfigSimulator(cfg)
# run the model, and we'll just pull the `api.model` from the `simulator`
simulator.run()
state = simulator.region_model.state

end_sim = time.time()
print("Elapsed time, simulation: "+ str(end_sim-start_sim))

start_cal = time.time()

# config_file_path = '/home/olga/workspace/shyft-data/neanidelv/yaml_config/neanidelva_calibration.yaml' # here is the *.yaml file
config_file_path = '/home/olga/workspace/shyft-data/neanidelv/yaml_config-rpmgsk/neanidelva_calibration.yaml' # here is the *.yaml file
cfg = YAMLCalibConfig(config_file_path, "neanidelva")

# to run a calibration using the above initiated configuration

calib = ConfigCalibrator(cfg)
n_cells = calib.region_model.size()
state_repos = DefaultStateRepository(calib.region_model)


results = calib.calibrate(cfg.sim_config.time_axis, state_repos.get_state(0).state_vector,cfg.optimization_method['name'],cfg.optimization_method['params'])

cells = calib.region_model.cells

end_cal = time.time()

print("Elapsed time, calibration: " + str(end_cal-start_cal))
# Get NSE of calibrated run:
result_params = []
for i in range(results.size()):
    result_params.append(results.get(i))
# print("Final NSE =", 1-calib.optimizer.calculate_goal_function(result_params))
print("Final KGE =", 1-calib.optimizer.calculate_goal_function(result_params))

print("{0:30s} {1:10s}".format("PARAM-NAME", "CALIB-VALUE"))

for i in range(results.size()):
    print("{0:30s} {1:10f}".format(results.get_name(i), results.get(i)))


# get the target vector and discharge statistics from the configured calibrator
target_obs = calib.tv[0]
disch_sim = calib.region_model.statistics.discharge(target_obs.catchment_indexes)
disch_obs = target_obs.ts.values
ts_timestamps = [dt.datetime.utcfromtimestamp(p.start) for p in target_obs.ts.time_axis]
# plot up the results
fig, ax = plt.subplots(1, figsize=(15,10))
ax.plot(ts_timestamps, disch_sim.values, lw=2, label = "sim")
ax.plot(ts_timestamps, disch_obs, lw=2, ls='--', label = "obs")
ax.set_title("observed and simulated discharge")
ax.legend()
ax.set_ylabel("discharge [m3 s-1]")
plt.show()

# We can make a quick plot of the data of each sub-catchment
fig, ax = plt.subplots(figsize=(20,15))

# plot each catchment discharge in the catchment_ids
for i,cid in enumerate(simulator.region_model.catchment_ids):
    # a ts.time_axis can be enumerated to it's UtcPeriod,
    # that will have a .start and .end of type utctimestamp
    # to use matplotlib support for datetime-axis, we convert it to datetime (as above)
    ts_timestamps = [dt.datetime.utcfromtimestamp(p.start) for p in simulator.region_model.time_axis]
    data = simulator.region_model.statistics.discharge([int(cid)]).values

    ax.plot(ts_timestamps,data, label = "{}".format(simulator.region_model.catchment_ids[i]))

fig.autofmt_xdate()
ax.legend(title="Catch. ID")
ax.set_ylabel("discharge [m3 s-1]")
plt.show()

parameters = calib.region_model.get_region_parameter() # fetching parameters from the simulator object
print(u"Calibrated rain/snow threshold temp: {} C".format(parameters.gs.tx)) # print current value of hs.tx

calib.optimizer.calculate_goal_function(result_params) # reset the parameters to the values of the calibration
parameters.gs.tx = 4.0 # setting a higher value for tx
s_init = state.extract_state([])
# type(state)
# s0=state_repos.get_state(0)
# s0.state_vector
# state.apply_state(s0, [])
# calib.run(state=s_init) # rerun the model, with new parameter
# disch_sim_p_high = calib.region_model.statistics.discharge(target_obs.catchment_indexes) # fetch discharge ts
# parameters.gs.tx = -4.0 # setting a higher value for tx
#
# calib.run(state=s_init) # rerun the model, with new parameter
#
# ts_timestamps = [dt.datetime.utcfromtimestamp(p.start) for p in target_obs.ts.time_axis]
# disch_sim_p_low = calib.region_model.statistics.discharge(target_obs.catchment_indexes) # fetch discharge ts
# fig, ax = plt.subplots(1, figsize=(15,10))
# ax.plot(ts_timestamps, disch_sim.values, lw=2, label = "calib")
# ax.plot(ts_timestamps, disch_sim_p_high.values, lw=2, label = "high")
# ax.plot(ts_timestamps, disch_sim_p_low.values, lw=2, label = "low")
# ax.plot(ts_timestamps, disch_obs, lw=2, ls='--', label = "obs")
# ax.set_title("investigating parameter gs.tx")
# ax.legend()
# ax.set_ylabel("discharge [m3 s-1]")
#
# plt.show()
# #
# s_init = state.extract_state([])

# reset the max water parameter
# parameters.gs.max_water = 1.0 # setting a higher value for tx
# calib.run(state=s_init) # rerun the model, with new parameter
# disch_sim_p_high = calib.region_model.statistics.discharge(target_obs.catchment_indexes) # fetch discharge ts
#
# parameters.gs.max_water = .001 # setting a higher value for tx
# calib.run(state=s_init) # rerun the model, with new parameter
# disch_sim_p_low = calib.region_model.statistics.discharge(target_obs.catchment_indexes) # fetch discharge ts
#
# # plot the results
# fig, ax = plt.subplots(1, figsize=(15,10))
# ax.plot(ts_timestamps, disch_sim.values, lw=2, label = "calib")
# ax.plot(ts_timestamps, disch_sim_p_high.values, lw=2, label = "high")
# ax.plot(ts_timestamps, disch_sim_p_low.values, lw=2, label = "low")
# ax.plot(ts_timestamps, disch_obs, lw=2, ls='--', label = "obs")
# ax.set_title("investigating parameter gs.max_water")
# ax.legend()
# ax.set_ylabel("discharge [m3 s-1]")
#
# plt.show()

simulator.run(state=s_init)

ts_timestamps = [dt.datetime.utcfromtimestamp(p.start) for p in target_obs.ts.time_axis]
disch_sim = simulator.region_model.statistics.discharge(target_obs.catchment_indexes) # fetch discharge ts
fig, ax = plt.subplots(1, figsize=(15,10))
ax.plot(ts_timestamps, disch_sim.values, lw=2, label = "calib")
ax.plot(ts_timestamps, disch_obs, lw=2, ls='--', label = "obs")
ax.set_title("investigating parameter gs.tx")
ax.legend()
ax.set_ylabel("discharge [m3 s-1]")

plt.show()