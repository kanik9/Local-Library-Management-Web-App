from django.contrib import admin
from .models import Genre, Book, BookInstance, Author

# Register your models here.

class BookInstanceInline(admin.TabularInline):
    model = BookInstance


#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]





#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name' , ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

class GenreAdmin(admin.ModelAdmin):
    pass


#admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None,{
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
         'fields': ('status', 'due_back')
        }),
    )



