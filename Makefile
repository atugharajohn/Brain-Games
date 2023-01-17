install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games

brain_even:
	poetry run brain-even

.PHONY: install brain-games build publish package-install lint brain-even