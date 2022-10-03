import pytest
import requests
import json

from powerbrain import Powerbrain

RESPONSE_PARAMS = json.loads("""
{
"title" : "Title",
"desc" : "Description",
"max_total_power" : 24000,
"power_reserve" : 5000,
"overdraft" : 0,
"max_total_evse_power" : 11000,
"lb_enabled" : true,
"disable_policy" : 1,
"ocpp_srv_tls_mode" : "off",
"ocpp_srv_port" : 19520,
"ocpp_srv_password" : "",
"cycle_time" : 3019,
"max_evses" : 3,
"shareware_mode" : false,
"version" : "1.6.1042",
"vsn" : 
{
"vendorid" : 52997,
"version" : 17171474,
"productid" : 1,
"serialno" : "ABC"
},
"ocpp_gateway_license_cnt" : 0,
"ocpp_gateway_licenses_used" : 0,
"dev_meta" : 
{
"evse_ajax" : "HTTP input",
"evse_evracing" : "EVracing",
"evse_go_e_homeplus_mobile" : "go-e HOME+ mobile",
"evse_heidelberg" : "Heidelberg Energy Control",
"evse_innogy_mb" : "innogy eBox professional Modbus",
"evse_keba_c_x" : "KEBA c-series/x-series",
"evse_mennekes_mb" : "Mennekes Amtron Modbus",
"evse_mockup" : "Simulation (VE)",
"evse_ocpp" : "EVSE with OCPP 1.6",
"evse_powerbrain" : "cFos Power Brain",
"evse_smartevse" : "Smart EVSE",
"evse_tesla" : "Tesla Wall Connector Gen 2",
"evse_wallbe" : "Wallbe Eco 2.0/2.0s",
"meter_abb_b23_b24" : "ABB B23 / B24",
"meter_ajax" : "HTTP input",
"meter_e3dc" : "E3/DC Solar Device",
"meter_kostal_http_json" : "Kostal Inverter HTTP",
"meter_mockup" : "Simulation (VM)",
"meter_orno_we516" : "Orno OR-WE-516",
"meter_pilot_spm9513" : "Pilot SPM9513",
"meter_powerbrain" : "cFos Power Brain",
"meter_powerfox_http_json" : "Powerfox HTTP",
"meter_sdm630" : "Eastron SDM630 / SDM630MCT",
"meter_sdm72dm" : "Eastron SDM72DM",
"meter_shelly_3em_http_json" : "Shelly HTTP",
"meter_sma_hm" : "SMA Homemanager Meter",
"meter_sma_inverter" : "SMA Inverter",
"meter_solarlog_cons" : "SolarLog Consumption",
"meter_solarlog_prod" : "SolarLog Production",
"meter_sonnen_battery_http_json" : "Sonnen Battery HTTP",
"meter_sonnen_consumption_http_json" : "Sonnen Consumption HTTP",
"meter_sonnen_grid_http_json" : "Sonnen Grid HTTP",
"meter_sonnen_production_http_json" : "Sonnen Production HTTP",
"meter_sunspec" : "SUNSPEC Solar Inverter",
"meter_virtual_available_evse_power" : "Power avail. for EVSEs (VM)",
"meter_virtual_consumed_power" : "Consumed non-EVSE Power (VM)",
"meter_virtual_evse_power" : "Consumed EVSE Power (VM)",
"meter_virtual_grid_demand" : "Grid Demand (VM)",
"meter_virtual_grid_demand_avg" : "Grid Demand, Avg. (VM)",
"meter_virtual_produced_power" : "Produced Power (VM)",
"meter_virtual_produced_power_avg" : "Produced Power, Avg. (VM)",
"meter_zz4_d513020" : "DTS 353 / ZZ4 D513020"
}
}""")

