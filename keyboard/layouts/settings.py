import json


class Settings(object):
    _settings_file = open("../settings.js", "w+")
    _settings = json.load(_settings_file.read())
    lang = _settings["text"]
