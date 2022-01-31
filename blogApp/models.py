from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
 
class Tag(models.Model):
    caption  = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption



class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image_name = models.CharField(max_length=100, blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)
    slug =  models.SlugField(unique=True)
    content = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)

    
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    subTitle = models.CharField(max_length=100, blank = True)
    text = models.CharField(max_length=500, blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_email = models.EmailField(max_length=100, blank=True)
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.subTitle}'

