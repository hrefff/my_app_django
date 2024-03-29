# My App Django

Django project for demo upload multiple images.

## Installation

0. clone repo
```bash
git clone git@github.com:hrefff/my_app_django.git
cd my_app_django
```

1. Install pyenv (if not installed)
```bash
curl https://pyenv.run | bash
```

2. Install needed python version (3.12)
```bash
pyenv install 3.12
pyenv local 3.12
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run server
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
