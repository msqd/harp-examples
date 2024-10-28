POETRY ?= $(shell which poetry || echo poetry)

.PHONY: start install


start: install
	$(POETRY) run harp server --enable rules --file config.yml & cd frontend && npm run dev

install:
	$(POETRY) install
	cd frontend && npm install 

