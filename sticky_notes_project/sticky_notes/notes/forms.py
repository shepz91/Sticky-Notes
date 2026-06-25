from django import forms
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    """
    Form for creating and updating StickyNotes
    """

    class Meta:
        model = StickyNote
        fields = ["title", "content", "color"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control note-title-input mb-2",
                    "placeholder": "Title (Optional)...",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control note-content-input mb-2",
                    "placeholder": "Take a note...",
                    "rows": 4,
                }
            ),
            # Changed from forms.Input to forms.TextInput here:
            "color": forms.TextInput(
                attrs={
                    "type": "color",
                    "class": "form-control form-control-color note-color-picker",
                }
            ),
        }
