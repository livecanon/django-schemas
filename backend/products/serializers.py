from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "content", "price", "id"]


# An example that shows what we can do with serializers.Serializer :)
class MockSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=20, decimal_places=2)

    def validate_price(self, value):
        """
        Check if the price is >= 0
        """

        if value < 0:
            raise serializers.ValidationError("Price cannot be a negative number.")
        return value

    # We also have the access to the validate() method
    # which can be usefull when we need to access multiple
    # fields at once.

    #    def validate(self, data):
    #       # check the data, is sth is wrong then return ValidationError
    #       retrun data
