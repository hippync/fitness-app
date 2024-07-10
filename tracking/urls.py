from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProfileViewSet, ActivityViewSet, WorkoutPlanViewSet, WorkoutSessionViewSet, GoalViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'workout-sessions', WorkoutSessionViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'progresses', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
