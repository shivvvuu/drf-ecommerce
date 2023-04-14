.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

.PHONY: test
test:
	poetry run pytest
	