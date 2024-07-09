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


class Doctor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    specialized_in = models.CharField(max_length=200, null=True, blank=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    prescription = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "doctor"
        order_by = ["-created_at"]


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    problem = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "patient"
        order_by = ["-created_at"]

