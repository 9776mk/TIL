## Admin site

- 관리자 페이지

```bash
 python manage.py createsuperuser
 
Username (leave blank to use 'user'): admin
Email address: # 입력 안하고 엔터
Password: # 1234
Password (again): # 1234
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

```python
# admin.py에 등록하기
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```



## Static files
- 웹 서버는 요청받은 특정 위치(URL)로 서버에 존재하는 정적자원(Static resource)을 제공

> articles/static/보노보노.jpeg

- 사용할 html
```python
{% load static %} 
<img src="{% static '보노보노.jpeg' %} alt="">
```

```python
# seeting.py에서 확인
STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR/ 'static']
```

## + django_bootstrap
```bash
pip install django-bootstrap5
```

```python
# settings.py
INSTALLED_APPS = [
	'django_bootstrap5',
]
```

```html
<!-- 사용할 html-->
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}

{% bootstrap_form article_form %}
```
