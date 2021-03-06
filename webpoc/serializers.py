from django.db.models import fields
from rest_framework  import serializers
from .models import Login, Customer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['transactionID', 'transdate', 'cfname', 'clname', 'country', 'ccity', 'ptype', 'product', 'qty', 'amount']


