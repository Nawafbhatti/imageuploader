from django.db import models


class uploadimg(models.Model):
    picture = models.FileField(upload_to='newupload/')