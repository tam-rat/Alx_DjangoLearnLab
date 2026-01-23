\# Retrieve a Book



```python

from bookshelf.models import Book



\# Retrieve all books

Book.objects.all()



\# Retrieve a specific book by title

Book.objects.get(title="1984")



