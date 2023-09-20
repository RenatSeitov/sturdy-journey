import random
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer, UserSerializer,TimeIntervalSerializer 

class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MetricsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TimeIntervalSerializer

    def post(self, request):
        start_date = request.data.get('start_time')
        end_date = request.data.get('end_time')
        if start_date is None or end_date is None:
            return Response({'error': 'Start date and end date are required.'}, status=400)
      
        if start_date > end_date:
            return Response({'error': 'Start date cannot be greater than end date.'}, status=400)

        metrix = {
            'Indastry box office': random.randint(1,100),
            'val': round(random.uniform(0, 10),2),
            'seasomasity':  round(random.uniform(0, 100),2),
            'percent': random.randint(1, 100)
            }
        return Response(metrix)