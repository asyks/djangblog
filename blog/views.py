from django.http import HttpResponse, HttpRequest
from blog.models import Authors, Posts
from django.template import loader, Context
from django.views.decorators.http import require_http_methods
import json, logging

def index(request):
  request = HttpRequest.body
  template = loader.get_template('index.html')
  c = Context({})
  response = HttpResponse(content=template.render(c), content_type='text/html; charset=utf-8')
  return response

def listAllAuthors(request):
  allAuthors = Authors.read_all()
  allAuthors = [{'firstname':a.firstname,'lastname':a.lastname,'dob':a.dob.strftime('%Y-%m-%d'),'id':a.id} for a in allAuthors]
  authorsJson = json.dumps(allAuthors, sort_keys=True, indent=4, separators=(',', ': '))
  response = HttpResponse(content=authorsJson, content_type='application/json; charset=utf-8')
  return response

def listAuthor(request):
  body = request.body
  try: 
    body = json.loads(body)
    a = Authors.read_by_id(int(body.get('id'))) or {}
    author = {'firstname':a.firstname,'lastname':a.lastname,'dob':a.dob.strftime('%Y-%m-%d'),'id':a.id}
  except:
    author = {} 
  authorJson = json.dumps(author, sort_keys=True, indent=4, separators=(',', ': '))
  response = HttpResponse(content=authorJson, content_type='application/json; charset=utf-8')
  return response

def createAuthor(request):
  body = request.body
  body = json.loads(body)
  Authors.write_one(f=body.get('firstname'),
    l=body.get('lastname'),d=body.get('dob'))
  return HttpResponse('OK')

def listAllPosts(request):
  allPosts = Posts.read_all()
  allPosts = [{'title':p.title,'content':p.content,'publishdate':p.publishdate.strftime('%Y-%m-%d'),'author':p.author.id,'id':p.id} for p in allPosts]
  postsJson = json.dumps(allPosts, sort_keys=True, indent=4, separators=(',', ': '))
  response = HttpResponse(content=postsJson, content_type='application/json; charset=utf-8')
  return response

def listPost(request):
  body = request.body
  try: 
    body = json.loads(body)
    p = Posts.read_by_id(int(body.get('id'))) or {}
    post = {'title':p.title,'content':p.content,'publishdate':p.publishdate.strftime('%Y-%m-%d'),'author':p.author.id,'id':p.id}
  except:
    post = {} 
  postJson = json.dumps(post, sort_keys=True, indent=4, separators=(',', ': '))
  response = HttpResponse(content=postJson, content_type='application/json; charset=utf-8')
  return response

def createPost(request):
  body = request.body
  body = json.loads(body)
  Posts.write_one(t=body.get('title'),
    c=body.get('content'), a=body.get('author'))
  return HttpResponse('OK')

def modifyPost(request):
  body = request.body
  body = json.loads(body)
  Posts.write_one(t=body.get('title'), c=body.get('content'), 
    a=body.get('author'), i=body.get('id'))
  return HttpResponse('OK')

def deletePost(request):
  body = request.body
  body = json.loads(body)
  Posts.delete_one(body.get('id'))
  return HttpResponse('OK')
