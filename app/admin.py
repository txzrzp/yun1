from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link
# Register your models here.

admin.site.site_header = '云计算实验室管理后台'
admin.site.site_title = '云计算'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')
    # 搜索框
    search_fields = ['title']
    # fk_fields 设置显示外键字段
    fk_fields = ['category']
    list_filter = ['user']  # 右侧栏过滤器，按作者进行筛选
    date_hierarchy = 'created_time'  # 详细时间分层筛选　

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')