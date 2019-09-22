from django.urls import path, include
from .views import blog_index, blog_detail, blog_category
urlpatterns = [

    # This looks for the urls.py inside the projects
    # application and register any URLs defined there.
    path('', blog_index, name='blog_index'),
    path('<category>/', blog_category, name='blog_category'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
]
