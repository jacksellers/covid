# covid


### Description


### Installation

Console 1 - Redis:
```
git clone https://github.com/jackwsellers/covid.git
cd covid
virtualenv appenv
source appenv/bin/activate
pip install -r requirements.txt
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
src/redis-server
```

Console 2 - Django (from 'covid'):
```
source appenv/bin/activate
cd app
python manage.py migrate
python manage.py runserver
```

Console 3 - Celery worker (from 'covid/app'):
```
source appenv/bin/activate
cd app
celery -A app worker -l info
```

Console 4 - Celery beat (from 'covid/app'):
```
source appenv/bin/activate
cd app
celery -A app beat -l info
```


### Testing