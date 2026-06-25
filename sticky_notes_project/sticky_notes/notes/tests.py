from django.test import TestCase
from django.urls import reverse
from .models import StickyNote


class StickyNoteViewCRUDTest(TestCase):

    def setUp(self):
        """Creates an initial sticky note to use for Read, Update, and Delete tests."""
        self.note = StickyNote.objects.create(
            title="Initial Note", content="This is the starting content."
        )

    """ test note list """

    def test_note_list_view(self):
        """Verifies the list view loads and displays existing notes."""
        response = self.client.get(reverse("note_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")
        # Check if the text from our setUp note is actually in the HTML response
        self.assertContains(response, "Initial Note")

    """ test note creation """

    def test_note_create_view(self):
        """Verifies a POST request to note_create saves a note and redirects."""
        # change database count from 1 to 2
        response = self.client.post(
            reverse("note_create"),
            data={
                "title": "New Web Note",
                "content": "Created via a POST request form submission.",
                "color": "#FEF3C7",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))
        self.assertEqual(StickyNote.objects.count(), 2)
        self.assertTrue(StickyNote.objects.filter(title="New Web Note").exists())

    """ test update note """

    def test_note_update_view(self):
        """Verifies a POST request to note_update changes the note details."""
        response = self.client.post(
            reverse("note_update", kwargs={"pk": self.note.pk}),
            data={
                "title": "Updated Title Name",
                "content": "The content has changed successfully.",
                "color": "#3B82F6",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))

        # Reload the note from the database to verify the updates
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title Name")
        self.assertEqual(self.note.content, "The content has changed successfully.")

    """ test note deletion """

    def test_note_delete_view(self):
        """Verifies a POST request to note_delete removes the record."""
        response = self.client.post(reverse("note_delete", kwargs={"pk": self.note.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("note_list"))

        # Database count should drop from 1 back to 0
        self.assertEqual(StickyNote.objects.count(), 0)
