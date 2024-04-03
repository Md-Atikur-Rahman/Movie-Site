## About Me

- Name : `Md Atikur Rahman`
- Email : `md.atik.dev@gmail.com`

## Getting started

### To start project, run:

- `docker-compose up --build`

The API will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Celery

- Note: Here For each command open a new terminal and run each server
- `docker-compose run app sh -c "celery -A core worker -l INFO"`
- `docker-compose run app sh -c "celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"`

### Load Initial Data

- `docker-compose run --rm app sh -c "python manage.py load_initial_auth_db"`
- `docker-compose run --rm app sh -c "python manage.py load_initial_movie_db"`

one of initial user:
email: john_doe@gmail.com
password: pass1

Now visit [http://127.0.0.1:8000](http://127.0.0.1:8000).