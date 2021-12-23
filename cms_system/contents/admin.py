from django.contrib import admin
from .models import Contents, Theme, Detail_Theme, Content_Like, Content_Comment
from .models import Contents_Description

# Register your models here.
admin.site.register(Contents)
admin.site.register(Theme)
admin.site.register(Detail_Theme)
admin.site.register(Content_Like)
admin.site.register(Content_Comment)
admin.site.register(Contents_Description)

