.PHONY: help

MANAGE = python manage.py
USER_ID = $(shell id -u)
GROUP_ID = $(shell id -g)
SHARED_FOLDER=/tmp/shared-docker-$(shell date +%Y%m%d_%H%M%S)
VERSION=1.0.0

help:  ## This help 
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Clean python bytecodes, optimized files, logs, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@echo 'Temporary files deleted'

shell: clean  ## Run a django shell
	@$(MANAGE) shell_plus

requirements-pip:  ## Install the APP requirements
	@pip install --upgrade pip
	@pip install -r requirements/base.txt
	@pip install -r requirements/development.txt

run-server: clean migrate  ## Run the server
	@$(MANAGE) runserver

migrations:  ## Create migrations
	@$(MANAGE) makemigrations $(app)

migrate: ##  Execute the migrations
	@$(MANAGE) migrate $(app)

createsuperuser:  ## Create the django admin superuser
	@$(MANAGE) createsuperuser

docker-compose-up: clean  ## Raise docker-compose for development environment
	@docker-compose up -d

docker-compose-stop: clean  ## Stop docker-compose for development environment
	@docker-compose stop

docker-compose-rm: docker-compose-stop ## Delete the development environment containers
	@docker-compose rm -f

docker-build-image: ## Build application image
	@echo 'Building application image'
	@docker build -t teste:${VERSION}--pull --no-cache --build-arg UID=$(USER_ID) --build-arg GID=$(GROUP_ID) --build-arg APP_PORT=8080 --network host .

docker-run-local: clean  ## Run the docker application image locally
	@echo "You can exchange files with these containers on the directory $(SHARED_FOLDER) on the host and /shared on the container."
	@mkdir -p $(SHARED_FOLDER)
	@echo 'Starting app container...'
	@docker run --rm -d --env-file .env --network host --mount type=bind,source=$(SHARED_FOLDER),target=/shared --name 'teste' teste:${VERSION}'make run-server' &

show-urls: clean  ## Show all urls available on the app
	@$(MANAGE) show_urls

release-patch:  ## Update package release as patch
	@bump2version patch

release-minor:  ## Update package release as minor
	@bump2version minor

release-major:  ## Update package release as major
	@bump2version major

lint: clean  ## Run pylint linter
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc  --django-settings-module=teste.settings teste/* loja/*
	@printf '\n FINISHED! \n --- \n'

style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 --tc .
	@black -S -t py37 -l 79 teste/. loja/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'