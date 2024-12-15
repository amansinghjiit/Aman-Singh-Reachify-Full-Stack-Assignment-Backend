from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be greater than 0")
            return value

        def validate_quantity(self, value):
            if value < 0:
                raise serializers.ValidationError("Quantity can't be less than 0")
            return value
