from django.contrib import admin

from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn__exact', 'publisher__name__startswith')

def initialled_name(obj):
    """
    obj.first_names='Jerome David', obj.last_names='Salinger' => 'Salinger, JD'
    """
    initials = '. '.join([name[0] for name in obj.first_names.split(" ")])+'.'
    return f"{obj.last_names}, {initials}"

class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)

class ReviewAdmin(admin.ModelAdmin):
    #exclude = ('date_edited')
    #fields = ('content', 'rating', 'creator', 'book')
    #fieldsets = (('Linkage', {'fields': ('creator', 'book')}), ('Review content', {'fields': ('content', 'rating')}))
    fieldsets = ((None, {'fields': ('creator', 'book')}), ('Review content', {'fields': ('content', 'rating')}))


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)


