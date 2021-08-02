from django.db import models



class BooksCategory(models.Model):
    """A category class for books"""
    name = models.CharField(max_length=100)

class Books(models.Model):
    """ A book class representation"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(BooksCategory, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    