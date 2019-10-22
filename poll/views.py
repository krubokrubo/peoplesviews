from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils.html import escape
from django.http import HttpResponse, StreamingHttpResponse
from poll import models
from poll import serializers
from poll import permissions
from poll import compute
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend
import time




class PollMainView(DetailView):
    model = models.Poll
    template_name = 'poll_main.html'

    def post(self, request, pk):
        return StreamingHttpResponse(compute.chunked_result(pk))
#       return HttpResponse('''Pk was {} and you posted the following data:
#                            <pre>{}</pre>'''
#           .format(pk, escape(request.POST)))

def recalculate(request, pk):
    return StreamingHttpResponse(compute.chunked_result(pk))


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
    


class VoteList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer
    filterset_fields = ['poll']

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user)


class ResultList(ListAPIView):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    filterset_fields = ['poll']
