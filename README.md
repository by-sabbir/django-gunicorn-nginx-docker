# Dockerize Django along with Nginx and PostgreSQL

Docker will make your life a bit easier when it comes to deployment and CI/CD. This method can be used to deploy most stacks with Nginx and Postgres, ie. Flask, django-rest, FastAPI, NodeJS...

## Installation

Your system must have [docker-compose](https://docs.docker.com/compose/install/) to follow along.

```bash
docker-compose build
docker-compose up
```
You would be able to access

[localhost:8008](http://localhost:8008/)

## Usage
stop the container
```bash
docker-compose down
```
drop to django shell
```bash
docker-compose exec web python manage.py shell
```
more at [here](https://docs.docker.com/get-started/overview/)
## Contributing
You can do whatever you want with this repo.
