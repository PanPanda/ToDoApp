from django.contrib import admin
from ToDoApp.models import Todo

class TodoAdmin(admin.ModelAdmin):
	"""docstring for TodoAdmin"""
	list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
	list_filter = ('pubtime',)
	ordering = ('-pubtime',)

admin.site.register(Todo, TodoAdmin)