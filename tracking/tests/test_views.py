import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from tracking.models import (
    CustomUser,
    Profile,
    Activity,
    WorkoutPlan,
    WorkoutSession,
    Goal,
    Progress,
)

# Create your tests here.

# Integration tests for views

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def create_profile(db):
    def make_profile(user, **kwargs):
        return Profile.objects.create(user=user, **kwargs)

    return make_profile


@pytest.mark.django_db
def test_user_creation(api_client):
    payload = {
        "username": "testuser",
        "password": "testpass123",
        "height": 180,
        "weight": 75,
        "date_of_birth": "1990-01-01",
        "user_id": "test_user_id",
    }
    response = api_client.post("/api/users/", payload)
    assert response.status_code == 201
    assert User.objects.filter(username="testuser").exists()


@pytest.mark.django_db
def test_profile_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    payload = {
        "profile_id": "profile1",
        "user": user.id,
        "profile_picture": "path/to/picture",
        "bio": "This is a bio",
    }
    response = api_client.post("/api/profiles/", payload)
    assert response.status_code == 201
    assert Profile.objects.filter(profile_id="profile1").exists()


@pytest.mark.django_db
def test_activity_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    payload = {
        "activity_id": "activity1",
        "user": user.id,
        "activity_type": "running",
        "duration": 30,
        "distance": 5.0,
        "date": "2023-01-01",
        "calories_burned": 300,
    }
    response = api_client.post("/api/activities/", payload)
    assert response.status_code == 201
    assert Activity.objects.filter(activity_id="activity1").exists()


@pytest.mark.django_db
def test_workout_plan_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    payload = {
        "plan_id": "plan1",
        "user": user.id,
        "plan_name": "Plan A",
        "start_date": "2023-01-01",
        "end_date": "2023-01-30",
        "goals": "Lose weight",
    }
    response = api_client.post("/api/workout-plans/", payload)
    assert response.status_code == 201
    assert WorkoutPlan.objects.filter(plan_id="plan1").exists()


@pytest.mark.django_db
def test_workout_session_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    plan = WorkoutPlan.objects.create(
        plan_id="plan1",
        user=user,
        plan_name="Plan A",
        start_date="2023-01-01",
        end_date="2023-01-30",
        goals="Lose weight",
    )
    activity = Activity.objects.create(
        activity_id="activity1",
        user=user,
        activity_type="running",
        duration=30,
        distance=5.0,
        date="2023-01-01",
        calories_burned=300,
    )
    payload = {
        "session_id": "session1",
        "plan": plan.plan_id,  # Use plan_id instead of id
        "activity": activity.activity_id,  # Use activity_id instead of id
        "date": "2023-01-01",
        "notes": "Great session",
    }
    response = api_client.post("/api/workout-sessions/", payload)
    assert response.status_code == 201
    assert WorkoutSession.objects.filter(session_id="session1").exists()


@pytest.mark.django_db
def test_goal_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    payload = {
        "goal_id": "goal1",
        "user": user.id,
        "description": "Run a marathon",
        "target_date": "2023-04-01",
        "is_achieved": False,
    }
    response = api_client.post("/api/goals/", payload)
    assert response.status_code == 201
    assert Goal.objects.filter(goal_id="goal1").exists()


@pytest.mark.django_db
def test_progress_creation(api_client, create_user):
    user = create_user(username="testuser", password="testpass123")
    payload = {
        "progress_id": "progress1",
        "user": user.id,
        "date": "2023-01-01",
        "weight": 70.0,
        "body_fat_percentage": 15.0,
        "muscle_mass": 30.0,
    }
    response = api_client.post("/api/progresses/", payload)
    assert response.status_code == 201
    assert Progress.objects.filter(progress_id="progress1").exists()
