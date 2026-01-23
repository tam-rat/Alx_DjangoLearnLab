from django.contrib import admin
from .models import Book  # Import the Book model

# Customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')                     # Add search functionality
    list_filter = ('publication_year',)                    # Filter by publication year

# Register the model with the admin site
admin.site.register(Book, BookAdmin)
