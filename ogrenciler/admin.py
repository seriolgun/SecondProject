from django.contrib import admin
#models.py dosyasında oluşturulan modelleri admin panelinde göstermek için kullanılan dosya
from .models import *
# Register your models here.
admin.site.register(Ogrenci)
