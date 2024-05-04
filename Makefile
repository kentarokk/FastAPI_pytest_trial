in:
	docker container exec -it api_fastapi bash

.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
up:
	docker-compose -f docker-compose.yml up

.PHONY: down
down:
	docker-compose -f docker-compose.yml down

.PHONY: migrate
migrate:
	docker-compose run \
		-e DATABASE_URL="postgresql://user:password@postgres:5432/narekuro-db" \
		api alembic upgrade head

.PHONY: migrate/base
migrate/base:
	docker-compose run \
		-e DATABASE_URL="postgresql://user:password@postgres:5432/narekuro-db" \
		api alembic downgrade base

.PHONY: seed
seed:
	DATABASE_URL="postgresql://user:password@localhost:5432/narekuro-db" \
	NEO4J_BOLT_URI=bolt://localhost:7687 \
	poetry run python seeds/seed.py

.PHONY: test
test:
	poetry run pytest -v

.PHONY: benchmark
benchmark:
	poetry run pytest tests --benchmark-only

.PHONEY: benchmark-profile
benchmark-profile:
	# https://www.graphviz.org/ が必要
	poetry run pytest tests -v --benchmark-only --benchmark-verbose --profile-svg

.PHONY: fmt
fmt:
	 poetry run black .

.PHONY: db-access
db-access:
	docker-compose exec postgres psql -U user -d narekuro-db
