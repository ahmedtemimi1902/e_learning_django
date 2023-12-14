# serializers.py

from rest_framework import serializers
from authentification.models import Course, Material, Assignment, ReadingState

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ReadingStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingState
        fields = '__all__'
