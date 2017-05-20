from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def list_of_articles(self):
        return self.objects.all()

class Article(models.Model):

    article_author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    comment_author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=300)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Comment to " + self.article.title + " by " + self.comment_author.name