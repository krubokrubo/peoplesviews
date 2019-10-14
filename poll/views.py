from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils.html import escape
from django.http import HttpResponse, StreamingHttpResponse
from poll import models
from poll import serializers
from poll import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend
import time


# this doesn't work with current configuration :(
def chunked_result_calc(pk):
    yield '<pre>Thank you for triggering the RESULT CALCULATION function.\n'
    yield 'Please wait while the result is being calculated.\n'
    yield ' ' * 1024
    yield '\n'
    poll = models.Poll.objects.get(id=pk)
    candidates = poll.candidate_set.all()
    votes = poll.vote_set.all()
    yield 'A total of {} votes were cast.\n'.format(votes.count())
    for vote in votes:
        yield 'Vote: {}\n'.format(vote.ranked_choices)
    time.sleep(2)
    yield 'This could take a while...\n'
    time.sleep(4)
    yield '...since the calculations are not yet built. Sorry. Goodbye.\n'
    yield '</pre>'


#def calculate_result(pk):
#    yield 'Calculating the result of the 


class PollMainView(DetailView):
    model = models.Poll
    template_name = 'poll_main.html'

    def post(self, request, pk):
        return StreamingHttpResponse(chunked_result_calc(pk))
#       return HttpResponse('''Pk was {} and you posted the following data:
#                            <pre>{}</pre>'''
#           .format(pk, escape(request.POST)))


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
