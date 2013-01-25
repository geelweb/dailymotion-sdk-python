#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

import geelweb.dailymotion.request

class DailymotionService():
    api_url = "https://api.dailymotion.com"

    localization = None
    family_filter = None

    def __init__(self, localization=None, family_filter=None):
        self.localization = localization
        self.family_filter = family_filter

    def get_params(self, fields=None, page=None, limit=None):
        data = {}
        if fields is not None:
            data['fields'] = ",".join(fields)

        if self.localization is not None:
            data['localization'] = self.localization

        if self.family_filter is not None:
            data['family_filter'] = self.family_filter

        if page is not None:
            data['page'] = page

        if limit is not None:
            data['limit'] = limit

        return data or None

    def get(self, item, item_id, fields=None, page=None, limit=None):
        url = "/".join([self.api_url, item, item_id])
        request = geelweb.dailymotion.request.Request(url)
        return request.get(self.get_params(fields, page, limit))

    def get_connection(self, item, item_id, connection, fields=None, page=None, limit=None):
        url = "/".join([self.api_url, item, item_id, connection])
        request = geelweb.dailymotion.request.Request(url)
        return request.get(self.get_params(fields, page, limit))

    def get_contest(self, contest, fields=None, page=None, limit=None):
        return self.get('contest', contest, fields, page, limit)

    def get_contest_connection(self, contest, connection, fields=None, page=None, limit=None):
        return self.get_connection('contest', contest, connection, fields, page, limit)

    def get_subtitle(self, subtitle, fields=None, page=None, limit=None):
        return self.get('subtitle', subtitle, fields, page, limit)

    def get_group(self, group, fields=None, page=None, limit=None):
        return self.get('group', group, fields, page, limit)

    def get_group_connection(self, group, connection, fields=None, page=None, limit=None):
        return self.get_connection('group', group, connection, fields, page, limit)

    def get_activity(self, activity, fields=None, page=None, limit=None):
        return self.get('activity', activity, fields, page, limit)

    def get_channel(self, channel, fields=None, page=None, limit=None):
        return self.get('channel', channel, fields, page, limit)

    def get_channel_connection(self, channel, connection, fields=None, page=None, limit=None):
        return self.get_connection('channel', channel, connection, fields, page, limit)

    def get_user(self, username, fields=None, page=None, limit=None):
        return self.get('user', username, fields, page, limit)

    def get_user_connection(self, username, connection, fields=None, page=None, limit=None):
        return self.get_connection('user', username, connection, fields, page, limit)

    def get_playlist(self, playlist, fields=None, page=None, limit=None):
        return self.get('playlist', playlist, fields, page, limit)

    def get_playlist_connection(self, playlist, connection, fields=None, page=None, limit=None):
        return self.get_connection('playlist', playlist, connection, fields, page, limit)

    def get_comment(self, comment, fields=None, page=None, limit=None):
        return self.get('comment', comment, fields, page, limit)

    def get_video(self, video, fields=None, page=None, limit=None):
        return self.get('video', video, fields, page, limit)

    def get_video_conection(self, video, connection, fields=None, page=None, limit=None):
        return self.get('video', video, connection, fields, page, limit)

