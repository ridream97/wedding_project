from django.db import models


class Block (models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return "%s %s" % (self.id, self.name)


class Album (models.Model):

    id_block = models.ForeignKey("prosite.Block")
    title = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='')


class Text (models.Model):
    id_block = models.ForeignKey("prosite.Block")
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return "%s %s %s" % (self.id, self.title, self.body)
