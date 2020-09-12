from django.urls import path
from myapp.views import PublisherList , PublisherDetail
urlpatterns = [
    path('publisher/',PublisherList.as_view()),
    path('publisher/<int:id>/',PublisherDetail.as_view()),

]