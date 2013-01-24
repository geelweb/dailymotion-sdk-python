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

    def get_params(self, fields=None):
        data = {}
        if fields is not None:
            data['fields'] = ",".join(fields)

        if self.localization is not None:
            data['localization'] = self.localization

        if self.family_filter is not None:
            data['family_filter'] = self.family_filter

        return data or None

    def get(self, item, item_id, fields=None):
        url = "/".join([self.api_url, item, item_id])
        request = geelweb.dailymotion.request.Request(url)
        return request.get(self.get_params(fields))

    def get_connection(self, item, item_id, connection, fields=None):
        url = "/".join([self.api_url, item, item_id, connection])
        request = geelweb.dailymotion.request.Request(url)
        return request.get(self.get_params(fields))

    def get_contest(self, contest, fields):
        return self.get('contest', contest, fields)

    def get_contest_connection(self, contest, connection, fields=None):
        return self.get_connection('contest', contest, connection, fields)

    def get_subtitle(self, subtitle, fields=None):
        return self.get('subtitle', subtitle, fields)

    def get_group(self, group, fields=None):
        return self.get('group', group, fields)

    def get_group_connection(self, group, connection, fields=None):
        return self.get_connection('group', group, connection, fields)

    def get_activity(self, activity, fields=None):
        return self.get('activity', activity, fields)

    def get_channel(self, channel, fields=None):
        return self.get('channel', channel, fields)

    def get_channel_connection(self, channel, connection, fields=None):
        return self.get_connection('channel', channel, connection, fields)

    def get_user(self, username, fields=None):
        return self.get('user', username, fields)

    def get_user_connection(self, username, connection, fields=None):
        return self.get_connection('user', username, connection, fields)

    def get_playlist(self, playlist, fields=None):
        return self.get('playlist', playlist, fields)

    def get_playlist_connection(self, playlist, connection, fields=None):
        return self.get_connection('playlist', playlist, connection, fields)

    def get_comment(self, comment, fields=None):
        return self.get('comment', comment, fields)

    def get_video(self, video, fields=None):
        return self.get('video', video, fields)

    def get_video_conection(self, video, connection, fields=None):
        return self.get('video', video, connection, fields)

