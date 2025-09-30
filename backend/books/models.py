from django.db import models
from django.core.validators import FileExtensionValidator

class Year(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='books')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(blank=True)
    pdf_file = models.FileField(
        upload_to='books/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    is_public = models.BooleanField(default=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(default=0)  # in bytes
    
    class Meta:
        ordering = ['-upload_date']
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        if self.pdf_file:
            self.file_size = self.pdf_file.size
        super().save(*args, **kwargs)
    
    @property
    def file_size_mb(self):
        return round(self.file_size / (1024 * 1024), 2)