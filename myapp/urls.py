from django.urls import path
from myapp.views import PersonCreateView
urlpatterns=[
	path('bombi',PersonCreateView.as_view(),name='PersonCreateView'),
]
