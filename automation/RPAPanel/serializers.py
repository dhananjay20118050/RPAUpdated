from django.conf import settings
from rest_framework import serializers
from RPAPanel.models import Nodes,Hubs
from rest_framework.validators import UniqueTogetherValidator

class NodeSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Nodes
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'updated_at', 'created_at','roleid')

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Nodes.objects.all(),
        #         fields=['name']
        #     )
        # ]


class HubSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Hubs
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'updated_at', 'created_at','roleid')

