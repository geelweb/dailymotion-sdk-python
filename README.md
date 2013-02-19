# Dailymotion Python SDK

This repository contains a *unofficial* SDK that allows to access the
[Dailymotion API](http://www.dailymotion.com/doc/api/reference.html)

## Installation

    sudo python setup.py install

## Dependencies

 * httplib2 0.7.7
 * urllib
 * json

## Usage

    import geelweb.dailymotion.service
    service = geelweb.dailymotion.service.DailymotionService()

    user = service.get("user", "autoplus")

    videos = service.get_connection("user", "autoplus", "videos", fields=('id', 'url', 'title', 'description'))

    fans = service.get_connection("user", "autoplus", "fans")

Or you can use shorcuts methods

    import geelweb.dailymotion.service
    service = geelweb.dailymotion.service.DailymotionService()

    user = service.get_user("autoplus")

    videos = service.get_user_connection("autoplus", "videos")

    fans = service.get_user_connection("autoplus", "fans")

## TODO

 * Authentication
 * Error management
 * POST/DELETE methods (create a video, delete a video)
