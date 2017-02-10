from rest_framework import serializers, routers, viewsets
from rest_framework.response import Response
from cms.models import Game, Competition, Team, Player, Map, TeamPlayer, Match, MatchMap, MatchMapTeamResult


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class TeamPlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    class Meta:
        model = TeamPlayer
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    teamplayer_set = TeamPlayerSerializer(many=True)
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


class MatchMapTeamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchMapTeamResult
        fields = '__all__'


class MatchMapSerializer(serializers.ModelSerializer):
    matchmapteamresult_set = MatchMapTeamResultSerializer(many=True)
    class Meta:
        model = MatchMap
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    #result = TeamResultSerializer(many=True)
    #teamresult_set = TeamResultSerializer(many=True)
    matchmap_set = MatchMapSerializer(many=True)
    class Meta:
        model = Match
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

class TeamPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TeamPlayerSerializer
    def get_queryset(self):
        team = self.request.query_params.get('team', None)
        queryset = TeamPlayer.objects.all()
        if team:
            queryset = TeamPlayer.objects.filter(team=team)
        return queryset

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

    def create(self, validated_data):
        print(validated_data.data['matchmap_set'])
        matchmap_set = validated_data.data.pop('matchmap_set')

        # Get competition object to pass to match object being created
        competition = validated_data.data.pop('competition')
        competition = Competition.objects.get(pk=competition)
        # Create match object
        match = Match.objects.create(
            competition=competition,
            **validated_data.data
        )
        # Loop through maps being played
        for mm in matchmap_set:
            matchmapteamresult_set =  mm.pop('matchmapteamresult_set')

            # Get map
            map = mm.pop('map')
            map = Map.objects.get(pk=map)

            match_map = MatchMap.objects.create(
                match=match,
                map=map
            )
            for mmtr in matchmapteamresult_set:
            #    match_mapold = mmtr.pop('match_map')
                team = mmtr.pop('team')
                team = Team.objects.get(pk=team)
                fielded_roster = mmtr.pop('fielded_roster')
                match_map_team_result = MatchMapTeamResult.objects.create(
                    match_map=match_map,
                    team=team,
                    **mmtr
                )
                for fr in fielded_roster:
                    match_map_team_result.fielded_roster.add(fr)

        return Response(match)


router = routers.DefaultRouter()
router.register(r'games', GameViewSet, base_name='games')
router.register(r'competitions', CompetitionViewSet, base_name='competitions')
router.register(r'teams', TeamViewSet, base_name='teams')
router.register(r'matches', MatchViewSet, base_name='matches')
router.register(r'maps', MapViewSet, base_name='maps')
router.register(r'teamplayers', TeamPlayerViewSet, base_name='teamplayers')
