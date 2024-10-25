POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server --enable rules --file config.yml

install:
	$(POETRY) install

