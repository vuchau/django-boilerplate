# django-boilerplate
Django + Celery + REST + Requirejs + Bower + Grunt + Foundation + Modernizr

### Setup

1. `pip install -r requirements.txt`	// install requirements
2. `npm install -g bower`           	// install bower
3. `bower install`                  	// install bower packages
4. `npm install -g grunt-cli`       	// install grunt-cli
5. `npm install`                    	// install node packages
6. `grunt build`                    	// build static/css/app.css
7. `grunt`                          	// watch for scss changes


### Run Celery

1. `celery -A django_boilerplate worker -l info`							// start celery worker
2. Open http://127.0.0.1:8000/test-celery and check your worker console		// test celery worker
