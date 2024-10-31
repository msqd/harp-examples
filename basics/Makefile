POETRY ?= $(shell which poetry || echo poetry)
RUN ?= $(POETRY) run

.PHONY: start install test


start: install
	$(RUN) harp server --example proxy:httpbin


test: install
	$(RUN) pytest


install:
	$(POETRY) install

