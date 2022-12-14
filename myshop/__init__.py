import sys
import collections
from .celery import app as celery_app
import collections

try:
    from collections import abc
    collections.MutableMapping = abc.MutableMapping
except:
    pass
