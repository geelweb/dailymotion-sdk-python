#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

import httplib2
import urllib
import json

class Request():
    url = None

    def __init__(self, url):
        self.url = url

    def get(self, data=None):
        params = ""
        url = self.url

        if data is not None and len(data):
            params = urllib.urlencode(data)
            url = "%s?%s" % (self.url, params)

        h = httplib2.Http()
        resp, content = h.request(url, method="GET")
        if resp.status == 200:
            return json.loads(content)

        return None
