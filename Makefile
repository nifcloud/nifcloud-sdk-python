path=./
test: lint py-test
lint:
	XDG_CONFIG_HOME=./ pipenv run flake8 $$(find $(path) -type f -name "*.py" -print)
py-test:
	PYTHONPATH=./ pipenv run py.test --capture=sys $(path)
isort:
	pipenv run isort -rc $$(find $(path) -type d -name ".git" -prune -o -type f -name "*.py" -print)
