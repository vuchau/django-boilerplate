# django-boilerplate
Django + PostgreSQL + Celery + REST + Requirejs + Bower + Grunt + Foundation + Modernizr

### Setup (Ubuntu)

```
pip install -r requirements.txt
sudo npm install -g bower
sudo apt-get install nodejs-legacy
bower install
sudo npm install -g grunt-cli
sudo npm install
sudo apt-get install ruby-full
sudo gem install sass
grunt build
grunt
```

### Run Celery

1. `celery -A django_boilerplate worker -l info`							// start celery worker
2. Open http://127.0.0.1:8000/test-celery and check your worker console		// test celery worker
