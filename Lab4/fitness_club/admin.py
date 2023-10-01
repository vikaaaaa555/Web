from django.contrib import admin
from .models import *


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Instructor, InstructorAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'phone_number')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Client, ClientAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'capacity')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Group, GroupAdmin)

admin.site.register(Lesson)
admin.site.register(Payment)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Membership, MembershipAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Coupon, CouponAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'last_name', 'rating', 'feedback', 'time_create')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user', 'rating')


admin.site.register(Feedback, FeedbackAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)


class VocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'vocation', 'description')
    list_display_links = ('id', 'vocation')
    search_fields = ('vocation',)


admin.site.register(Vocation, VocationAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(FAQ, FAQAdmin)
