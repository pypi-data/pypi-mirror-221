# SPDX-FileCopyrightText: 2022 German Aerospace Center (DLR)
#
# SPDX-License-Identifier: MIT

PROGRAM_VERSION = $(lastword $(shell poetry version --no-ansi))
ALL_PYTHON_FILES = $(shell find src/exodusreader test doc -type f -name "*.py")


all: audit

clean:
	rm -rf build
	rm -rf dist
	poetry run coverage erase

prepare:
	mkdir -p build

test: prepare
	poetry run pytest --doctest-modules --junit-xml=build/tests.xml src/exodusreader/ test/

doctest: prepare
	poetry run pytest --doctest-modules --junit-xml=build/doctests.xml src/exodusreader/

formatting:
	poetry run black src/exodusreader test
	poetry run isort src/exodusreader test

license-metadata:
	poetry run reuse addheader --copyright="German Aerospace Center (DLR)" --license="MIT" $(ALL_PYTHON_FILES)
	poetry run black src/exodusreader test

check-formatting:
	poetry run black src/exodusreader test --check
	poetry run isort src/exodusreader test --check-only

check-license-metadata:
	poetry run reuse lint

check-code: prepare
	poetry run flake8 src/exodusreader test --exit-zero --output-file=build/flake8.txt

check-coverage: prepare
	poetry run pytest --cov=src/exodusreader --cov-fail-under=50 --cov-report=term-missing --cov-report=html --cov-report=xml

check-security:
	poetry run bandit -r src/exodusreader/
	poetry run bandit -r -ll src/exodusreader/

audit: check-code check-coverage check-formatting check-license-metadata check-security

docs: prepare
	poetry run sphinx-apidoc src/exodusreader --force --output-dir=doc/
	poetry run sphinx-build -w build/sphinxwarn.txt -D version="$(PROGRAM_VERSION)" -D release="$(PROGRAM_VERSION)" -b html doc/ build/html/

doc: docs

package: prepare
	poetry build -f sdist
	poetry build -f wheel

.PHONY: list
list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
