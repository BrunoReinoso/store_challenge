
# Store Challenge

## Description 
This project is a challenge to evaluate new incomers to the Automation Team.

## Architecture
  - A web application using Python, Django Framework and Django Rest Framework.
  - A postgresql database.

## Development
This project was developed on Linux Ubuntu 21.04. See the Dockerfile apt-get install command to get the list of packages you will need to have installed for the requirements to be installed successfully.

Then, we recommend installing pyenv and pyenv-virtualenv, install python 3.8.0 on it and then create a pyenv virtualenv with this python version.

Alternatively, in case you need, there are also commands in the Makefile to build and run the containers for the app.


## Installation

Clone the project

```bash
  git clone https://github.com/BrunoReinoso/store-challenge
```

Go to the project directory

```bash
  cd core
```

Activate the virtualenv and install the dependencies:

```bash
  make requirements-pip
```

## Development Environment
### Database

#### Up the container with database

```bash
  make docker-compose-up
```

#### Creating tables

This command below will create all instructions to setup your database:

```bash
  make migrations
```

With instructions created, it's time to apply them (execute within database):

```bash
  make migrate
```

### Start the server

After this command below, you can already go to 127.0.0.1:8000 on your browser to see the application.

```bash
  make run-server
```

### Creating superuser

In order to access administrative module, you will need to create a super user. Execute the command below and follow instructions:

```bash
  make superuser
```
  
## Authors

- [@BrunoReinoso](https://github.com/BrunoReinoso/)

## Helpers

- [@AdailtonNascimento](https://github.com/dhelbegor)
- [@DaltonInoue](https://github.com/inotlad)
- [@RockyShimithy](https://github.com/rockyshimithy)
- [@TiagoParanhos](https://github.com/tiagoprn)
