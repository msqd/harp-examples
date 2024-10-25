POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server --example proxy:httpbin --file config.yml

install:
	$(POETRY) install

