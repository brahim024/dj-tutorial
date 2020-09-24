from django.urls import path
from .import views
from .views import PostListView
from .feed import LatestPostFeed
app_name='myapp'
urlpatterns = [
	path('post',PostListView.as_view(),name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_details,name='post_detail'),
	path('<int:post_id>/share/',views.post_share, name='post_share'),
	path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    path('feed/',LatestPostFeed(),name='post_feed'),
	#path('',views.post_list,name='post_list'),
	#path('publisher/',PublisherList.as_view()),
    #path('publisher/<int:id>/',PublisherDetail.as_view()),
    #path('ex1',TemplateView.as_view(template_name='myapp/author1.html',extra_context={'title':'Custom Title'})),
    #path('ex2',AuthorView.as_view(),name='auther'),
] 