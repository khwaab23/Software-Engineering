# from django.urls import path
# from .views import cv_view  # Import your view

# urlpatterns = [
#     path('cv/', cv_view, name='cv'),  # URL pattern for the CV page
# ]
from django.urls import path
from .views import cv_view

urlpatterns = [
    path('', cv_view, name='cv'),  
]
