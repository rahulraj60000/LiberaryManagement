from rest_framework import serializers

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['id', ]

        def validate(self, data):
            pass


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ['id', ]

        def validate(self, data):
            pass


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        def validate(self, data):
            pass


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCheckoutDetails
        fields = '__all__'

        def validate(self, data):
            pass


class ReservationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationDetails
        fields = '__all__'

        def validate(self, data):
            pass