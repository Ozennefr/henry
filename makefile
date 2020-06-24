format:
	@black .

lint:
	@flakehell app

test:
	@pytest

start:
	@cd src && uvicorn main:app --reload --host 0.0.0.0 > /henry/logs/app.log 2>&1

build_dev:
	@docker build --target dev -t henry_dev .

build_release:
	@docker build -t henry_release .
