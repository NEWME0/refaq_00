from ..first.serializers import PartialModelSerializer
from .models import Record


class RecordSerializer(PartialModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
