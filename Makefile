python3 = python3
django = $(python3) ./manage.py

admin:
	$(django) createsuperuser

app $(app_name):
	mkdir ./apps/$(app_name)
	$(django) startapp $(app_name) ./apps/$(app_name)

migrate $(app_name):
	$(django) makemigrations $(app_name)
	$(django) migrate

freeze:
	$(pythhon3) -m pip freeze > ./requirements.txt
