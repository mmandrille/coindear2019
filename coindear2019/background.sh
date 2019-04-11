#!/bin/bash
cd /opt/coindear2019
source venv/bin/activate
cd /opt/coindear2019/coindear2019
python manage.py process_tasks
