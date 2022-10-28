from django.contrib import admin

# Register your models here.
from .models import Category, Post ,Comments

class CommentItemInline(admin.TabularInline):
    model = Comments
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields =['title','intro','body']
    list_display =['title','slug','category','created_at','status']
    list_filter =['category','created_at','status']
    inlines =[CommentItemInline]
    prepopulated_fields ={'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields =['title']
    list_display =['title']
    prepopulated_fields ={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post','created_at']


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comments,CommentAdmin)