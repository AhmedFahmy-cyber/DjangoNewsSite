from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    cat_img = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class News(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/')
    detail = models.TextField(max_length=400)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("allnews")

    def get_detail_url(self):
        return reverse("main:detail" ,args=[str(self.id)])
    
    def get_category_url(self):
        return reverse("main:category" ,args=[str(self.id)])
      

class Comment(models.Model):
    name =models.CharField(max_length=200)
    news = models.ForeignKey(News , on_delete=models.CASCADE) 
    email = models.CharField(max_length=200)
    comment=  models.TextField(max_length=400)
    status = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
    
