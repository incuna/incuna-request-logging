release:
	python setup.py register sdist bdist_wheel upload

test-coverage:
	@python -Wmodule -m coverage run tests/run.py

coverage-report:
	@coverage report --fail-under 100

test:
	@$(MAKE) --no-print-directory test-coverage
	@$(MAKE) --no-print-directory coverage-report
	@flake8 .
