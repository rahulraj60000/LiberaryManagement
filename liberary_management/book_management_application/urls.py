from django.urls import path
from .views import *

urlpatterns = [
    path('book_details/<int:pk>/', BookDetails.as_view(), name="BookDetails"),
    path('member_details/<int:pk>/', MemberDetails.as_view(), name="MemberDetails"),
    path('author_details/<int:pk>/', AuthorDetails.as_view(), name="AuthorDetails"),
    path('reservation_service/', ReservationService.as_view(), name="ReservationService"),
    path('book_checkout/', book_checkout, name="book_checkout"),
    path('member_overdue_books/', member_overdue_books, name="member_overdue_books")

]