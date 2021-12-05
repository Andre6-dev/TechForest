from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Planes)
admin.site.register(Pagos)
admin.site.register(Usuarios)
admin.site.register(Errores)
admin.site.register(Diapositivos)
admin.site.register(Opciones)
admin.site.register(Administradores)
admin.site.register(Valvula)