
from itertools import product
from rest_framework import serializers
from prosno.models import Course, Question, Review, User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = []        
        # extra_kwargs = {
        #     'explanation': {'write_only': True},
        #     'course': {'write_only': True},
        #     'question_maker': {'write_only': True},
        #     'answer': {'write_only': True},
        #     # 'points': {'read_only': True}
        # }
        
class QuestionSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']

class ReveiwSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'description', 'date', 'user']

    
    def create(self, validated_data):
        question_id = self.context['question_id']
        return Review.objects.create(question_id=question_id, **validated_data)