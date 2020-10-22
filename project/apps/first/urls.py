from django.urls import path
from .views import UserListCreateView, GroupListCreateView, ScopeListCreateView


urlpatterns = [
    path('user/', UserListCreateView.as_view()),
    path('group/', GroupListCreateView.as_view()),
    path('scope/', ScopeListCreateView.as_view()),
]
