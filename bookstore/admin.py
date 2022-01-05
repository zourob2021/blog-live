from django.contrib import admin

# Register your models here.


from.models import Tag, book, customer, order

admin.site.register(customer)

admin.site.register(order)

admin.site.register(book)

admin.site.register(Tag)