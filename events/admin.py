from django.contrib import admin
from events.models import Events,UserProfile,Comments,Contact

# Register your models here.
admin.site.register(Events)
admin.site.register(UserProfile)
admin.site.register(Comments)
admin.site.register(Contact)