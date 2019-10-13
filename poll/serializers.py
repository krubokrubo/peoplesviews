from rest_framework import serializers
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
