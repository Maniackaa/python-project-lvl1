install:
		poetry install

brain-games:
		poetry run brain-games

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

package-uninstall:
		pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl

reinstall:
		poetry build
		pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl
		python3 -m pip install --user dist/*.whl

lint:
		poetry run flake8 brain_games

say-hello:
		echo 'Hello, World!'

upload:
		git add .
		git commit -m 'test'
		git push
