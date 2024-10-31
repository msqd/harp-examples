POETRY ?= $(shell which poetry || echo poetry)
RUN ?= $(POETRY) run

.PHONY: start install test


start: install
	$(RUN) harp server --example proxy:httpbin

install:
	$(POETRY) install

test:
	$(RUN) pytest
