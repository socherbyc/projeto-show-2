




8-> integrar com programa que multiplica as matrizes



## setup
```
pip install django

# https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html
pip install Celery
sudo apt-get install -y erlang
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
# sudo systemctl status rabbitmq-server

# -c = número de workers paralelos
celery -A trab2 worker -c 1 -l info

```

## run
```
python manage.py runserver 0.0.0.0:8000
```