\# Delete the book instance

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()



\# Confirm deletion

Book.objects.all()  # This should return an empty queryset



