from django.urls import path
from myapp.views import PublisherList , PublisherDetail, AuthorList
urlpatterns = [
    path('publisher/',PublisherList.as_view()),
    path('publisher/<int:id>/',PublisherDetail.as_view()),
    path('auther/',AuthorList.as_view()),
]