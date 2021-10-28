.PHONY: help

PROJECT_NAME = challenge
APP_NAME = store
MANAGE = cd $(PROJECT_NAME) && python manage.py
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
	@$(MANAGE) shell

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
	@pylint --rcfile=.pylintrc  --django-settings-module=core.settings $(PROJECT_NAME)/* --errors-only
	@printf '\n FINISHED! \n --- \n'

style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 --tc .
	@black -S -t py38 -l 79 $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

tests: ## Run tests 
	@printf '\n -- \n >>> Running tests...<<<\n'
	@cd $(PROJECT_NAME) && py.test $(APP_NAME) --ds=core.settings -s  -vvv
	@printf '\n FINISHED! \n --- \n'

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	@cd $(PROJECT_NAME) && py.test $(APP_NAME) -k $(test) --ds=core.settings -s  -vvv

docker-build-image: ## Build application image
	@echo 'Building application image'
	@docker build -t "$(PROJECT_NAME)" --pull --no-cache --build-arg UID="$(USER_ID)" --build-arg GID="$(GROUP_ID)" -f Dockerfile .

docker-run-local: clean  ## Run the docker application image locally
	@echo 'Starting app container...'
	@docker run --rm -d -p 8000:8000 --env-file .env --network host --name '$(PROJECT_NAME)' $(PROJECT_NAME):latest