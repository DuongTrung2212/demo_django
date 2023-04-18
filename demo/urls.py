from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import home
from . import views

router = DefaultRouter()
router.register("courses", views.CourseViewSet)
router.register("lessons", views.LessonViewSet)
router.register("users", views.UserViewSet)
# router.register('courses', home)

urlpatterns = [
    # path('', home.index, name='index'),
    path("", include(router.urls)),
]
