clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

run:
	python -m aiohttp.web -H 0.0.0.0  -P 7000 app:init_app

run-gunicorn:
	gunicorn app:init_app --bind 0.0.0.0:7000 --worker-class aiohttp.GunicornWebWorker
