from django.urls import path
from. import views
urlpatterns=[
	path('bombi',views.artist,name='artist'),
]
