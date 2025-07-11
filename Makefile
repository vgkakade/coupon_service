init:
	./manage.py makemigrations
	./manage.py migrate
	./manage.py collectstatic --noinput
	./manage.py superuserexists || ./manage.py createsuperuser
serve:
	python manage.py runserver 8001
