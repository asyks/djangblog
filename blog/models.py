from django.db import models
from datetime import datetime

class Authors(models.Model):

  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  dob = models.DateField()

  def write_one(self, f, l, d):
    d = datetime.strptime(d, '%Y-%m-%d')
    author = self(firstname=f, lastname=l, dob=d)
    author.save()

  def read_by_name(self, n):
    first, last = n.split(' ')
    try:
      author = self.objects.get(firstname=first)
      if author.lastname == last:
        return author
    except DoesNotExist:
      return None

  def read_by_id(self, i):
    try:
      author = self.objects.get(id=i) 
      return author
    except:
      return None

  def read_all(self):
    try:
      authors = self.objects.all()
      return authors
    except:
      return None

class Posts(models.Model):

  title = models.CharField(max_length=200)
  content = models.TextField()
  publishdate = models.DateTimeField()
  author = models.ForeignKey(Authors)

  def write_one(self, t, c, a):
    p = datetime.utcnow()
    a = Authors.read_by_name(a) or 'anon'
    posts = self(title=t, content=c, publishdate=p, author=a)
    posts.save()

  def modify(self, t, c, a, i):
    p = datetime.utcnow()
    a = Authors.read_by_name(a) or 'anon'
    posts = self(title=t, content=c, publishdate=p, author=a, id=i)
    posts.save()
    pass

  def read_by_title(self, t):
    try:
      post = self.objects.get(title=t)
      return post
    except:
      return None

  def read_by_id(self, i):
    try:
      post = self.objects.get(id=i)
      return post
    except:
      return None

  def read_all(self):
    try:
      posts = self.objects.all()
      return posts
    except:
      return None
