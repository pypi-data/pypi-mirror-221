include Makehelp.mk

SHELL := /bin/bash
ACTIVATE_VENV := true


## Create Python virtual environment
venv:
	$(eval ACTIVATE_VENV := . .venv/bin/activate)
	[ -d .venv ] || ( python3 -m venv .venv \
		&& $(ACTIVATE_VENV) \
		&& pip3 install --upgrade pip~=23.2.1 )


## Install Python dependencies
requirements:
	( $(ACTIVATE_VENV) \
		&& pip3 install -r requirements.txt \
		&& pip3 install -r requirements-test.txt )


## Run Black formatter
fmt:
	( $(ACTIVATE_VENV) && black . )


## Run Black formatter check
check-fmt:
	( $(ACTIVATE_VENV) && black --check . )
.PHONY: check-fmt


## Check Python lint
check-lint:
	( $(ACTIVATE_VENV) && pylint snowcross )
.PHONY: check-lint


## Check static types
check-type:
	( $(ACTIVATE_VENV) && mypy snowcross )
.PHONY: check-type


## Run all checks
check: check-fmt check-lint check-type
.PHONY: check


## Build
build: clean
	( $(ACTIVATE_VENV) && SETUPTOOLS_SCM_PRETEND_VERSION=0.0.2 python3 setup.py sdist bdist_wheel )


## Clean
clean:
	rm -rf build dist


## Install local development version
dev-install: build
	( $(ACTIVATE_VENV) && pip3 uninstall -y snowcross && pip3 install dist/snowcross-*-py3-none-any.whl )
.PHONY: dev-install


## Test
test:
	( $(ACTIVATE_VENV) && python3 -m pytest tests/ )
.PHONY: test


publish: build
	( $(ACTIVATE_VENV) && twine check dist/* && twine upload dist/* )
.PHONY: publish
