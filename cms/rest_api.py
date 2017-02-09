from rest_framework import serializers, routers, viewsets

from cms.models import Game, Competition, Team, Player, Map


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    map_set = MapSerializer(many=True)
    team_set = TeamSerializer(many=True)
    class Meta:
        model = Game
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'







class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class CompetitionViewSet(viewsets.ModelViewSet):
    serializer_class = CompetitionSerializer
    def get_queryset(self):
        game = self.request.query_params.get('game', None)
        queryset = Competition.objects.all()
        if game:
            queryset = Competition.objects.filter(game__id=game)
        return queryset


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


router = routers.DefaultRouter()
router.register(r'games', GameViewSet, base_name='games')
router.register(r'competitions', CompetitionViewSet, base_name='competitions')
router.register(r'teams', TeamViewSet, base_name='teams')
router.register(r'players', PlayerViewSet, base_name='players')
