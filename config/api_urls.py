from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from poll import views

urlpatterns = [
    path('poll/',
        views.PollList.as_view(),
        name='poll-list'),
    path('poll/<int:pk>/',
        views.PollDetail.as_view(),
        name='poll-detail'),
    path('candidate/',
        views.CandidateList.as_view(),
        name='candidate-list'),
    path('vote/',
        views.VoteList.as_view(),
        name='vote-list'),
    path('result/',
        views.ResultList.as_view(),
        name='result-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
