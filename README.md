# Trade Hub

## Build

### Virtual Environment

```console
mkdir tradehub && cd tradehub
uv init --python 3.12
```

### Start a Django Project

```console
uv add Django
source .venv/bin/activate

uv run django-admin startproject tradehub .
uv run python manage.py makemigrations
uv run python manage.py startapp shop
uv run python manage.py createsuperuser

uv run python manage.py runserver
```
