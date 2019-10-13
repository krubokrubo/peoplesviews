from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Candidate(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    datestamp = models.DateTimeField(auto_now=True)

class VoteLine(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    rank = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vote','rank'],
                                    name='unique_ranks_per_vote'),
            models.UniqueConstraint(fields=['vote','candidate'],
                                    name='unique_candidates_per_vote'),
        ]

class PollResult(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    datestamp = models.DateTimeField(auto_now=True)
    result = models.TextField()
