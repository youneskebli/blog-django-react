build:
	docker-compose up --build -d

up:
	docker-compose up -d

ssh:
	docker exec -it blogapp bash

server:
	docker exec -it blogapp python manage.py runserver 0.0.0.0:8000

down:
	docker-compose down

flake8:
	docker exec -it blogapp flake8 /usr/src/app

test:
	docker exec -it blogapp python manage.py test