import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from theatre.models import Actor, Director

@pytest.mark.django_db
def test_actor_list_view(client):
    Actor.objects.create(first_name="Tom", last_name="Cruise")
    url = reverse('actor_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Tom" in response.content.decode()

@pytest.mark.django_db
def test_director_list_view_authenticated(client):
    user = User.objects.create_user(username='tester', password='secret')
    client.login(username='tester', password='secret')
    Director.objects.create(first_name="Quentin", last_name="Tarantino")
    url = reverse('director_list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Tarantino" in response.content.decode()

@pytest.mark.django_db
def test_add_actor_view_post_valid_data(client, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='secret')
    client.login(username='testuser', password='secret')
    url = reverse('add_actor')
    data = {"first_name": "Emma", "last_name": "Stone"}
    response = client.post(url, data)
    assert response.status_code == 302
    assert Actor.objects.filter(first_name="Emma", last_name="Stone").exists()


