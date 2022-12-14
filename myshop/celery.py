import os

from celery import Celery
import collections

try:
    from collections import abc
    collections.MutableMapping = abc.MutableMapping
except:
    pass
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
"""
brew unlink python
$ brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/e128fa1bce3377de32cbf11bd8e46f7334dfd7a6/Formula/python.rb
$ brew switch python 3.9

"""