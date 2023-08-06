import socket
import subprocess
from datetime import datetime, timedelta, date
from urlparse import urlparse

from flask import jsonify, Response, abort, request, current_app
from flask_restplus import Resource, Api
from primestg.service import Service, format_timestamp
from primestg.utils import DLMSTemplates, PrimeTemplates
from primestg.ziv_service import ZivService
from werkzeug.exceptions import MethodNotAllowed

from openstg.utils import ArgumentsParser, get_season
from openstg.config import AppSetup
from openstg.services import GISCEService
from constants import supported_rtu_reports, supported_orders, supported_reports
from openstg.utils import get_library_version


class GisceStg(Api):
    pass

gisce_service  = GISCEService()

class BaseResource(Resource):
    pass


def get_url_from_cnc(cnc_name):
    """
    Gets the web services URL from the DB. Using the concentrator name.
    :param cnc_name: Concentrator name
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

    concentrador_obj = gisce_service.get_obj('tg.concentrator')
    search_params = [('name', '=', cnc_name)]
    concentrador_ids = concentrador_obj.search(search_params)
    concentrador = concentrador_obj.read(concentrador_ids[0], ['dc_ws_address'])

    return concentrador.get('dc_ws_address')


def get_field_from_cnc(cnc_name, fieldname):
    """
    Gets the web services URL from the DB. Using the concentrator name.
    :param cnc_name: Concentrator name
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

    concentrador_obj = gisce_service.get_obj('tg.concentrator')
    search_params = [('name', '=', cnc_name)]
    concentrador_ids = concentrador_obj.search(search_params)
    concentrador = concentrador_obj.read(concentrador_ids[0])

    if fieldname in concentrador:
        return concentrador.get(fieldname)

    return None


