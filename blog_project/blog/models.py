from django.db import models
from users.models import CustomUser


# Create your models here.
class Writer(CustomUser):
    name = models.CharField(
        max_length=255,
        default="",
        null=False,
        blank=False
    )
    is_editor = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending Approval"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    written_by = models.ForeignKey(
        Writer, on_delete=models.CASCADE, related_name="articles_written"
    )
    edited_by = models.ForeignKey(
        Writer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="articles_edited",
    )

    def __str__(self):
        return self.title

    def can_edit(self, user):
        return self.satus == self.PENDING and user.writer.is_editor
