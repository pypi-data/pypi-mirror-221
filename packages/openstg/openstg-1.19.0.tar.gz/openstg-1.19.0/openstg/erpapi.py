# -*- coding: utf-8 -*-
import requests
from urlparse import urlparse
import json

class ErpApiException(Exception):
    pass

class ErpApi(object):
    token = None
    base_endpoint = None

    def connect(self, url, token=None):
        parsed_url = urlparse(url)

        self.base_endpoint = '{}://{}:{}{}'.format(
            parsed_url.scheme, parsed_url.hostname, parsed_url.port, parsed_url.path
        )

        if token is None:
            # print('Connect by usr/pwd')
            user = parsed_url.username
            password = parsed_url.password


            token_url = '{}token'.format(self.base_endpoint)

            session = requests.Session()
            session.auth = (user, password)

            r = session.get(token_url)

            if r.status_code == 200:
                data = r.json()
                self.token = data['token']
            else:
                raise(ErpApiException("Error connecting: [{}] {}".format(r.status_code, r.content)))
        else:
            # print('Connect by token')
            self.token = token

    def test(self):
        # test connection with ResCompany get
        res = {}
        try:
            res = self.filter('IrModel', filter=[], fields=['name'], limit=1)
        except Exception as e:
            pass

        return len(res.get('items', [])) and True or False

    def __str__(self):
        test = self.test()
        if self.base_endpoint is not None and self.token is not None:
            if test:
                return 'Connected REST ERP API in {}'.format(self.base_endpoint)
            else:
                return 'Not Connected. BAD CREDENTIALS'
        else:
            return 'Not Connected'

    def create_uri(self, object, res_id=None, filter=None, fields=None, limit=None, offset=None):
        '''
        Creates a URI using parameters
        :param object: Camel case object name (i.e. 'ResUser')
        :param oid: resurce id if desired
        :param filter: ERP domain
        :param fields: list of fields to download in .dot notation (i.e user_id.name)
        :param limit: Number of registers to get (0 -> all)
        :param offset: first register offset
        :return:
        '''
        first_param = True
        uri = '{}{}'.format(self.base_endpoint, object)
        if res_id:
            uri += '/{}'.format(res_id)
        if fields:
            schema = ','.join(fields)
            uri += '{}schema={}'.format(first_param and '?' or '&', schema)
            first_param = False
        if filter:
            if isinstance(filter, (list, tuple)):
                 filter = json.dumps(filter)
            uri += '{}filter={}'.format(first_param and '?' or '&', filter)
            first_param = False
        if limit:
            uri += '{}limit={}'.format(first_param and '?' or '&', limit)
            first_param = False
        if offset:
            uri += '{}offset={}'.format(first_param and '?' or '&', offset)
            first_param = False

        return uri

    def read(self, object, res_id, fields=None):
        '''
        Read model data
        :param object: Camel case object name (i.e. 'ResUser')
        :param id: resurce id
        :param fields: list of fields to download in .dot notation (i.e user_id.name)
        :return: dictionary with field and value
        '''
        headers = {'Authorization': 'token {}'.format(self.token)}

        uri = self.create_uri(object, res_id, fields=fields)
        r = requests.get(uri, headers=headers)

        return r.json()

    def filter(self, object, filter=None, fields=None, limit=None):
        '''
        Search for resurces of a model using a ERP domain (filter)
        :param object: Camel case object name (i.e. 'ResUser')
        :param id: filter ERP style domain
        :param fields: list of fields to download in .dot notation (i.e user_id.name)
        :return: list of dictionary with field and values
        '''
        headers = {'Authorization': 'token {}'.format(self.token)}

        uri = self.create_uri(object, fields=fields, filter=filter, limit=limit)
        r = requests.get(uri, headers=headers)

        return r.json()


