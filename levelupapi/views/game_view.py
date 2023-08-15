"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
        Response -- JSON serialized game instance 
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            title=request.data["title"],
            game_type=game_type,
            creator=gamer,
            description=request.data["description"],
            players_needed=request.data["players_needed"],
            skill_level=request.data["skill_level"]
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'game_type_id', 'creator_id', 'description', 'players_needed', 'skill_level')