install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

package-install:
	python3 -m pip install --user dist/*.whl