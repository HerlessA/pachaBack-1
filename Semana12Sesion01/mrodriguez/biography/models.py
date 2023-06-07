from django.db import models
from django.utils import timezone


# Create your models here.
class Biography(models.Model):
    id = models.AutoField(primary_key=True)
    birth_name = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.ForeignKey(
        "biography.Nationality", on_delete=models.CASCADE
    )  # biograpy_nationality
    religion = models.CharField(max_length=200)
    study_center = models.TextField()
    career = models.TextField()
    website = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    # def publish(self):
    #     self.published_date = timezone.now
    #     self.save()

    def __str__(self):
        return str(self.id)


class Nationality(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country
