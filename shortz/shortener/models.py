from django.db import models
from django.core.validators import URLValidator


class URLEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    full_url = models.URLField(validators=[URLValidator()])
    code = models.CharField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "URL entries"
        verbose_name = "URL entry"

    def __str__(self):
        return "URLEntry: code={code}, full_url={full_url}".format(code=self.code, full_url=self.full_url)
