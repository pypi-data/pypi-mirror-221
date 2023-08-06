# coding: utf-8
from flask import Flask, request
from flask_restplus import Api, Resource
import xml.dom.minidom as xmlmd
import time
import os


dc_status = {
        '0': "SUCCESS: The request with ID {} for the concentrator {} have "
             "finished successfully. {}",
        '1': "WORKING: The request with ID {} for the concentrator {} is "
             "still in progress. {}",
        '2': "ERROR: The request with ID {} for the concentrator {} has "
             "been cancelled due to a timeout on the DC-Meter connection. "
             "{}",
        '3': "ERROR: The request with ID {} for the concentrator {} has "
             "been rejected for being outdated. {}",
        '4': "ERROR: The request with ID {} for the concentrator {} has "
             "been partially applied (success in some meters, failure in "
             "others). {}",
        '5': "ERROR: The request with ID {} for the concentrator {} is "
             "not properly formed."
             " Unable to process it. {}",
        '6': "ERROR: The request with ID {} for the concentrator {} has "
             "been cancelled due to a timeout on the DC-STG connection. "
             "{}",
        '7': "ERROR: The request with ID {} for the concentrator {} has "
             "asked information from a meter which does not exist in the"
             "DC database. {}",
        '8': "ERROR: The request with ID {} for the concentrator {} has an "
             "incompatibility with the protocol version. {}"
    }

meter_status = {
        '0': "SUCCESS: The meter {} have finished serving the request "
             "with ID {} successfully.",
        '1': "ERROR: The meter {} couldn't finish serving the request "
             "with ID {}.",
        '2': "WARNING: The meter {} have finished serving the request with "
             "ID {}. But any report after it is missing",
        '3': "ERROR: The meter {} couldn't finish serving the request with "
             "ID {}. Order partially applied (part of the data sent in the "
             "order were not correctly applied in the meter)."
    }


class Stg(Api):
    def _register_doc(self, app_or_blueprint):
        #We have to
        pass


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


class WSStgResource(Resource):

    def post(self):
        f_name = '/tmp/post-{}'.format(time.time())
        if isinstance(request.data, bytes):
            # Python3 backwards compatibility
            request.data = request.data.decode()
        with open(f_name, 'w') as f:
            f.write(request.data)
        out_msg = manage_request()
        os.remove(f_name)
        print(out_msg)
        return "Ok", 200


def manage_request_status(info):
    if 'Reference' not in info:
        info['Reference'] = ''
    default = "ERROR: The request with ID {} for the concentrator {}. has " \
              "suffered an UNKNOWN error {}".format(info['IdPet'],
                                                    info['IdDC'],
                                                    info['Reference'])
    return dc_status.get(info['ReqStatus'], default).format(
        info['IdPet'], info['IdDC'], info['Reference'])


def manage_meter_status(info):
    default = "ERROR: The meter {} suffered and UNKNOWN error processing the " \
              "request with ID {}.".format(info['IdPet'], info['IdDC'])
    return meter_status.get(info['MeterStatus'], default).format(
        info['IdMeters'], info['IdPet'])


def manage_request():
    dom = xmlmd.parseString(request.data.replace('ns1:', ''))
    if 'UpdateMetersStatus' in request.data:
        return manage_meter_status(create_dict(dom, 'UpdateMetersStatus'))
    else:
        if 'UpdateRequestStatus' in request.data:
            return manage_request_status(
                create_dict(dom, 'UpdateRequestStatus'))
        else:  # Report message
            return manager_report_status(create_dict(dom, 'Report'))


def create_dict(dom, item):
    res = {}
    for elem in dom.getElementsByTagName(item):
        for x in elem.childNodes:
            if x.nodeType == xmlmd.Node.ELEMENT_NODE:
                if x.firstChild is None:
                    pass
                else:
                    res[x.tagName] = x.childNodes[0].data
    return res


def manager_report_status(info):
    if 'Reference' not in info:
        info['Reference'] = ''
    default = 'A report has been received but we don\'t handle its type yet'
    return 'A report has been received. With status: {}'.format(
        dc_status.get(info['ReqStatus'], default).format(info['IdPet'],
                                                         info['IdDC'],
                                                         info['Reference']))

    # TODO: Connect to ERP to read the S15 report received


resources = [
    (WSStgResource, '/ws')
]
