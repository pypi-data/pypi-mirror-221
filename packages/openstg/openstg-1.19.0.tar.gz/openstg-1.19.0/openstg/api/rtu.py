from openstg.api import get_required_info, gisce_service, ReadOnlyResource
from flask import request, jsonify
from openstg.utils import ArgumentsParser


def get_url_from_ls(ls_name):
    """
    Gets the web services URL from the DB. Using the remote terminal unit name.
    :param ls_name: Line supervisor name
    :return: An string with the URL of the web service
    """
    try:
        search_params, limit, offset = ArgumentsParser.parse()
    except (ValueError, SyntaxError) as e:
        response = jsonify({
            'status': 'ERROR',
            'errors': {'filter': e.message}
        })
        response.status_code = 422
        return response

    ls_obj = gisce_service.get_obj('giscedata.line.supervisor')
    ls_ids = ls_obj.search([('name', '=', ls_name)])
    ls_data = ls_obj.read(ls_ids[0], ['rt_unit'])
    rtu_id, rtu_name = ls_data.get('rt_unit', (0, ''))

    rtu_obj = gisce_service.get_obj('giscedata.rtu')
    try:
        rtu = rtu_obj.read(rtu_id, ['rtu_ws_address'])
        return rtu.get('rtu_ws_address')
    except IndexError:
        raise IndexError("No RTU's were found")


def get_url_from_rtu(rtu_name):
    """
    Gets the web services URL from the DB. Using the remote terminal unit name.
    :param rtu_name: Remote terminal unit name
    :return: An string with the URL of the web service
    """
    try:
        search_params, limit, offset = ArgumentsParser.parse()
    except (ValueError, SyntaxError) as e:
        response = jsonify({
            'status': 'ERROR',
            'errors': {'filter': e.message}
        })
        response.status_code = 422
        return response

    rtu_obj = gisce_service.get_obj('giscedata.rtu')
    search_params = [('name', '=', rtu_name)]
    rtu_ids = rtu_obj.search(search_params)

    try:
        rtu = rtu_obj.read(rtu_ids[0], ['rtu_ws_address'])
        return rtu.get('rtu_ws_address')
    except IndexError:
        raise IndexError("No RTU's were found")


# PRIMEPLUS code: G50
class LSParametersExtendedAsync(ReadOnlyResource):
    def get(self, ls_name):
        info = get_required_info(request)
        from primestgplus.service import RTUService
        try:
            s = RTUService(info['request_id'], get_url_from_ls(ls_name), sync=False, source=info['source'])
            rep = s.get_ls_parameters_extended(ls_name, info['date_from'], info['date_to'])
            return rep, {'request_id': info['request_id']}
        except IndexError as e:
            return {'error': e.message}


# PRIMEPLUS code: S52
class GetRTUHourlyEnergyCurveAsync(ReadOnlyResource):

    def get(self, rtu_name):
        info = get_required_info(request)
        from primestgplus.service import RTUService
        try:
            s = RTUService(info['request_id'], get_url_from_rtu(rtu_name), sync=False, source=info['source'])
            rep = s.get_hourly_energy_curve(rtu_name, info['date_from'], info['date_to'])
            return rep, {'request_id': info['request_id']}
        except IndexError as e:
            return {'error': e.message}


# PRIMEPLUS code: S56
class LSParametersAsync(ReadOnlyResource):

    def get(self, ls_name):
        info = get_required_info(request)
        from primestgplus.service import RTUService
        try:
            s = RTUService(info['request_id'], get_url_from_ls(ls_name), sync=False, source=info['source'])
            rep = s.get_ls_parameters(ls_name, info['date_from'], info['date_to'])
            return rep, {'request_id': info['request_id']}
        except IndexError as e:
            return {'error': e.message}


# PRIMEPLUS code: S62
class RTUParametersAsync(ReadOnlyResource):

    def get(self, rtu_name):
        info = get_required_info(request)
        from primestgplus.service import RTUService
        try:
            s = RTUService(info['request_id'], get_url_from_rtu(rtu_name), sync=False, source=info['source'])
            rep = s.get_rtu_parameters(rtu_name, info['date_from'], info['date_to'])
            return rep, {'request_id': info['request_id']}
        except IndexError as e:
            return {'error': e.message}


class LSVoltageCurrentProfileAsync(ReadOnlyResource):

    def get(self, ls_name):
        info = get_required_info(request)
        from primestgplus.service import RTUService
        try:
            s = RTUService(info['request_id'], get_url_from_ls(ls_name), sync=False, source=info['source'])
            rep = s.get_ls_voltage_current_profile(ls_name, info['date_from'], info['date_to'])
            return rep, {'request_id': info['request_id']}
        except IndexError as e:
            return {'error': e.message}


rtu_resources = [
    # PRIME code: G50
    (LSParametersExtendedAsync, '/get-ls-parameters-extended/async/<string:ls_name>'),
    # PRIME code: S52
    (GetRTUHourlyEnergyCurveAsync, '/get-rtu-hourly-energy-curve/async/<string:rtu_name>'),
    # PRIME code: S56
    (LSParametersAsync, '/get-ls-parameters/async/<string:ls_name>'),
    # PRIME code: S62
    (RTUParametersAsync, '/get-rtu-parameters/async/<string:rtu_name>'),
    # PRIME code: S64
    (LSVoltageCurrentProfileAsync, '/get-ls-voltage-current-profile/async/<string:ls_name>'),
]