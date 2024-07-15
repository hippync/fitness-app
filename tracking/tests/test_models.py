import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from tracking.models import (
    Profile,
    Activity,
    WorkoutPlan,
    WorkoutSession,
    Goal,
    Progress,
)

# Create your tests here.

# Unit tests for models

User = get_user_model()


@pytest.mark.django_db
def test_create_custom_user():
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
        height=180,
        weight=75,
        date_of_birth="1990-01-01",
        user_id="test_user_id",
    )
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.height == 180
    assert user.weight == 75
    assert str(user) == "test_user_id"


@pytest.mark.django_db
def test_create_profile():
    user = User.objects.create_user(username="testuser", password="testpass123")
    profile = Profile.objects.create(
        profile_id="profile1",
        user=user,
        profile_picture="path/to/picture",
        bio="This is a bio",
    )
    assert profile.profile_id == "profile1"
    assert profile.user == user
    assert profile.profile_picture == "path/to/picture"
    assert profile.bio == "This is a bio"
    assert str(profile) == "profile1"


@pytest.mark.django_db
def test_create_activity():
    user = User.objects.create_user(username="testuser", password="testpass123")
    activity = Activity.objects.create(
        activity_id="activity1",
        user=user,
        activity_type="running",
        duration=30,
        distance=5.0,
        date=timezone.now().date(),
        calories_burned=300,
    )
    assert activity.activity_id == "activity1"
    assert activity.user == user
    assert activity.activity_type == "running"
    assert activity.duration == 30
    assert activity.distance == 5.0
    assert activity.calories_burned == 300
    assert str(activity) == "activity1"


@pytest.mark.django_db
def test_create_workout_plan():
    user = User.objects.create_user(username="testuser", password="testpass123")
    workout_plan = WorkoutPlan.objects.create(
        plan_id="plan1",
        user=user,
        plan_name="Plan A",
        start_date=timezone.now().date(),
        end_date=timezone.now().date() + timezone.timedelta(days=30),
        goals="Lose weight",
    )
    assert workout_plan.plan_id == "plan1"
    assert workout_plan.user == user
    assert workout_plan.plan_name == "Plan A"
    assert workout_plan.goals == "Lose weight"
    assert str(workout_plan) == "plan1"


@pytest.mark.django_db
def test_create_workout_session():
    user = User.objects.create_user(username="testuser", password="testpass123")
    workout_plan = WorkoutPlan.objects.create(
        plan_id="plan1",
        user=user,
        plan_name="Plan A",
        start_date=timezone.now().date(),
        end_date=timezone.now().date() + timezone.timedelta(days=30),
        goals="Lose weight",
    )
    activity = Activity.objects.create(
        activity_id="activity1",
        user=user,
        activity_type="running",
        duration=30,
        distance=5.0,
        date=timezone.now().date(),
        calories_burned=300,
    )
    workout_session = WorkoutSession.objects.create(
        session_id="session1",
        plan=workout_plan,
        activity=activity,
        date=timezone.now().date(),
        notes="Great session",
    )
    assert workout_session.session_id == "session1"
    assert workout_session.plan == workout_plan
    assert workout_session.activity == activity
    assert workout_session.notes == "Great session"
    assert str(workout_session) == "session1"


@pytest.mark.django_db
def test_create_goal():
    user = User.objects.create_user(username="testuser", password="testpass123")
    goal = Goal.objects.create(
        goal_id="goal1",
        user=user,
        description="Run a marathon",
        target_date=timezone.now().date() + timezone.timedelta(days=100),
        is_achieved=False,
    )
    assert goal.goal_id == "goal1"
    assert goal.user == user
    assert goal.description == "Run a marathon"
    assert not goal.is_achieved
    assert str(goal) == "goal1"


@pytest.mark.django_db
def test_create_progress():
    user = User.objects.create_user(username="testuser", password="testpass123")
    progress = Progress.objects.create(
        progress_id="progress1",
        user=user,
        date=timezone.now().date(),
        weight=70.0,
        body_fat_percentage=15.0,
        muscle_mass=30.0,
    )
    assert progress.progress_id == "progress1"
    assert progress.user == user
    assert progress.weight == 70.0
    assert progress.body_fat_percentage == 15.0
    assert progress.muscle_mass == 30.0
    assert str(progress) == "progress1"


# Integration tests for views
