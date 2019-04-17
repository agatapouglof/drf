from django.contrib import admin
from .models import GCAAffaire, GCAClient, GCAContact, GCAUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# ajout des modèles dans la vue admin

admin.site.register(GCAAffaire)
admin.site.register(GCAClient)
admin.site.register(GCAContact)


class GCAUserAdmin(UserAdmin):
    model = GCAUser
    list_display = ['email', 'username', 'code']

admin.site.register(GCAUser, GCAUserAdmin)
