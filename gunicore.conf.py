import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing
bind = "0.0.0.0:8080"
backlog  = 512
chdir = '/home/eli/Desktop/src/python/elishop/public'
timeout = 60
worker_class = "gevent"
workers = multiprocessing.cpu_count()*2 + 1
threads = 2
max_requests = 5000

loglevel = "info"
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s "%(a)s"'

accesslog = "/home/eli/Desktop/src/python/elishop/runtime/access.log"
errorlog = "/home/eli/Desktop/src/python/elishop/runtime/error.log"


