from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# class Video(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     file = models.FileField(upload_to='videos/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
# class CssVideos(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     file = models.FileField(upload_to='videos/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class JsVideos(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     file = models.FileField(upload_to='videos/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    

# ### backend for course cretification
# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()

# class Lesson(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     content = models.TextField()

# class UserCourseProgress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     lessons_completed = models.ManyToManyField(Lesson, blank=True)

#     @property
#     def progress_percentage(self):
#         total_lessons = self.course.lesson_set.count()
#         completed_lessons = self.lessons_completed.count()
#         return (completed_lessons / total_lessons) * 100 if total_lessons > 0 else 0

# class Certificate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     issued_date = models.DateTimeField(auto_now_add=True)



## courses model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')  # Ensure you have Pillow installed

    def __str__(self):
        return self.title

# videos model 
class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='course_videos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
