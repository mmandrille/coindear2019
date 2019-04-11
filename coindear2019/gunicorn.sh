#!/bin/bash
cd /opt/coindear2019
source venv/bin/activate
cd /opt/coindear2019/coindear2019
gunicorn coindear2019.wsgi -t 600 -b 127.0.0.1:8008 -w 6 --user=servidor --group=servidor --log-file=/opt/coindear2019/gunicorn.log 2>>/opt/coindear2019/gunicorn.log
