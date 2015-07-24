release:
	python setup.py register sdist bdist_wheel upload

test:
	@python -Wmodule -m coverage run tests/run.py
	@coverage report --fail-under 100
	@flake8 .
