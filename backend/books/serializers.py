from rest_framework import serializers
from .models import Book, Subject, Year

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'name', 'order']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

class BookSerializer(serializers.ModelSerializer):
    year_name = serializers.CharField(source='year.name', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    file_size_mb = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'year', 'year_name', 
            'subject', 'subject_name', 'description', 'pdf_file', 
            'thumbnail', 'is_public', 'upload_date', 'file_size_mb'
        ]

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'year', 'subject', 
            'description', 'pdf_file', 'thumbnail', 'is_public'
        ]