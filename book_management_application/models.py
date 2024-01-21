from django.db import models

from rest_framework import serializers
from django.db import models

# Create your models here.

'''
entity - BOOK {

id: unique id Str
tile: str
author: Author 
}

here book and author have many to many relation

entity - Author 
{
id: Str(uuid)
name: Str
}

entity - Member 

{
id: uuid Str
name: str
}

reservation_service
{
id: str
book: Book
member: Member
borrow_date: DateTime

}

'''


class Author(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Author name: {self.name}"

    class Meta:
         app_level = "book_management_application"
         db_table = "author"


class Book(models.Model):
    id = models.BigIntegerField(primary_key=True)

    book_id = models.CharField(max_length=35, null=False, blank=False, db_index=True)
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.ManyToManyField(Author)
    no_of_copies = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Book Title: {self.title}"

    class Meta:
        app_level = "book_management_application"
        db_table = "book"


class Member(models.Model):
    id = models.BigIntegerField(primary_key=True)

    member_id = models.CharField(max_length=250, null=False, blank=False, db_index=True)
    name = models.CharField(max_length=250, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"member name: {self.name}"

    class Meta:
        app_level = "book_management_application"
        db_table = "Member"


class ReservationDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f": book: {self.book}, member: {self.member} borrow_date: {self.borrow_date}"

    class Meta:
        app_level = "book_management_application"
        db_table = "reservation_details"


class BookCheckoutDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_index=True)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    fine_paid = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"book checkout date : {self.borrow_date}"

    class Meta:
        app_level = "book_management_application"
        db_table = "book_checkout_details"

























