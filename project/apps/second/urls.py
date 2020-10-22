from django.urls import path
from .views import CreateRecordView, List01RecordView, List02RecordView, List03RecordView


urlpatterns = [
    path('record/', CreateRecordView.as_view()),
    path('record/01/', List01RecordView.as_view()),
    path('record/02/', List02RecordView.as_view()),
    path('record/03/', List03RecordView.as_view()),
]
