from django.db import models

# Create your models here.


class BookType(models.Model):
    type_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.type_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=50)
    type = models.ForeignKey(BookType)

    def __unicode__(self):
        return "title=%s, pub_date=%s, author=%s, type=%s" % (self.title, self.pub_date, self.author, self.type)


class Recommend(models.Model):
    book_id = models.ForeignKey(Book)