from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm


def note_list(request):
    """View all notes and create the initial blank form"""
    
    notes = StickyNote.objects.all()
    form = StickyNoteForm()  # Empty form ready for creation
    return render(request, "notes/note_list.html", {"notes": notes, "form": form})


def note_create(request):
    """Save a new sticky note"""

    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("note_list")


def note_update(request, pk):
    """Edit an existing note"""
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = StickyNoteForm(instance=note)  # Pre-fill form with existing note

    return render(request, "notes/note_edit.html", {"form": form, "note": note})


def note_delete(request, pk):
    """Remove a note"""
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        note.delete()
    return redirect("note_list")
