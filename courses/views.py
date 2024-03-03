from django.shortcuts import render
from courses.models import Video
from django.core.paginator import Paginator
# from datetime import timedelta
# from moviepy.editor import VideoFileClip

from .models import Course
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView
from .models import Course, Video

from django.db.models import Q  # For complex queries
# Create your views here.
def courses(request):
    return render (request, 'courses.html')
def userpage(request):
    courses = Course.objects.all()
    return render(request, 'userpage.html', {'courses': courses})
# def logout(request):
#     return render(request, "index.html")

# def playlist(request):
#     videos = Video.objects.all()
#     paginator = Paginator(videos,1)  # Show 10 videos per page.
    
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     playlist = []
#     for video in videos:
#         clip = VideoFileClip(video.file.path)
#         duration = clip.duration
#         playlist.append({'title': video.title, 'duration': duration})
#     return render(request, 'playlist.html', {'page_obj': page_obj, 'playlist': playlist})

# def playlistcss(request):
#     videos = CssVideos.objects.all()
#     paginator = Paginator(videos,1)  # Show 10 videos per page.
    
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     playlistcss = []
#     for video in videos:
#         clip = VideoFileClip(video.file.path)
#         duration = clip.duration
#         playlistcss.append({'title': video.title, 'duration': duration})
#     return render(request, 'playlistcss.html', {'page_obj_css': page_obj, 'playlistcss': playlistcss})

# def playlistjs(request):
#     videos = JsVideos.objects.all()
#     paginator = Paginator(videos,1)  # Show 10 videos per page.
    
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     playlistjs = []
#     for video in videos:
#         clip = VideoFileClip(video.file.path)
#         duration = clip.duration
#         playlistjs.append({'title': video.title, 'duration': duration})
#     return render(request, 'playlistjs.html', {'page_obj_js': page_obj, 'playlistjs': playlistjs})

# ### views for the analythics 
# @login_required
# def enroll_in_course(request, course_id):
#     course = Course.objects.get(id=course_id)
#     UserCourseProgress.objects.get_or_create(user=request.user, course=course)
#     return redirect('course_detail', course_id=course_id)

# @login_required
# def complete_lesson(request, course_id, lesson_id):
#     course_progress = UserCourseProgress.objects.get(user=request.user, course_id=course_id)
#     lesson = Lesson.objects.get(id=lesson_id)
#     course_progress.lessons_completed.add(lesson)
#     course_progress.save()
#     # Redirect to the next lesson or course overview
#     return redirect('course_detail', course_id=course_id)

# @login_required
# def generate_certificate(request, course_id):
#     course_progress = UserCourseProgress.objects.get(user=request.user, course_id=course_id)
#     if course_progress.progress_percentage == 100:
#         Certificate.objects.get_or_create(user=request.user, course_id=course_id)
#         # Redirect to a page where the user can view/download the certificate
#         return redirect('certificate_page', course_id=course_id)
#     else:
#         # Handle the case where the user hasn't completed the course
#         return redirect('course_detail', course_id=course_id)

### courses and videos viewing 
class CourseListView(ListView):
    model = Course
    template_name = 'courses.html'  # Your template path
    context_object_name = 'courses'

# class CourseView(ListView):
#     model = Course
#     template_name = 'userpage.html'  # Your template path
#     context_object_name = 'courses'


# course details
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'  # Your template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['course_title'] = course.title
        context['course_description'] = course.description
        
        return context


# course video viewer
class CourseDashboardView(DetailView):
    model = Course
    template_name = 'video_viewer.html'  # Your template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(course=self.get_object())
        return context


#search function
class SearchView(ListView):
    model = Course
    template_name = 'courses/course_list.html'  # Your template path
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')  # Get the search parameter from the URL
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        return queryset

