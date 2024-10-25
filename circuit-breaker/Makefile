POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server -f config.yml

install:
	$(POETRY) install --no-root

