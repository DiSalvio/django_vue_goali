from rest_framework import serializers

from .models import Goal

class GoalSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'name', 'description', 'status')
