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

deploy: ## Build site and deploy to gh-pages branch
	@echo "Building site..."
	$(ZOLA) build
	@echo "Deploying to gh-pages..."
	@# Stash current branch
	$(GIT) stash push -m "Deploy stash" || true
	@# Switch to gh-pages branch
	$(GIT) checkout gh-pages
	@# Remove old files (keep .git)
	find . -mindepth 1 -maxdepth 1 ! -name '.git' ! -name '.gitignore' -exec rm -rf {} +
	@# Copy new files
	cp -r public/* .
	@# Commit and push
	$(GIT) add .
	$(GIT) commit -m "Deploy site - $$(date)"
	$(GIT) push origin gh-pages
	@# Switch back to master
	$(GIT) checkout master
	@# Restore any stashed changes
	$(GIT) stash pop 2>/dev/null || true
	@echo "Deployment complete!"
