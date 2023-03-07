from django.contrib import admin

from .models import Caakes
from .models import Cookies

#adding id to caakes variable'
class CaakesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Caakes, CaakesAdmin)

admin.site.register(Cookies)
