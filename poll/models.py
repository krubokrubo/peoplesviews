from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    
class Candidate(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    datestamp = models.DateTimeField(auto_now=True)

class VoteLine(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    rank = models.IntegerField()

class PollResult(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    datestamp = models.DateTimeField(auto_now=True)
    result = models.TextField()
