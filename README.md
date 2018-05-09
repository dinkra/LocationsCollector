# Preparation steps (will be split between docker and ansible):
Setup machine:
- Install nginx - execute `brew install nginx`.
- Install PostgreSQL (reference - https://www.postgresql.org/download/macosx/).
- Install `pyenv` (reference - https://github.com/pyenv/pyenv#installation).

Setup project:
- Setup postgres database (reference - https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/). Check project settings for reference.
- Execute `pyenv local` in order to switch to a proper python version.
- Execute `make install_versioned_deps` in order to create a virtual environment.
- Execute `. venv/bin/activate` in order to activate virtual environment.
- Execute `./manage.py migrate` in order to migrate database.

Start project:
- Execute `gunicorn -c gunicorn.conf.py wsgi` in order to launch gunicorn.


# TODO:
- [x] Setup models.
- [x] Implement a POST call.
- [x] Implement throttling.
- [x] Add logging to console.
- [x] Add unit tests.
- [x] Setup docker images.
- [ ] Setup ansible, encrypted variables, use variables in docker files.
- [ ] Setup SSL for nginx.
- [ ] Add documentation.