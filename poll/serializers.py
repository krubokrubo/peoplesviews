from rest_framework import serializers
from rest_framework.serializers import ValidationError
from poll import models

class PollSerializer(serializers.ModelSerializer):
#   owner = serializers.HyperlinkedRelatedField(view_name=
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Poll
        fields = ['url', 'id', 'title', 'owner', 'created']



class CandidateSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = models.Candidate
#       fields = ['id', 'title']
        fields = ['id', 'title', 'poll', 'created', 'created_by']


class VoteSerializer(serializers.ModelSerializer):
    voter = serializers.ReadOnlyField(source='voter.username')

    def validate(self, data):
        valid_candidates = models.Candidate.objects.filter(
                poll=data['poll']
            ).values_list('id', flat=True)
        choices = data['ranked_choices'].split(',')
        seen = set()
        for choice in choices:
            if not choice.isdecimal():
                raise ValidationError('bad format:"{}"'.format(choice))
            if choice != str(int(choice)):
                raise ValidationError('bad format:"{}"'.format(choice))
            if int(choice) in seen:
                raise ValidationError('already seen:{}'.format(choice))
            if int(choice) not in valid_candidates:
                raise ValidationError('not a candidate:{}'.format(choice))
            seen.add(int(choice))
        return data

    class Meta:
        model = models.Vote
        fields = ['id', 'poll', 'voter', 'submitted', 'ranked_choices']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
