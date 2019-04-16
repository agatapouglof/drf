from django.contrib import admin
from .models import GCAAffaire, GCAClient, GCAContact
#ajout des modèles dans la vue admin

admin.site.register(GCAAffaire)
admin.site.register(GCAClient)
admin.site.register(GCAContact)
