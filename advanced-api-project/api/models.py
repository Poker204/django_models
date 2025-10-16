from django.db import models

# Author model stores author names
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


# Book model stores title, publication year, and linked author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.PositiveIntegerField()  # Year of publication
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # One-to-many link: Author → Books

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
