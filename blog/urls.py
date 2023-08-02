from django.urls import path
from .views import BlogListView, BlogDetaiLView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetaiLView.as_view(), name='post_detail')
]
