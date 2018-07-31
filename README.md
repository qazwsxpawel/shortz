# Shortz: bare bones url shortener ;)


## Installation & usage

This is a bog standard Django + DRF (https://www.django-rest-framework.org/)
Best way to proceed:

1. `mkvirtualenv shortz`
2. `pip install -r requirements.txt`
3. `(cd shortz/ && ./manage.py migrate)`
4. `(cd shortz/ && ./manage.py runserver)`
5. ready for testing


## Testing

There are no unit tests, as those were not required.
You can test the app using client of your choice (curl, Postman, restclient from Emacs what have you).
Here I'm showing result of using httpie per https://github.com/jakubroztocil/httpie#json

**Valid URL shortening**

```
$ http POST http://127.0.0.1:8000/shorten_url/ url=https://github.com/qazwsxpawel/

HTTP/1.1 201 Created
Allow: OPTIONS, POST
Content-Length: 181
Content-Type: application/json
Date: Tue, 31 Jul 2018 14:19:37 GMT
Server: WSGIServer/0.2 CPython/3.6.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": "oLMpI6NRP8GhPKoPa_UKUg",
    "date_created": "2018-07-31T14:19:37.074597Z",
    "shortened_url": "http://localhost:8000/oLMpI6NRP8GhPKoPa_UKUg",
    "url": "https://github.com/qazwsxpawel/"
}

```

**Invalid URL handling***

```
$ http POST http://127.0.0.1:8000/shorten_url/ url=https://github/qazwsxpawel/

HTTP/1.1 400 Bad Request
Allow: OPTIONS, POST
Content-Length: 30
Content-Type: application/json
Date: Tue, 31 Jul 2018 14:21:22 GMT
Server: WSGIServer/0.2 CPython/3.6.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "url": [
        "Enter a valid URL."
    ]
}

```

## Scaling
## Next steps
