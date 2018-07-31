import base64
from hashlib import md5

from django.db import models
from django.core.validators import URLValidator

from shortz import settings

class URLEntry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(validators=[URLValidator()])
    code = models.CharField(primary_key=True, max_length=200, unique=True, blank=True)
    shortened_url = models.URLField(validators=[URLValidator()], blank=True)

    class Meta:
        verbose_name_plural = "URL entries"
        verbose_name = "URL entry"

    def __str__(self):
        return "URLEntry: code={code}, full_url={full_url}".format(code=self.code, full_url=self.url)

    def _shortcode(self, url):
        """Based on: https://pypi.org/project/url_shortener/"""

        digest = md5(url.encode('utf-8')).digest()
        b64enc =  base64.b64encode(digest)
        return b64enc.replace(b'=',b'').replace(b'/', b'_')

    def save(self, *args, **kwargs):
        shortcode = self._shortcode(self.url).decode('utf-8')
        self.code = shortcode
        self.shortened_url = '{}{}'.format(settings.DEV_HOST, shortcode)
        super().save(*args, **kwargs)
