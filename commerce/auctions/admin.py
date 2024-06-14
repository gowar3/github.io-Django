from django.contrib import admin

from .models import Listing, Bid, Comment

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "description", "price")

class BidAdmin(admin.ModelAdmin):
    list_display = ("owner", "offer")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "comments")


admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
