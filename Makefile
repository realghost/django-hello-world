MANAGE=django-admin.py
APPLICATIONS=contacts requests

test:
	PYTHONPATH="./django" DJANGO_SETTINGS_MODULE=main.settings $(MANAGE) test $(APPLICATIONS)

run:
	PYTHONPATH="./django" DJANGO_SETTINGS_MODULE=main.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH="./django" DJANGO_SETTINGS_MODULE=main.settings $(MANAGE) syncdb --noinput
