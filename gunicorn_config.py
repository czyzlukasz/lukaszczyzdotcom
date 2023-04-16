wsgi_app = "lukaszczyzdotcom.wsgi:application"
loglevel = "info"
workers = 1
bind = "0.0.0.0:8000"
reload = False
accesslog = errorlog = "/tmp/dev.log"
capture_output = True