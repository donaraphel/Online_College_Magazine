from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Model for Article Categories
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Model for Articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)

    def __str__(self):
        return self.title

# Model for Comments on Articles
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserDetails(models.Model):
    username = models.CharField(max_length=100, unique=True)
    user_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    bio = models.TextField(max_length=250)

    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        # Use Django's make_password to hash the password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        if(self.password == raw_password):
            return True

# Model for User Likes
class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)