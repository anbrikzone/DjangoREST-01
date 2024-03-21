from django.urls import path, include
from .views import PostAPIView


urlpatterns = [
    path('', view=PostAPIView.as_view(), name='post-list'),
]