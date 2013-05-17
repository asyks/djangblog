# Create your views here.

from django.http import HttpResponse
from blog.models import Authors, Posts

def index(request):
  return HttpResponse('Hello World!')

def authors(request):
  return HttpResponse('Authors Page')
"""
class AuthorsView(ListView):
  model = Authors

  def head(self, *args, **kwargs):
    response = HttpResponse('Hello World!')
    return response
"""
