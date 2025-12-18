from django.contrib import admin
from users.models import *

admin.site.register (User)
admin.site.register (Admin)
admin.site.register (Staff)
admin.site.register (Client)
admin.site.register (Wallet)