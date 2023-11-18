# Banking Fake Server

Fake Server that simulates (BNI OPG, BNI RDL, BNI VA and OY) like a production where all this part are connected together

## Code style
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## Tech Used
<b>Built with</b>
- [AIOHTTP](https://docs.aiohttp.org/en/stable/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisite

* Python 3 +
* PIP 
* Docker
* Docker Compose


### Running Locally

```bash
git clone this repository
pip install -r requirements.txt
make run or python -m aiohttp.web -H 0.0.0.0  -P 7000 app:init_app
```

### Running via Docker Compose

to run just execute but make sure you choose and provide right env settings:
```bash
docker-compose up -d --build
```

### Run Unittest + Coverage
This app uses pytest so to run unittest and coverage you can just
```
pytest tests/....
```

### Makefile
All commands that can be executed on the apps it's registered in Makefile
please checkout the makefile to know more.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 
version 1.0

## Authors

* ** Kelvin ** - (https://github.com/vousmeevoyez)
