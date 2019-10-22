from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255, unique=True)
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['poll','title'],
                                    name='unique_candidates_per_poll'),
        ]

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    submitted = models.DateTimeField(auto_now=True)
    ranked_choices = models.CharField(max_length=1000)

    def get_username(self):
        if self.voter is None:
            return 'None'
        return self.voter.username

# NOT USED CURRENTLY. SIMPLY SAVING ALL RANKED_CHOICES IN THE VOTE OBJECT
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

class Result(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    datestamp = models.DateTimeField(auto_now=True)
    method_name = models.CharField(max_length=255)
    detail = models.TextField()
