from django.db import models
from datetime import datetime

class Authors(models.Model):

  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  dob = models.DateField()

  @classmethod
  def write_one(cls, f, l, d):
    d = datetime.strptime(d, '%Y-%m-%d')
    author = cls(firstname=f, lastname=l, dob=d)
    author.save()

  @classmethod
  def read_by_name(cls, n):
    first, last = n.split(' ')
    try:
      author = cls.objects.get(firstname=first)
      if author.lastname == last:
        return author
    except DoesNotExist:
      return None

  @classmethod
  def read_by_id(cls, i):
    try:
      author = cls.objects.get(id=i) 
      return author
    except:
      return None

  @classmethod
  def read_all(cls):
    try:
      authors = cls.objects.all()
      return authors
    except:
      return None

class Posts(models.Model):

  title = models.CharField(max_length=200)
  content = models.TextField()
  publishdate = models.DateTimeField()
  author = models.ForeignKey(Authors)

  @classmethod
  def write_one(cls, t, c, a):
    p = datetime.utcnow()
    a = Authors.read_by_name(a) or Authors.read_by_id(1)
    post = cls(title=t, content=c, publishdate=p, author=a)
    post.save()

  @classmethod
  def modify(cls, t, c, a, i):
    p = datetime.utcnow()
    a = Authors.read_by_name(a) or Authors.read_by_id(1)
    post = cls(title=t, content=c, publishdate=p, author=a, id=i)
    post.save()

  @classmethod
  def read_by_title(cls, t):
    try:
      post = cls.objects.get(title=t)
      return post
    except:
      return None

  @classmethod
  def read_by_id(cls, i):
    try:
      post = cls.objects.get(id=i)
      return post
    except:
      return None

  @classmethod
  def read_all(cls):
    try:
      posts = cls.objects.all()
      return posts
    except:
      return None

  @classmethod
  def delete_one(cls, i):
    try:
      post = cls.objects.get(id=i)
      post.delete()
      return True
    except:
      return False
