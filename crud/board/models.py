from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("제목", max_length=20, null=False)
    content = models.TextField("내용", null=False)