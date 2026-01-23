\# Update the title of the book

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()



\# Check the updated title

Book.objects.all()



