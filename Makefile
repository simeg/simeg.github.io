.PHONY: serve build check clean init-theme update-theme deploy

ZOLA = $(shell which zola)
GIT = $(shell which git)

serve: ## Start development server with live reload
	$(ZOLA) serve

build: ## Generate static site for production
	$(ZOLA) build

check: ## Validate content and check internal links
	$(ZOLA) check

clean: ## Remove generated public directory
	rm -rf public/

init-theme: ## Initialize the archie-zola theme submodule for first time setup
	$(GIT) submodule update --init --recursive

update-theme: ## Update the archie-zola theme submodule
	$(GIT) submodule update --remote themes/archie-zola

