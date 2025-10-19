.PHONY: build up down logs migrate test fresh-start

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f web

migrate:
	docker-compose exec web python manage.py migrate

test:
	docker-compose run --rm test

fresh-start:
	docker-compose down -v
	make build
	make up
	@ping -n 11 localhost > nul
	make migrate

superuser:
	docker-compose exec web python manage.py createsuperuser