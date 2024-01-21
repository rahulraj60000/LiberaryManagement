from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from .models import *
from .serializers import *

# Create your views here.


class BookDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, pk=None, format=None):


        if pk:
            book_obj = Book.objects.get(book_id=pk)
            serializer = BookSerializer(book_obj)
        else:
            book_objs = Book.objects.all()
            serializer = BookSerializer(book_objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        book_obj = Book.objects.get(book_id=pk)
        serializer = BookSerializer(book_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        book_obj = Book(request.data)

        serializer = BookSerializer(book_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, pk=None, format=None):

        if pk:
            book_obj = Member.objects.get(member_id=pk)
            serializer = MemberSerializer(book_obj)
        else:
            book_objs = Member.objects.all()
            serializer = MemberSerializer(book_objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):

        book_obj = Member(request.data)

        serializer = MemberSerializer(book_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AuthorDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, pk=None, format=None):

        if pk:
            author_obj = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author_obj)
        else:
            book_objs = Member.objects.all()
            serializer = MemberSerializer(book_objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):

        author_obj = Author(request.data)

        serializer = AuthorSerializer(author_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationService(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, pk=None, format=None):

        pass
    '''
    write login for fetching all the records of book , based on book_id who have borrowed 
    also based on member_id , how many book a specific member have borrowed
    '''


    def post(self, request):

        status, message, error_message = '', '', False,

        try:

            book_id = request.data.get("book_id", "")
            member_id = request.data.get("member_id", "")

            book_obj = Book.objects.get(book_id=book_id)
            member_obj = Member.objects.get(member_id=member_id)

            reservation_obj = ReservationService(
                book=book_obj,
                member=member_obj
            )

            reservation_obj.save()
            status = True
        except Exception as e:

            error_message = f"Error in ReservationDetails, error: {str(e)}"

            message = "Something went wrong, Please try Again"
        finally:

            response = {
                "status": status,
                "message": message,
                "error_message": error_message,
                "data": {}
            }

            return Response(response, status.HTTP_200_OK)


@api_view(['POST'])
def book_checkout(request, pk):
    status, message, error_message, status_code = '', '', False, 400

    data = {}
    try:


        book_id = request.data.get("book_id", "")
        member_id = request.data.get("member_id", "")

        book_obj = Book.objects.get(book_id=book_id)
        member_obj = Member.objects.get(member_id=member_id)

        if book_obj.no_of_copies > 0:

            book_obj.no_of_copies -= 1
            book_obj.save()

            checkout = BookCheckoutDetails.objects.create(book=book_obj, member=member_obj)
            serializer = CheckoutSerializer(checkout)
            data = serializer.data
            status_code = 200
            success = True
        else:
            message = 'No copies available for checkout'
            status_code = 401
            status = False

    except Exception as e:
        error_message = f"Error in book_checkout, error: {str(e)}"
        message = "Something went wrong, Please try again"

    finally:

        response = {
            "status": status,
            "status_code": status_code,
            "message": message,
            "error_message": error_message,
            "data": data
        }

        return Response(response, status.HTTP_200_OK)



@api_view(['GET'])
def member_overdue_books(request, pk):
    status, message, error_message, status_code = '', '', False, 400

    data = {}
    try:

        member_id = request.data.get("member_id", "")

        member_obj = Member.objects.get(member_id=member_id)

        overdue_checkouts = BookCheckoutDetails.objects.filter(member=member_obj, return_date__lt=datetime.now())
        total_fine = sum([(datetime.now() - overdue_checkouts.return_date).days * 50 for checkout in overdue_checkouts])
        data = {
            'overdue_books': CheckoutSerializer(overdue_checkouts, many=True).data,
            'total_fine': total_fine,
        }

        status_code = 200


    except Exception as e:
        error_message = f"Error in book_checkout, error: {str(e)}"
        message = "Something went wrong, Please try again"

    finally:

        response = {
            "status": status,
            "status_code": status_code,
            "message": message,
            "error_message": error_message,
            "data": data
        }

        return Response(response, status.HTTP_200_OK)



