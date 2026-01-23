\# Create a Book



```python

from bookshelf.models import Book



\# Create a new book instance

book = Book(title="1984", author="George Orwell", publication\_year=1949)

book.save()



\# Check creation

Book.objects.all()





