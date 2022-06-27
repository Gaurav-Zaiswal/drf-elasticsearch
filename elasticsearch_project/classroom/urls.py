from django.urls import path

from .views import GetCreateClassroom

urlpatterns = [
    path('<int:id>/', GetCreateClassroom.as_view())
]