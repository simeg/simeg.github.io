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
	@# Clean up any existing worktree
	$(GIT) worktree remove public-deploy 2>/dev/null || true
	@# Create fresh worktree
	$(GIT) worktree add public-deploy gh-pages 2>/dev/null || $(GIT) worktree add --orphan public-deploy gh-pages
	@# Clear existing files and copy new ones
	rm -rf public-deploy/* public-deploy/.*[^.] 2>/dev/null || true
	cp -r public/* public-deploy/ 2>/dev/null || true
	@# Commit and push
	cd public-deploy && $(GIT) add . && $(GIT) commit -m "Deploy site - $$(date)" && $(GIT) push origin gh-pages
	@# Clean up
	$(GIT) worktree remove public-deploy 2>/dev/null || rm -rf public-deploy
	@echo "Deployment complete!"
