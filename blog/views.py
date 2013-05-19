from django.http import HttpResponse, HttpRequest
from blog.models import Authors, Posts
import json, logging

def index(request):
  request = HttpRequest.body
  response = HttpResponse(content='Hello World!', content_type='text/html; charset=utf-8')
  return response

def listAllAuthors(request):
  allAuthors = Authors.read_all()
  allAuthors = [{'firstname':a.firstname,'lastname':a.lastname,'dob':a.dob.strftime('%Y-%m-%d')} for a in allAuthors]
  authorsJson = json.dumps(allAuthors, sort_keys=True, indent=4, separators=(',', ': '))
  response = HttpResponse(content=authorsJson, content_type='application/json; charset=utf-8')
  return response

def listAllPosts(request):
	## procedure for listing all blog posts
  pass

def listPost(request):
	## procedure for returning details of a post
  pass

def createPost(request):
  ## procedure for creating a new blog post
  request = HttpRequest.body
  pass

def createPost(request):
  ## procedure for creating a new blog post
  request = HttpRequest.body
  pass

def deletePost(request):
  ## procedure for deleting a blog post
  request = HttpRequest.body
  pass

def modifyPost(request):
  ## procedure for modiftying a blog post
  request = HttpRequest.body
  pass

def createAuthor(request):
  ## procedure for creating a new author
  p = request.POST
  logging.warning(p)
  return HttpResponse('Ok')

def listAuthor(request):
  ## procedure for returning details of an author
  pass

## returning json
##jsonContent = 'application/json; charset=utf-8'
##json.dumps(object, sort_keys=True, indent=4, seperators=(',', ': '))

## getting json from request body
## HttpRequest.body
"""
class AuthorsView(ListView):
  model = Authors

  def head(self, *args, **kwargs):
    response = HttpResponse('Hello World!')
    return response
"""
