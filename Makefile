install:
		poetry install

brain-games:
		poetry run brain-games

brain-games:
		poetry run brain-even

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

make lint:
		poetry run flake8 brain_games

say-hello:
		echo 'Hello, World!'

upload:
		git add .
		git commit -m 'test'
		git push
