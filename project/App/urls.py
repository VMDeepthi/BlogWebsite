from django.urls import path
from .views import PostList,PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),  # Make sure 'home' is here
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
