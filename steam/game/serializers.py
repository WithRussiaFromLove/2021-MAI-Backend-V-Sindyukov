from rest_framework import serializers
from .models import *

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = '__all__'

class GamePublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePublisher
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'