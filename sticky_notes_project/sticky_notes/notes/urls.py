from django.urls import path
from . import views

urlpatterns = [
    # Home page lists all notes
    path("", views.note_list, name="note_list"),
    # Create page adds a new note
    path("create/", views.note_create, name="note_create"),
    # Update page edits a specific note
    path("update/<int:pk>/", views.note_update, name="note_update"),
    # Delete page removes a specific
    path("delete/<int:pk>/", views.note_delete, name="note_delete"),
]
