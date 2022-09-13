from django.urls import path
from .views import *

urlpatterns = [
    path('articlelist/', ArticleList.as_view()),

]
