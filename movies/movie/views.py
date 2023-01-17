from .serializers import UserSerializer, MovieSerializer, CurrUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, views
from rest_framework.response import Response
from .permissions import IsAdmin, IsEditable, IsUser
from .models import Movies, Review
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):  # this view is for admin to view all users and update their credentials
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, IsAuthenticated)
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id', 'email']

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='delete success')


class MovieViewSet(viewsets.ModelViewSet):  # This view is for the movies
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsEditable, IsAuthenticated)
    filter_backends = [DjangoFilterBackend]  # filter for the movies on the basis of movie id, genre and movie_name

    filterset_fields = ['id', 'genre', 'movie_name']

    # @action()


class CurrentUser(viewsets.ModelViewSet):  # This view is for the current user to change his credentials
    serializer_class = CurrUserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'put', 'delete')

    def get_queryset(self):
        user = self.request.user.id
        return User.objects.filter(pk=user)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='delete success')


class MovieReview(views.APIView):  # This view is for rating of the movie
    permission_classes = [IsAuthenticated, IsUser]

    def get(self, request, movie_id):
        try:
            movie = Movies.objects.filter(pk=movie_id).first()
            reviews = list(Review.objects.filter(movie_id=movie_id).values("author", "comment", "stars"))
            return Response({'data': movie.movie_name, 'review': reviews})
        except:
            return Response({'Error': "No Movie Found"})

    def post(self, request, movie_id):
        author = request.user.first_name + " " + request.user.last_name
        comments = request.data['comment']
        stars = request.data['stars']
        # print(author, comments, stars, movie_id)
        review = Review(author=author, stars=stars, comment=comments, movie_id=movie_id)
        review.save()
        return Response({'data': "Rating is received"})
