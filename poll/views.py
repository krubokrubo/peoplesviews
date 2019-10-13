from django.shortcuts import render
from django.views.generic.detail import DetailView
from poll import models
from poll import serializers
from poll import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend


class PollMainView(DetailView):
    model = models.Poll
    template_name = 'poll_main.html'


# REST API views below

class PollList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsOwnerOrReadOnly]
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer


class CandidateList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
#   filter_backends = [DjangoFilterBackend]
    filterset_fields = ['poll']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class CandidatesByPoll(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CandidateSerializer

    def get_queryset(self):
        poll_id = self.kwargs['poll']
        return models.Candidate.objects.filter(poll=poll_id)
