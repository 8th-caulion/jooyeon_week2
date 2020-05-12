from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Travel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default=timezone.now)
    body = models.TextField() 

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]   

class Comment(models.Model):
    post = models.ForeignKey('travel.Travel', on_delete=models.CASCADE, related_name='comments')
    #  글쓸때처럼 자기 아이디 뜨게 할수는 없나??
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
        