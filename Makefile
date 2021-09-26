.PHONY: install add black black/check isort isort/check mypy lint lint/check test run

install:
	pip install -r requirements.txt

add:
	pip install "$(package)"
	pip freeze | grep "$(package)" >> requirements.txt
	sort -u -o requirements.txt requirements.txt

black:
	black ytsub

black/check:
	black --check --diff ytsub

isort:
	isort ytsub

isort/check:
	isort --check --diff ytsub

pylint:
	pylint ytsub

lint: isort black

lint/check: isort/check black/check pylint

mypy:
	mypy ytsub

test:
	APP_env=test pytest $(options)

run:
	python -m ytsub

db/reset:
	make db/reset_db database=dev-db
	make db/create_tables env=development

db/reset/test:
	make db/reset_db database=test-db
	make db/create_tables env=test

db/reset_db:
	docker-compose exec -T postgres psql postgres postgres -c 'DROP DATABASE IF EXISTS "$(database)"'
	docker-compose exec -T postgres psql postgres postgres -c 'CREATE DATABASE "$(database)"'

db/create_tables:
	APP_env=$(env) APP_database_echo=true python -m ytsub.cli create-tables
