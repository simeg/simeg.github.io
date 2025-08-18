# Declare phony targets (targets that don't create files)
.PHONY: update-state check dry-run install run lint test coverage watch

# Shorthand for running commands with poetry
POETRY_RUN=poetry run

# CI pipeline: run checks and generate coverage report
ci: check coverage

# Install project dependencies using Poetry
install:
	poetry install

# Update the stored state file with current Everdrive firmware versions
update-state:
	$(POETRY_RUN) python -m everdrive_version_notifier.update_state

# Check for new Everdrive firmware versions and send notifications
check:
	$(POETRY_RUN) everdrive-check

# Perform a dry run check without sending actual notifications
dry-run:
	DRY_RUN=true $(POETRY_RUN) everdrive-check

# Run the main check process (alias for check target)
run: check

# Format code using Black formatter
lint:
	$(POETRY_RUN) black src tests

# Run tests after linting
test: lint
	$(POETRY_RUN) pytest

# Run tests with coverage reporting (terminal and XML output)
coverage:
	$(POETRY_RUN) pytest --cov=everdrive_version_notifier --cov-report=term-missing --cov-report=xml

# Run tests in watch mode (re-run tests when files change)
watch:
	$(POETRY_RUN) ptw --now
