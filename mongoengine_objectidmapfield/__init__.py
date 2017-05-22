# -*- coding: utf-8 -*-
from .fields import ObjectIdMapField  # flake8: disable=F401

__author__ = 'Malthe Jørgensen'
__all__ = ('ObjectIdMapField')
VERSION = (0, 0, 1)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version


__version__ = get_version()