RESPONSE_DEV_INFO_CHARGING = json.loads("""
{
"params" : {
"title" : "Carport",
"desc" : "Ladepunkte",
"max_total_power" : 24000,
"power_reserve" : 5000,
"overdraft" : 0,
"max_total_evse_power" : 11000,
"lb_enabled" : true,
"disable_policy" : 1,
"ocpp_srv_tls_mode" : "off",
"ocpp_srv_port" : 19520,
"ocpp_srv_password" : "",
"cycle_time" : 3009,
"max_evses" : 3,
"shareware_mode" : false,
"version" : "1.6.1042",
"vsn" : 
{
"vendorid" : 52997,
"version" : 17171474,
"productid" : 1,
"serialno" : "ABC"
},
"ocpp_gateway_license_cnt" : 0,
"ocpp_gateway_licenses_used" : 0
},
"devices" : [
{
"dev_type" : "evse_powerbrain",
"device_enabled" : 1,
"name" : "cFos Power Brain",
"address" : "evse",
"id" : 1,
"dev_id" : "E1",
"number" : 2,
"desc" : "Left",
"com_err" : false,
"com_errors" : 0,
"last_error" : "",
"is_evse" : true,
"used_phases" : 0,
"is_mock" : false,
"label" : "",
"min_charging_cur" : 6000,
"max_power" : 11040,
"prio" : 1,
"charging_enabled" : true,
"cur_charging_power" : 6555,
"last_set_charging_cur" : 15942,
"total_energy" : 571766,
"phases" : 7,
"state" : 3,
"model" : "cFos Power Brain,1.0,1.6.1042,ABC",
"paused" : false,
"pause_time" : 300,
"pause_min_time" : 300,
"ucnt" : 0,
"evse" : 
{
"dc_sensor_faults" : 0,
"dc_last_test_time" : "2021-07-20T14:18:02.735Z",
"dc_sensor_fault" : false,
"dc_sensor_glitches" : 4,
"cp_state" : "Charging",
"cp_fault" : false,
"pp_state" : "no cable",
"charging" : true,
"current" : 15900,
"enabled" : true
},
"ocpp" : 
{
"status" : "disabled"
}
},
{
"dev_type" : "evse_powerbrain",
"device_enabled" : 1,
"name" : "cFos Power Brain",
"address" : "192.168.1.1:4701",
"id" : 1,
"dev_id" : "E2",
"number" : 4,
"desc" : "Right",
"com_err" : false,
"com_errors" : 3,
"last_error" : "not connected: 192.168.1.1.:4701",
"is_evse" : true,
"used_phases" : 0,
"is_mock" : false,
"label" : "",
"min_charging_cur" : 6000,
"max_power" : 11040,
"prio" : 1,
"charging_enabled" : true,
"cur_charging_power" : 0,
"last_set_charging_cur" : -1,
"total_energy" : 192289,
"phases" : 0,
"state" : 1,
"model" : "failed to connect",
"paused" : false,
"pause_time" : 300,
"pause_min_time" : 300,
"ucnt" : 0
}
],
"loadmgr_disabled" : false
}""")

def test_params(requests_mock):
    requests_mock.get('mock://powerbrain/cnf?cmd=get_params', json=RESPONSE_PARAMS)
    pb = Powerbrain('mock://powerbrain')
    pb.connect()
    assert pb.meta['title'] == 'Title'

def test_status(requests_mock):
    requests_mock.get('mock://powerbrain/cnf?cmd=get_dev_info', json=RESPONSE_DEV_INFO_CHARGING)
    requests_mock.get('mock://powerbrain/cnf?cmd=get_params', json=RESPONSE_PARAMS)
    pb = Powerbrain('mock://powerbrain')
    pb.connect()
    dev_info = pb.get_dev_info()
    assert dev_info['loadmgr_disabled'] == False
    assert dev_info['devices']['E1'] != None
    #assert requests.get('mock://powerbrain/cnf?cmd=get_dev_info').json()['loadmgr_disabled'] == False
