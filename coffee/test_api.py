import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_category_list():
    client = APIClient()
    response = client.get('/coffee/category/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_drinks_list():
    client = APIClient()
    response = client.get('/coffee/drinks/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_list():
    client = APIClient()
    response = client.get('/coffee/order/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_category_authenticated():
    user = User.objects.create_superuser(username='test', password='test1234')
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.post('/coffee/category/', {'name': 'Tect'})
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_category_simpleuser():
    user = User.objects.create_user(username='tester', password='tester1234')
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    respone = client.post('/coffee/category/', {'name': 'Тест'})
    assert respone.status_code == 403


@pytest.mark.django_db
def test_ingredient_list():
    client = APIClient()
    response = client.get('/coffee/ingredient/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_ingredient_list():
    user = User.objects.create_user(username='test', password='test123')
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.post('/coffee/ingredient/', {'name': 'Тест'})
    assert response.status_code == 403
