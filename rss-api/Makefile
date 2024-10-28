POETRY ?= $(shell which poetry || echo poetry)
RUN ?= $(POETRY) run

.PHONY: start start-config start-app install

start:
	@echo "Please use 'make start-config' or 'make start-app' to run the config based example or the application based example."

start-config: install
	$(RUN) harp server --enable rules --file config/common.yml --file config/rules.yml

start-app: install
	$(RUN) harp server --enable rss_api --file config/custom_app.yml

install:
	$(POETRY) install

