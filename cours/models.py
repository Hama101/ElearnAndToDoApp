from django.db import models as m

# Create your models here.
class Course(m.Model):
    title = m.CharField(max_length=100)
    imgUrl = m.CharField(max_length=3083)
    ytUrl = m.CharField(max_length=3083)
    description = m.CharField(null=True ,max_length=255)
    done = m.BooleanField(default=False)

    def __str__(self):
        return self.title


class Item(m.Model):
    title = m.CharField(max_length=200)
    done = m.BooleanField(default=False)
    date = m.DateField(null=True, blank=True)
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title