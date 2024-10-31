POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server --enable aggregator --file config.yml

install:
	$(POETRY) install

