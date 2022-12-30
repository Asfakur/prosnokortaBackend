
from rest_framework import serializers
from prosno.encryptions import generateHash, generateKey
from prosno.models import Chapter, Class, Course, Exam, Question, QuestionInExam, Review, Set, Profile


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

# class SimpleQuestionSeriralizer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['id', 'description', 'first_option', 'second_option', 'third_option', 'fourth_option', 'answer']
#     answer = serializers.SerializerMethodField(method_name='encryt_answer')

#     def encryt_answer(self, question: Question):
#         return question.answer * 5


# some constant for hashing
MOD_1 = 1002523
MOD_2 = 1000457
BASE_1 = 257
BASE_2 = 263


class SimpleQuestionSeriralizer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'description', 'first_option',
                  'second_option', 'third_option', 'fourth_option', 'answer']
#     answer = serializers.SerializerMethodField(method_name='encryt_answer')

# ###################

#     def encryt_answer(self, question: Question):
#         actual_answer = chr(question.answer)

#         hashKey_1 = generateKey()
#         hashKey_2 = generateKey()

#         print(hashKey_2)
#         print(hashKey_1)

#         hashValue_1 = generateHash(hashKey_1, actual_answer, BASE_1, MOD_1)
#         hashValue_2 = generateHash(hashKey_2, actual_answer, BASE_2, MOD_2)

#         return [hashValue_1, hashKey_1, hashValue_2, hashKey_2]

#################


class QuestionSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['points']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = []


class ReveiwSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = Review
        fields = ['id', 'description', 'date', 'profile']

    def create(self, validated_data):
        question_id = self.context['question_id']
        return Review.objects.create(question_id=question_id, **validated_data)


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        exclude = []


class QuestionInExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionInExam
        # fields = ['set', 'question']
        exclude = []


class QuestionInExamSerializerReadOnly(serializers.ModelSerializer):
    question = SimpleQuestionSeriralizer()

    class Meta:
        model = QuestionInExam
        # fields = ['question']
        fields = ['id', 'set', 'question']
        # exclude = []


class ClassSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = []


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = []


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        exclude = []


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        exclude = []
