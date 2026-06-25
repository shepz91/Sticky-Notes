from django.db import models


class StickyNote(models.Model):
    """Core fields"""

    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()

    """Custom style field"""
    color = models.CharField(max_length=7, default="#FEF3C7")

    """Fields for sorting and tracking"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]  # Shows the most recently updated notes first

    def __str__(self):
        # Returns the title
        return self.title if self.title else f"Note: {self.content[:20]}..."
