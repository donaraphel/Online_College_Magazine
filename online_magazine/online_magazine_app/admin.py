
# Register your models here.
from django.contrib import admin
from .models import UserDetails, Category, Article, Comment, UserLike

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserLike)