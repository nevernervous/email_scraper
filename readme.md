### INSTRUCTIONS FOR DEV STATION SETUP

Requires python 3.5.2

How to run:
```
npm install -g bower
bower install
pip install -r requirements.txt
python manage.py runserver

celery -A email_scraper worker -l info
```