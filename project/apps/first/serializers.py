from rest_framework.serializers import ModelSerializer
from .models import User, Group, Scope


class PartialModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(PartialModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            for field_name in set(self.fields) - set(fields):
                self.fields.pop(field_name)


class UserSerializer(PartialModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(PartialModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ScopeSerializer(PartialModelSerializer):
    def to_representation(self, instance):
        result = super(ScopeSerializer, self).to_representation(instance)
        result['users'] = UserSerializer(many=True).to_representation(instance.users)
        result['group'] = GroupSerializer(fields=['id', 'title']).to_representation(instance.group)
        return result

    class Meta:
        model = Scope
        fields = '__all__'
