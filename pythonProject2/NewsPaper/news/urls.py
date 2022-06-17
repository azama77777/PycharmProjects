from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('postcreate/', PostCreate.as_view()),
    path('postlist/', PostList.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),
]
