from django.db import models
from django.utils import timezone
from django.urls import reverse
from tinymce import models as tmce_models
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    content = tmce_models.HTMLField(default='N/A')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #photo
    photo = models.ImageField(upload_to='', default='../img/controller.jpg')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list') #after comment submitted, return to list of posts
                                    #maybe change to return to post that was commented on instead

    def __str__(self):
        return self.text
