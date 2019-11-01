#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 合并配置文件
from src.main.app.awesome_webapp.webapp import config_default

__author__ = "Mason.Wu"


class Dict(dict):
    """
    Simple dict but support access as x.y style
    """

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def to_dict(d):
    dd = Dict()
    for k, v in d.items():
        dd[k] = to_dict(v) if isinstance(v, dict) else v
    return dd


configs = config_default.configs

try:
    from src.main.app.awesome_webapp.webapp import config_override

    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = to_dict(configs)
