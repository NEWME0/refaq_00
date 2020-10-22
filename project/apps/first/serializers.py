from rest_framework.serializers import ModelSerializer
from .models import User, Group, Scope


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ScopeSerializer(ModelSerializer):
    def to_representation(self, instance):
        result = super(ScopeSerializer, self).to_representation(instance)
        result['users'] = UserSerializer(many=True).to_representation(instance.users)
        result['group'] = GroupSerializer().to_representation(instance.group)
        return result

    class Meta:
        model = Scope
        fields = '__all__'
