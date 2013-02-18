from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'edited')
    list_filter = ('author',)
    search_fields = ['title', 'author', 'text']
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(MyModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(Post, PostAdmin)
