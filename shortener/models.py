from django.db import models


class Link(models.Model):
    full_link = models.URLField('Full_link')
    short_link = models.CharField('Short_link', max_length=20, null=True, blank=True)
    designed_link = models.CharField('Designed Link', max_length=20, null=True, blank=True, unique=True)
    count_use = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_link

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
