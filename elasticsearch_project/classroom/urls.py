from django.urls import path

from .views import GetCreateClassroom, ClassroomListView

urlpatterns = [
    path('<int:id>/', GetCreateClassroom.as_view()),
    path('', ClassroomListView.as_view()),
]