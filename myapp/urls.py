from django.urls import path
from django.views.generic import TemplateView
from myapp.views import AuthorView


urlpatterns = [
    #path('publisher/',PublisherList.as_view()),
    #path('publisher/<int:id>/',PublisherDetail.as_view()),
    path('ex1',TemplateView.as_view(template_name='author1.html',extra_context={'title':'Custom Title'})),
    path('ex2',AuthorView.as_view(),name='ex2'),
]