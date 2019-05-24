from django.contrib import admin

from .models import (
    Character,
    World

)

models = [Character, World]

for m in models:
    admin.site.register(m)