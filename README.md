# Evaluatortest
Project Submission for International Womens Hackathon 2018 Hackerearth
## How to test the app.

Follow the steps below to start the development server on localhost.
__Install python3 if you haven't already__
__python-virtualenv is also required.__
1. Create a virtual environment:
```
$ virtualenv -p python3 env
```

2. Activate the virtual environment:
```
$ cd env
$ source bin/activate
```

3. Clone this repo:
```
(env) $ git clone https://github.com/heerqaz/evaluatortest.git
```

4. Install the requirements:
```
(env) $ pip3 install -r requirements.txt
```

5. Run the migrations and collect staticfiles.
```
(env) $ cd evaluatortest
(env) $ python3 manage.py migrate
(env) $ python3 manage.py collectstatic
```

6. Start the server:
```
(env) $ python3 manage.py runserver
```

7. Open (http://localhost:8000/) in your web browser.
8. Create a superuser :
```
(env) $ python manage.py createsuperuser
```
9. Go to http://localhost:8000/admin to add questions.
