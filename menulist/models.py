from audioop import reverse

from django.db import models
from django.http import Http404


# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    explicit_url = models.CharField(verbose_name='Path to the page', max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(verbose_name='URL for the function', max_length=100, blank=True, null=True, unique=True, help_text='Format: [django app]:[django view] [same URL as above]')

    def save(self, *args, **kwargs):
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_named_url = reverse(url_name, args=params)
            if self.explicit_url:
                if self.explicit_url != reversed_named_url:
                    raise Http404('explicit_url does not match named_url')
            else:
                self.explicit_url = reversed_named_url
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_parent_ids(self):
        if self.parent:
            return self.parent.get_parent_ids() + [self.parent.id]
        else:
            return []
