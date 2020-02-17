from django.contrib import admin
from .models import sports
from .models import match
from .models import comment
from .models import readmore

admin.site.register(sports)
admin.site.register(match)
admin. site.register(comment)
admin. site.register(readmore)

# Register your models here.
