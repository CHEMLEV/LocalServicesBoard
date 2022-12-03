from django.contrib import admin
from .models import Classified, Review


class ReviewInline(admin.TabularInline):  # new
    model = Review


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]


admin.site.register(Classified)
admin.site.register(Review)





