
from django.urls import path, include
from .views import landing_view
urlpatterns = [

    # This looks for the urls.py inside the projects
    # application and register any URLs defined there.
    path('', landing_view, name='landing_page'),
]
