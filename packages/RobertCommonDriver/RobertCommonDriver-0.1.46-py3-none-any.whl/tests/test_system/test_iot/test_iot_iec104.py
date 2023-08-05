import time
from robertcommondriver.system.iot.iot_iec104 import IOTIEC104, unpack


def logging_print(**kwargs):
    print(kwargs)


def test_read():
    dict_config = {'host': '192.168.1.184', 'port': 2404, 'timeout': 4}
    dict_point = {}
    dict_point['iec1'] = {'point_writable': True, 'point_name': 'iec1', 'point_type': 1, 'point_address': 1, 'point_scale': '1'}
    dict_point['iec2'] = {'point_writable': True, 'point_name': 'iec2', 'point_type': 13, 'point_address': 16386, 'point_scale': '1'}

    client = IOTIEC104(configs = dict_config, points= dict_point)
    client.logging(call_logging=logging_print)
    while True:
        try:
            result = client.read(names=list(dict_point.keys()))
            print(result)
        except Exception as e:
            print(f"error: {e.__str__()}")
        time.sleep(1)


def test_parse():
    #r = IOTIEC104.APDU(bytes.fromhex('68 0E 06 00 08 00 64 01 06 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'))
    r = IOTIEC104.APDU(bytes.fromhex('68 0E 02 00 02 00 01 82 14 00 01 00 01 00 00 01 68 0E 04 00 02 00 64 01 0A 00 01 00 00 00 00 14'))
    #r = IOTIEC104.APDU(bytes.fromhex('68 0E 02 00 02 00 01 82 14 00 01 00 01 00 00 01'))
    print(r.info())


def test_read1():
    dict_config = {'host': '192.168.1.184', 'port': 2404, 'timeout': 5, 'zongzhao_interval': 0, 'zongzhao_timeout': 30, 'u_test_timeout': 10,  's_interval': 1}
    dict_point = {}
    dict_point['iec1'] = {'point_writable': True, 'point_name': 'iec1', 'point_type': 1, 'point_address': 100, 'point_scale': '1'}
    dict_point['iec2'] = {'point_writable': True, 'point_name': 'iec2', 'point_type': 13, 'point_address': 600, 'point_scale': '1'}

    client = IOTIEC104(configs = dict_config, points= dict_point)
    client.logging(call_logging=logging_print)
    while True:
        try:
            result = client.read(names=list(dict_point.keys()))
            print(result)
        except Exception as e:
            print(f"error: {e.__str__()}")
        time.sleep(5)


def test_frame():
    info = IOTIEC104.APDU(bytes.fromhex('68 0f 08 00 02 00 05 01 14 00 01 00 2c 01 00 00 00 ')).info()
    print(info)


test_frame()