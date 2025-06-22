.PHONY: update-state check dry-run install run lint test coverage watch

POETRY_RUN=poetry run

ci: check coverage

install:
	poetry install

update-state:
	$(POETRY_RUN) python -m everdrive_version_notifier.update_state

check:
	$(POETRY_RUN) everdrive-check

dry-run:
	DRY_RUN=true $(POETRY_RUN) everdrive-check

run: check

lint:
	$(POETRY_RUN) black src tests

test: lint
	$(POETRY_RUN) pytest

coverage:
	$(POETRY_RUN) pytest --cov=everdrive_version_notifier --cov-report=term-missing --cov-report=xml

watch:
	$(POETRY_RUN) ptw --now
