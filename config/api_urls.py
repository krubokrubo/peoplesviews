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
#   path('poll/<int:poll>/candidate/',
#       views.CandidatesByPoll.as_view(),
#       name='candidates-by-poll'),
    path('candidate/',
        views.CandidateList.as_view(),
        name='candidate-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
