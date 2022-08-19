from django.views.generic import TemplateView, DetailView, ListView
from green_life_coaching.models import Blog

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogListView(ListView):
    template_name = 'blogs.html'
    model = Blog
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog
    