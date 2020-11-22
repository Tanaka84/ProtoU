from django.contrib import admin
from urania.models import Word, Voter, Vote

# Register your models here.
admin.site.register(Word)
admin.site.register(Voter)
admin.site.register(Vote)