.PHONY: update-state check dry-run install run lint test coverage watch

install:
	poetry install

update-state:
	poetry run python -m everdrive_version_notifier.update_state

check:
	poetry run everdrive-check

dry-run:
	DRY_RUN=true poetry run everdrive-check

run: check

lint:
	poetry run black src tests

test: lint
	poetry run pytest

coverage:
	poetry run pytest --cov=everdrive_version_notifier --cov-report=term-missing

watch:
	poetry run ptw --now
