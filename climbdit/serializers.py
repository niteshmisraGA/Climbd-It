from rest_framework import serializers
from .models import Climb, Climber, Location, State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['stateName', 'locations']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['locationName', 'climbs']


class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climb
        fields = ['climbName', 'climbGrade', 'climbDescription', 'climbPic', 'climbers']

class ClimberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climber
        fields = ['name']