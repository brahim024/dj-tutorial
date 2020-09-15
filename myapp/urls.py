from django.urls import path
from .import views
app_name='myapp'
urlpatterns = [
	path('',views.post_list,name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_details,name='post_detail'),
    #path('publisher/',PublisherList.as_view()),
    #path('publisher/<int:id>/',PublisherDetail.as_view()),
    #path('ex1',TemplateView.as_view(template_name='myapp/author1.html',extra_context={'title':'Custom Title'})),
    #path('ex2',AuthorView.as_view(),name='auther'),
]