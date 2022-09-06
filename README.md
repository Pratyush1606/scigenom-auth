# scigenom-auth

This repo contains the microservice for authentication.

---

## **Technologies**

* [Django](https://www.djangoproject.com/): Django builds better web apps with less code
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Rest APIs with Django
* Database used: [SQLite](https://www.sqlite.org/index.html)

---

## **Local Setup**

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python [here](https://www.python.org/downloads/).

* Get the Source Code, either Clone the repository or use the zip file

  * Using HTTPS

    ```sh
    git clone https://github.com/Pratyush1606/scigenom-auth.git
    ```
  
  * Using SSH

    ```sh
    git clone git@github.com:Pratyush1606/scigenom-auth.git
    ```

* Download [pip](https://pip.pypa.io/en/stable/installing/) and add it to the path

* Change your working directory to the the cloned folder

    ```bash
    cd path/to/scigenom-auth
    ```

* Download all the dependencies

    ```bash
    pip install -r requirements.txt
    ```

    Use `pip3` if `pip` not working

* Make a `.env` file in the root directory location only and put the following

    ```python
    DJANGO_SECRET_KEY = django-insecure-%a37a2uf4oz8h=bue_7)7p_&r1tqr&dlh7+-3r+*h)+y)@p9!u
    DJANGO_DEBUG = True
    ```

  * While putting `DEBUG = False`, remember to modify `ALLOWED_HOSTS` (for just quick reference, modify as `ALLOWED_HOSTS = ['*']`)

  * For generating a Django ***SECRET_KEY***, many different sites are there. This [site](https://miniwebtool.com/django-secret-key-generator/) can be used for quick reference.

### Before proceeding further, make sure ```Directory``` looks like

```
scigenom-auth
├── auth
|   ├── __init__.py
|   ├── settings.py
|   ├── asgi.py
|   ├── wsgi.py
|   └── urls.py
├── .gitignore
├── .env
├── manage.py
├── README.md
└── requirements.txt
```

* Migrate to the database

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    Use `python3` if `python` not working

    After this, you would see a new file named `db.sqlite3` in your parent folder

* Run server

    ```sh
    python manage.py runserver
    ```

* Run tests

  ```sh
  python manage.py test
  ```

---
