# Cheesy Pizza

The django backend for the cheesypizza website

## Run the project

This project is a back-end template and can be used for various front-end service. It utilizes the `Django Rest Framework` and has an API.

The project is using `Python3.6.9` and any other version will cause some errors.

To run locally:

- Create the python virtual environment

  ```
     python3.6.9 -m venv env

  ```

- Activate the env

  ```
      source ./env/bin/activate

  ```

- Upgrade the pip

  ```
      pip install --upgrade pip

  ```

* `cd` into the src folder. Install the requirements

  ```
      pip install -r requirements.txt

  ```

* Migrate, makemigrations, migrate!

  ```
      python manage.py migrate

      python manage.py makemigrations

      python manage.py migrate

  ```

* Create the super user

  ```
      python manage.py createsuperuser

  ```

* Run the local server

  ```
      python manage.py runserver
  ```

This will run the server on `localhost:8000`

You can change it by passing the IP and the port as an argument after the runserver command.

For the development database I'm using the standard `SQLite` db, but in the production I set it up the `PostgreSQL` db. If you're going to run this on the production, make sure to change the db settings in the settings_prod.py file and also add the allowed hosts and whitelist the origins.

You can checkout the DigitalOcean's articles on

[how to install and run django locally](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

&

[how to configure django with nginx on production](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn)
