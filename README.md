[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# SmallURL

## How to develop?

Start by cloning the repository.

```bash
git clone https://github.com/mateus-brito/smallurl
cd smallurl
touch .env
```

Set the values for environment variables:

```console
SECRET_KEY=THIS_IS_NOT_A_GOOD_SECRET
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,.localhost
```

### Docker-compose

```bash
docker-compose build
docker-compose up -d
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

### Deploy to production

Want to find out how to get a project like this into production? [Read here](https://github.com/Mateus-Brito/deploying/blob/main/contents/dokku/django.md)
