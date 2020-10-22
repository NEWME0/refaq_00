from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer, GroupSerializer, ScopeSerializer
from .models import User, Group, Scope


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GroupListCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class ScopeListCreateView(ListCreateAPIView):
    serializer_class = ScopeSerializer
    queryset = Scope.objects.all()
