from django.db import models

length_50 = 50
length_100 = 100
length_255 = 255
max_lenght_1000 = 100

class Class(models.Model):
    class_no = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=length_50) 

    def __str__(self) -> str:
        return self.title
    

class Course(models.Model):
    title = models.CharField(max_length=length_100)
    code = models.CharField(max_length=length_50)
    class_id = models.ForeignKey(Class, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=length_100)
    no = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title

class User(models.Model):
    TYPE_STUDENT = 'S'
    TYPE_TEACHER = 'T'
    TYPE_ADMIN = 'A'

    TYPE_CHOICES = [
        (TYPE_STUDENT, 'Student'),
        (TYPE_TEACHER, 'Teacher'),
        (TYPE_ADMIN, 'Admin')
    ]

    name = models.CharField(max_length=length_100)
    age = models.SmallIntegerField()
    email = models.EmailField(max_length=length_255)
    password = models.CharField(max_length=max_lenght_1000)
    phone = models.CharField(max_length=length_50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

# https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    total_question = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    # def __str__(self) -> str:
    #     return self.user.name


class Question(models.Model):
    description = models.TextField(null=True)
    first_option = models.CharField(max_length=255)
    second_option = models.CharField(max_length=255)
    third_option = models.CharField(max_length=255)
    fourth_option = models.CharField(max_length=255)
    answer = models.PositiveSmallIntegerField()
    explanation = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    class_no = models.ForeignKey(Class, on_delete=models.PROTECT, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.PROTECT, null=True)
    points = models.PositiveBigIntegerField(default=0) # 0 to 2,147,483,647



    # admin string representation
    def __str__(self) -> str:
        return self.description # this will present the description of the question
        #in admin section

    # for sorting we declare a class called meta
    class Meta:
        ordering = ['description']


class Set(models.Model):
    total_questions = models.PositiveIntegerField()#check the maximum value
    total_marks = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)

class QuestionInExam(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    set = models.ForeignKey(Set, on_delete=models.PROTECT)

class Review(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
