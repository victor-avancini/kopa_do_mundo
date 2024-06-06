from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from exception import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from teams.models import Team
from utils import data_processing


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data

        try:
            data_processing(data)
            team = Team.objects.create(**data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"message": str(e)}, 400)
        except Exception as e:
            return Response({"message": "Internal server error"}, 500)

        team_dict = model_to_dict(team)

        return Response(team_dict, 201)

    def get(self, request: Request) -> Response:
        teams_dict = [
            model_to_dict(team) for team in Team.objects.all()
        ]
        return Response(teams_dict, 200)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(team)
        return Response(team_dict, 200)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        data = request.data

        for key, value in data.items():
            setattr(team, key, value)
        team.save()

        team_dict = model_to_dict(team)
        return Response(team_dict, 200)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()
            return Response(204)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
