from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ToDO'
        ordering = ['-id']

    def __str__(self):
        return self.title



