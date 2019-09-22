from django.urls import path, include
from projects.views import project_index, project_detail

urlpatterns = [
    path('', project_index, name="project_index"),

    # <int:pk> tells django that the value passed in the
    # URLs is an integer and its variable name is pk.
    path('<int:pk>/', project_detail, name="project_detail"),


]
