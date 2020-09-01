from django.urls import path
from. import views
urlpatterns=[
	path('bombi',views.artists,name='artists'),
]