def get_cnc_url_from_register(register_name):
    """
    Gets the web services URL from the DB. Using the register name.
    :param register_name: The name of the register
    :return: The URL of the web services of the concentrator
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

    reg_name = register_name.split(',')[0]
    search_params = [('name', '=', reg_name)]
    registrador_obj = gisce_service.get_obj('giscedata.registrador')
    registrador_ids = registrador_obj.search(search_params)

    if registrador_ids:
        registrador = registrador_obj.read(registrador_ids[0])

        concentrador_obj = gisce_service.get_obj('tg.concentrator')
        concentrador = concentrador_obj.read(registrador['cnc_id'][0])

        return concentrador['dc_ws_address']


def get_required_info(request):
    """
    Gets the information needed to ask for every report
    :param request: Contains the parameters given in the path
    :return: A dictionary containing the required information
    """
    now = datetime.now()

    date_from = format_timestamp(now)
    date_to = format_timestamp(now + timedelta(hours=1))

    if request.args.get('from'):
        date_from = '{}{}{}'.format(request.args.get('from'), '000',
                                    get_season(request.args.get('from')))
    if request.args.get('to'):
        date_to = '{}{}{}'.format(request.args.get('to'), '000',
                                  get_season(request.args.get('to')))
    AppSetup.configure_counter(current_app)

    return {
        'date_from': date_from,
        'date_to': date_to,
        'source': request.args.get('source'),
        'request_id': current_app.counter.next()
    }


def test_cnc_connection(public_ip, dc_ws_port=None):
    status = False
    if public_ip:
        status = subprocess.call('/bin/ping -c 1 {}'.format(public_ip), shell=True) == 0
        if not status and dc_ws_port:
            s = socket.socket()
            s.settimeout(10.0)
            error_ws_conn = s.connect_ex((public_ip, dc_ws_port))
            s.close()
            status = error_ws_conn == 0
    return status


class ApiCatchall(BaseResource):

    def get(self, path):
        abort(404)

    post = get
    put = get
    delete = get
    patch = get


class ReadOnlyResource(BaseResource):

    def not_allowed(self):
        raise MethodNotAllowed

    post = patch = not_allowed


# Utilities


class SupportedReports(ReadOnlyResource):

    def get(self):
        return jsonify(supported_reports)


class SupportedSpecificReports(ReadOnlyResource):

    def get(self, type='cnc'):
        if type == 'rtu':
            return jsonify(supported_rtu_reports)
        elif type == 'cnc':
            return jsonify(supported_reports)
        return "Unsuported type use rtu or cnc"


class SupportedOrders(ReadOnlyResource):

    def get(self):
        return jsonify(supported_orders)


class StatusCNC(ReadOnlyResource):

    def post(self, cnc_name):
        url = get_url_from_cnc(cnc_name)
        parse = urlparse(url)
        public_ip = parse.hostname
        dc_ws_port = parse.port
        connects = test_cnc_connection(public_ip, dc_ws_port)
        return jsonify({'status': ('up' if connects else 'down')})


class PingMachine(ReadOnlyResource):

    def post(self, public_ip, dc_ws_port):
        resp_ping = test_cnc_connection(public_ip, int(dc_ws_port))
        return jsonify({'status': ('up' if resp_ping else 'down')})


# Send Orders

#PRIME code: B11
class OrderRequest(ReadOnlyResource):

    def get(self, cnc_name, txx):
        info = get_required_info(request)
        generic_values = {
            'id_req': 'B11',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'version': get_field_from_cnc(cnc_name, 'dc_ws_stg_version')
        }
        payload = {
            'txx': txx,
            'date_from': info['date_from'],
            'date_to': info['date_to']
        }

        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        order = s.get_order_request(generic_values, payload)
        resp = Response(order, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# DLMS Templates
class DLMStemplates(ReadOnlyResource):
    def get(self):
        dlms_templates = DLMSTemplates().templates
        return jsonify([{'name': key, 'description': dlms_templates[key]['description']} for key in dlms_templates])


# DLMS Templates by Type
class DLMStemplatesByType(ReadOnlyResource):
    def get(self, template_type):
        return DLMSTemplates().get_available_templates(template_type=template_type)


# PRIME code: B12
class ChangeDLMScontracts(ReadOnlyResource):
    def post(self, cnc_name, dlms_template):
        meter_name = request.json.get('meter_name', None)
        activation_date_text = request.json.get('activation_date', None)
        info = get_required_info(request)

        generic_values = {
            'id_req': 'B12',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'cnt': meter_name,
            'version': get_field_from_cnc(cnc_name, 'dc_ws_stg_version'),
        }

        try:
            url = get_url_from_cnc(cnc_name)

            if not url or url == 'None':
                return self.im_a_teapot('No url from Cnc {}'.format(cnc_name))

            s = Service(info['request_id'], url, sync=True)

            if activation_date_text is None:
                activation_date = datetime.now() + timedelta(days=1)
            else:
                activation_date = datetime.strptime(activation_date_text, '%Y-%m-%d')

            payload = {
                'template': dlms_template,
                'date': activation_date,
                'date_to': format_timestamp(datetime.now()+timedelta(hours=1)),
                'date_from': format_timestamp(datetime.now()),
            }

            order = s.order_raw_dlms(generic_values, payload)
            resp = Response(order, mimetype="text/plain")
            resp.headers['request_id'] = info['request_id']
            return resp.response
        except Exception as e:
            return e

    def im_a_teapot(self, message):
        response = jsonify({'message': message})
        response.status_code = 418
        return response

# PRIME code: B12
class ChangeDLMScurrentpowers(ReadOnlyResource):
    def post(self, cnc_name):
        meter_name = request.json.get('meter_name', None)
        p1 = request.json.get('p1', None)
        p2 = request.json.get('p2', None)
        p3 = request.json.get('p3', None)
        p4 = request.json.get('p4', None)
        p5 = request.json.get('p5', None)
        p6 = request.json.get('p6', None)

        info = get_required_info(request)

        generic_values = {
            'id_req': 'B12',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'cnt': meter_name,
            'version': get_field_from_cnc(cnc_name, 'dc_ws_stg_version'),
        }

        try:
            url = get_url_from_cnc(cnc_name)

            if not url or url == 'None':
                return self.im_a_teapot('No url from Cnc {}'.format(cnc_name))

            s = Service(info['request_id'], url, sync=True)

            payload = {
                'template': 'C1_ACT_POWERS',
                'powers': [p1, p2, p3, p4, p5, p6],
                'date_to': format_timestamp(datetime.now()+timedelta(hours=1)),
                'date_from': format_timestamp(datetime.now()),
            }

            order = s.order_raw_dlms(generic_values, payload)
            resp = Response(order, mimetype="text/plain")
            resp.headers['request_id'] = info['request_id']
            return resp.response
        except Exception as e:
            return e

    def im_a_teapot(self, message):
        response = jsonify({'message': message})
        response.status_code = 418
        return response


class ChangeDLMSlatentpowers(ReadOnlyResource):
    def post(self, cnc_name):
        meter_name = request.json.get('meter_name', None)
        p1 = request.json.get('p1', None)
        p2 = request.json.get('p2', None)
        p3 = request.json.get('p3', None)
        p4 = request.json.get('p4', None)
        p5 = request.json.get('p5', None)
        p6 = request.json.get('p6', None)
        textdate = request.json.get('date', None)

        info = get_required_info(request)

        generic_values = {
            'id_req': 'B12',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'cnt': meter_name,
            'version': get_field_from_cnc(cnc_name, 'dc_ws_stg_version'),
        }

        try:
            url = get_url_from_cnc(cnc_name)

            if not url or url == 'None':
                return self.im_a_teapot('No url from Cnc {}'.format(cnc_name))

            s = Service(info['request_id'], url, sync=True)

            payload = {
                'template': 'C1_LAT_POWERS',
                'powers': [p1, p2, p3, p4, p5, p6],
                'date': datetime.strptime(textdate, '%Y-%m-%d').date(),
                'date_to': format_timestamp(datetime.now()+timedelta(hours=1)),
                'date_from': format_timestamp(datetime.now()),
            }

            order = s.order_raw_dlms(generic_values, payload)
            resp = Response(order, mimetype="text/plain")
            resp.headers['request_id'] = info['request_id']
            return resp.response
        except Exception as e:
            return e

    def im_a_teapot(self, message):
        response = jsonify({'message': message})
        response.status_code = 418
        return response


class GetDLMSTrafoRatio(ReadOnlyResource):
    def post(self, cnc_name):
        meter_name = request.json.get('meter_name', None)
        info = get_required_info(request)

        generic_values = {
            'id_req': 'B12',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'cnt': meter_name,
        }

        try:
            url = get_url_from_cnc(cnc_name)

            if not url or url == 'None':
                return self.im_a_teapot('No url from Cnc {}'.format(cnc_name))

            s = Service(info['request_id'], url, sync=True)

            payload = {
                'template': 'TRAFO_RATIO',
                'date_to': format_timestamp(datetime.now() + timedelta(hours=1)),
                'date_from': format_timestamp(datetime.now()),
            }

            order = s.order_raw_dlms(generic_values, payload)
            resp = Response(order, mimetype="text/plain")
            resp.headers['request_id'] = info['request_id']
            return resp.response
        except Exception as e:
            return e

    def im_a_teapot(self, message):
        response = jsonify({'message': message})
        response.status_code = 418
        return response


class UploadZIVCycle(ReadOnlyResource):
    def post(self, cnc_name):
        cycle_data = request.json.get('cycle_data', None)
        info = get_required_info(request)

        try:
            url = get_field_from_cnc(cnc_name, 'dc_web_address')
            username = 'admin'
            password = get_field_from_cnc(cnc_name, 'w_password')

            if not url or url == 'None':
                return self.im_a_teapot('No url from Cnc {}'.format(cnc_name))

            zs = ZivService(url, user=username, password=password, sync=True)

            result = zs.send_cycle("cycle", cycle_data)
            return result.status_code
        except Exception as e:
            return e

    def im_a_teapot(self, message):
        response = jsonify({'message': message})
        response.status_code = 418
        return response

# PRIME code: B03
class CutoffReconnection(ReadOnlyResource):

    def post(self, cnc_name):
        info = get_required_info(request)
        meter_name = request.json.get('meter_name', None)
        order = request.json.get('order', None)

        generic_values = {
            'id_req': 'B03',
            'id_pet': str(info['request_id']),
            'cnc': cnc_name,
            'cnt': meter_name,
            'version': get_field_from_cnc(cnc_name, 'dc_ws_stg_version'),
        }

        assert order in ('cutoff', 'reconnect', 'connect'), "Order not recognized"

        if order == 'cutoff':
            payload = {
                'order_param': '0',
            }
        elif order == 'reconnect':
            payload = {
                'order_param': '1'
            }
        elif order == 'connect':
            payload = {
                'order_param': '2'
            }

        payload.update({
            'date_from': info['date_from'],
            'date_to': info['date_to']
        })
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        order = s.get_cutoff_reconnection(generic_values, payload)
        resp = Response(order, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp.response


# Synchronous requests

# PRIME code: S01
class InstantData(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_instant_data(register_name)
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S02
class DailyIncremental(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_daily_incremental(register_name, info['date_from'],
                                      info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllDailyIncremental(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_daily_incremental(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S04
class MonthlyBilling(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_monthly_billing(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllMonthlyBilling(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_monthly_billing(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S05
class DailyAbsolute(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_daily_absolute(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllDailyAbsolute(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_daily_absolute(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S06
class RegisterParameters(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_meter_parameters(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllRegisterParameters(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_meter_parameters(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S09
class RegisterEvents(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_meter_events(register_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllRegisterEvents(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_meter_events(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp

# PRIME code: S12
class ConcentratorParameters(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=True)
        rep = s.get_concentrator_parameters(cnc_name, info['date_from'],
                                            info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S21
class AdvancedInstantData(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_advanced_instant_data(register_name)
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S23
class ContractDefinition(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=True)
        rep = s.get_contract_definition(register_name, info['date_from'],
                                        info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# PRIME code: S24
class ConcentratorMeters(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_concentrator_meters(cnc_name, info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


class AllContractDefinition(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=True)
        rep = s.get_all_contract_definition(info['date_from'], info['date_to'])
        resp = Response(rep, mimetype="text/plain")
        resp.headers['request_id'] = info['request_id']
        return resp


# Asynchronous requests

# PRIME code: S02
class DailyIncrementalAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_daily_incremental(register_name, info['date_from'],
                                      info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllDailyIncrementalAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_daily_incremental(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S04
class MonthlyBillingAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_monthly_billing(register_name, info['date_from'],
                                    info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllMonthlyBillingAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_monthly_billing(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S05
class DailyAbsoluteAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_daily_absolute(register_name, info['date_from'],
                                   info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllDailyAbsoluteAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_daily_absolute(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S06
class RegisterParametersAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_meter_parameters(register_name, info['date_from'],
                                        info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllRegisterParametersAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_meter_parameters(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S09
class RegisterEventsAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_meter_events(register_name, info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllRegisterEventsAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_meter_events(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S12
class ConcentratorParametersAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_concentrator_parameters(cnc_name, info['date_from'],
                                            info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S18
class DailyAverageVoltageAndCurrentAsync(ReadOnlyResource):
    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_daily_average_voltage_and_current(register_name, info['date_from'],
                                    info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllDailyAverageVoltageAndCurrentAsync(ReadOnlyResource):
    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_daily_average_voltage_and_current(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S18
class CutoffsStatusAsync(ReadOnlyResource):
    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_cutoffs_status(register_name, info['date_from'],
                                    info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllCutoffsStatusAsync(ReadOnlyResource):
    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_cutoffs_status(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}

# PRIME code: S23
class ContractDefinitionAsync(ReadOnlyResource):

    def get(self, register_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_cnc_url_from_register(register_name),
                    sync=False, source=info['source'])
        rep = s.get_contract_definition(register_name, info['date_from'],
                                      info['date_to'])
        return rep, {'request_id': info['request_id']}


# PRIME code: S24
class ConcentratorMetersAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name), sync=False, source=info['source'])
        rep = s.get_concentrator_meters(cnc_name, info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


class AllContractDefinitionAsync(ReadOnlyResource):

    def get(self, cnc_name):
        info = get_required_info(request)
        s = Service(info['request_id'], get_url_from_cnc(cnc_name),
                    sync=False, source=info['source'])
        rep = s.get_all_contract_definition(info['date_from'], info['date_to'])
        return rep, {'request_id': info['request_id']}


class TestRESTAPI(ReadOnlyResource):
    def get(self):
        # TEST WSDL
        try:
            import primestg
            wsdl_path = primestg.get_data('WS_DC.wsdl')
            with open(wsdl_path, 'r') as wsdl_file:
                pass  # just test that can be opened
        except Exception as e:
            wsdl_path = False

        # TEST SQLITE COUNTER
        AppSetup.configure_counter(current_app)

        # TEST ERP BACKEND CONNECTION
        company_obj = gisce_service.get_obj('res.company')
        company_data = company_obj.read(1, ['name'])

        # TEST VERSIONS
        versions = {
            'openstg': get_library_version('openstg'),
            'primestg': get_library_version('primestg'),
            'primestgplus': get_library_version('primestgplus')
        }

        return {
            'has_wsdl': wsdl_path,
            'response': company_data['name'],
            'request_id': current_app.counter.current(),
            'versions': versions
        }



resources = [
    # Utilities
    (SupportedReports, '/supported_reports'),
    (SupportedSpecificReports, '/supported_reports/<string:type>'),
    (SupportedOrders, '/supported_orders'),
    (StatusCNC, '/status/<string:cnc_name>'),
    (PingMachine, '/ping/<string:public_ip>/<string:dc_ws_port>'),

    # Synchronous requests
    # PRIME code: S01
    (InstantData, '/instant-data/<string:register_name>'),
    # PRIME code: S02
    (DailyIncremental, '/daily-incremental/<string:register_name>'),
    (AllDailyIncremental, '/<string:cnc_name>/daily-incremental'),
    # PRIME code: S04
    (MonthlyBilling, '/monthly-billing/<string:register_name>'),
    (AllMonthlyBilling, '/<string:cnc_name>/monthly-billing'),
    # PRIME code: S05
    (DailyAbsolute, '/daily-absolute/<string:register_name>'),
    (AllDailyAbsolute, '/<string:cnc_name>/daily-absolute'),
    # PRIME code: S06
    (RegisterParameters, '/meter-parameters/<string:register_name>'),
    (AllRegisterParameters, '/<string:cnc_name>/meter-parameters'),
    # PRIME code: S09
    (RegisterEvents, '/meter-events/<string:register_name>'),
    (AllRegisterEvents, '/<string:cnc_name>/meter-events'),
    # PRIME code: S12
    (ConcentratorParameters, '/<string:cnc_name>/cnc-parameters'),
    # PRIME code: S21
    (AdvancedInstantData, '/advanced-instant-data/<string:register_name>'),
    # PRIME code: S23
    (ContractDefinition, '/contract-definition/<string:register_name>'),
    (AllContractDefinition, '/<string:cnc_name>/contract-definition'),
    # PRIME code: S24
    (ConcentratorMeters, '/<string:cnc_name>/cnc-meters'),


    # Asynchronous requests
    # PRIME code: S02
    (DailyIncrementalAsync, '/daily-incremental/async/<string:register_name>'),
    (AllDailyIncrementalAsync, '/<string:cnc_name>/daily-incremental/async'),
    # PRIME code: S04
    (MonthlyBillingAsync, '/monthly-billing/async/<string:register_name>'),
    (AllMonthlyBillingAsync, '/<string:cnc_name>/monthly-billing/async'),
    # PRIME code: S05
    (DailyAbsoluteAsync, '/daily-absolute/async/<string:register_name>'),
    (AllDailyAbsoluteAsync, '/<string:cnc_name>/daily-absolute/async'),
    # PRIME code: S06
    (RegisterParametersAsync, '/meter-parameters/async/<string:register_name>'),
    (AllRegisterParametersAsync, '/<string:cnc_name>/meter-parameters/async'),
    # PRIME code: S09
    (RegisterEventsAsync, '/meter-events/async/<string:register_name>'),
    (AllRegisterEventsAsync, '/<string:cnc_name>/meter-events/async'),
    # PRIME code: S12
    (ConcentratorParametersAsync, '/<string:cnc_name>/cnc-parameters/async'),
    # PRIME code: S14
    (DailyAverageVoltageAndCurrentAsync, '/voltage-current-profile/async/<string:register_name>'),
    (AllDailyAverageVoltageAndCurrentAsync, '/<string:cnc_name>/voltage-current-profile/async'),
    # PRIME code: S18
    (CutoffsStatusAsync, '/cutoffs-status/async/<string:register_name>'),
    (AllCutoffsStatusAsync, '/<string:cnc_name>/cutoffs-status/async'),
    # PRIME code: S23
    (ContractDefinitionAsync, '/contract-definition/async/<string:register_name>'),
    (AllContractDefinitionAsync, '/<string:cnc_name>/contract-definition/async'),
    # PRIME code: S24
    (ConcentratorMetersAsync, '/<string:cnc_name>/cnc-meters/async'),

    # Send Orders
    # PRIME code: B03
    (CutoffReconnection, '/<string:cnc_name>/cutoff-reconnect/async'),

    # PRIME code: B11
    (OrderRequest, '/<string:cnc_name>/order-request/<string:txx>/async'),

    # DLMS Contracts
    (DLMStemplates, '/dlms_templates'),
    (DLMStemplatesByType, '/dlms_templates/types/<string:template_type>'),
    (ChangeDLMScontracts, '/<string:cnc_name>/dlms_templates/<string:dlms_template>'),
    (ChangeDLMScurrentpowers, '/<string:cnc_name>/currentpowers'),
    (ChangeDLMSlatentpowers, '/<string:cnc_name>/latentpowers'),
    (GetDLMSTrafoRatio, '/<string:cnc_name>/get-traforatio'),

    (UploadZIVCycle, '/<string:cnc_name>/ziv_cycle'),
    (TestRESTAPI, '/test_connection'),
]
