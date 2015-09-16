# django-boilerplate
Django + PostgreSQL + Celery + REST + Requirejs + Bower + Grunt + Foundation + Modernizr + Mailgun

### Setup (Ubuntu)

```
pip install -r requirements/[DEV|STG|PROD].txt

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash
nvm install stable

npm install -g bower
bower install
npm install -g grunt-cli
npm install

sudo apt-get install ruby-full
sudo gem install sass

grunt build
grunt
```

### Run Celery

1. `celery -A django_boilerplate worker -l info`							// start celery worker
2. Open http://127.0.0.1:8000/test-celery and check your worker console		// test celery worker
