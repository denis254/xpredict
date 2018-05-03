from rest_framework import serializers

from .models import FreeTipsGames, SingleBetGames

class FreeTipsGamesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = FreeTipsGames

        fields = ('published_date', 'country', 'home_team', 'home_score', 'away_score', 'away_team', 'prediction', 'status')


class SingleBetGamesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = SingleBetGames

        fields = ('published_date', 'country', 'home_team', 'home_score', 'away_score', 'away_team', 'prediction', 'status')
