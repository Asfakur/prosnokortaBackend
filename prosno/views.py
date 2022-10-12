from . models import Question, Review
from rest_framework.response import Response
from .serializers import QuestionSerializer, ReveiwSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend



class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # for filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_no', 'course', 'chapter', 'author']


    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        if question.points > 0:
            return Response({"error": "Question alredey used should not be deleted"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):

    # queryset = Review.objects.all()
    def get_queryset(self):
        return Review.objects.filter(question_id=self.kwargs['question_pk'])

    serializer_class = ReveiwSerializer


    # in this view class we have access to urls params
    # so we can read the question id from the urls
    # and using context object we can pass it to serializer
    # we use context object to provide additional data to serializer
    
    def get_serializer_context(self):
        return {'question_id': self.kwargs['question_pk']}
