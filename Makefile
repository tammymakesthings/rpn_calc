##############################################################################
# Makefile for Python projects
##############################################################################

PYTEST ?= $(shell which pytest)
POETRY ?= $(shell which poetry)
PYTHON ?= $(shell which python)

PROJECT_ROOT   := $(PWD)

PYTHON_SRC     := $(shell find $(PROJECT_ROOT)/src -name '*.py' -print)
PYTHON_TESTS   := $(shell find $(PROJECT_ROOT)/tests -name '*.py' -print)
DOC_FILES      := $(shell find $(PROJECT_ROOT)/docs -type f -print)
ROOT_DOC_FILES := $(PROJECT_ROOT)/LICENSE \
	$(wildcard $(PROJECT_ROOT)/*.rst) \
	$(wildcard $(PROJECT_ROOT)/*.md)
POETRY_FILE   := $(PROJECT_ROOT)/pyproject.toml

all: test

build: $(PROJECT_ROOT)/.build.timestamp

test: $(PYTHON_SRC) $(PYTHON_TESTS) poetry.lock
	$(POETRY) run pytest $(PROJECT_ROOT)/tests

$(PROJECT_ROOT)/.build.timestamp: $(PYTHON_SRC) $(PYTHON_TESTS) $(DOC_FILES) $(ROOT_DOC_FILES) poetry.lock
	$(POETRY) build
	touch $(PROJECT_ROOT)/.build.timestamp

release: $(PROJECT_ROOT)/.build.timestamp
	$(POETRY) publish

clean:
	rm -f dist/*.whl dist/*.tar.gz

.PHONY: all build
