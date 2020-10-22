from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import RecordSerializer
from .models import Record


class CreateRecordView(CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class List01RecordView(ListAPIView):
    queryset = Record.objects.all()

    def get_serializer(self, *args, **kwargs):
        return RecordSerializer(*args, **kwargs, fields=['field_01', 'field_02', 'field_03'])


class List02RecordView(ListAPIView):
    queryset = Record.objects.all()

    def get_serializer(self, *args, **kwargs):
        return RecordSerializer(*args, **kwargs, fields=['field_04', 'field_05', 'field_06'])


class List03RecordView(ListAPIView):
    queryset = Record.objects.all()

    def get_serializer(self, *args, **kwargs):
        return RecordSerializer(*args, **kwargs, fields=['field_07', 'field_08', 'field_09'])
