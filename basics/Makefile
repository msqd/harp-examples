POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server --example proxy:httpbin

install:
	$(POETRY) install --no-root

