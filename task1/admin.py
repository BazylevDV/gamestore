from django.contrib import admin
from .models import Buyer,Game # импортируем обе модели




admin.site.register(Buyer)
admin.site.register(Game)