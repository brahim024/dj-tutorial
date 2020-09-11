from django.urls import path
from myapp.views import PublisherList
urlpatterns = [
    path('publishers/',PublisherList.as_view()),
]