from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.

    Allows rich text editing of the content field using Summernote.
    """

    summernote_fields = ('content',)



@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing collaboration requests.

    Displays the message and read status of each request.
    Allows filtering by read status and searching through messages.
    """

    list_display = ('message', 'read',)
