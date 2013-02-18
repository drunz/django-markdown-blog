from quotes.models import Quote
from django.contrib import admin

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author')
    list_filter = ('author',)
    search_fields = ['text', 'author']

admin.site.register(Quote, QuoteAdmin)

