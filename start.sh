#!/bin/bash
trap 'kill %1; kill %2' SIGINT
redis-server & celery -A ProteinFinder worker -l info & python manage.py runserver
