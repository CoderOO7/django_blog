# django_blog

It's a blog app made in django for playing with django framework.

## REQUIREMENTS
* python 3.7.5+
* pip
* MySQL
* npm 

## Running the app

1. If the above tools are installed correctly then run below commands:
    ```bash
    $ git clone https://github.com/CoderOO7/django_blog.git
    $ cd django_blog
    $ virtualenv -p <python3.7 binary path> venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
     ```
2. Create a database using mysql. For ex: django_blog

3. Create copy of `.env.sample` with file name `.env` in directory django_blog. And provide required credentials.
    ```
      SECRET_KEY=0x!b#(1*cd73w$&azzc6p+essg7v=g80ls#z&xcx*mpemx&@9$
      DATABASE_NAME=db_name
      DATABASE_USER=db_user
      DATABASE_PASSWORD=password
      DATABASE_HOST=localhost
      DATABASE_PORT=8000
      DATABASE_ENGINE=django.db.backends.mysql
     ```
4. Get back to root directory to perform database migrations and create super user
    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
    ```
   
5. At last run the server
   ```
   python manage.py runserver
   ```