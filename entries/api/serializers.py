import datetime
from rest_framework import serializers
from dataclasses import dataclass
from entries.models import  EntryModel


class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.DateTimeField()

    def create(self, validated_data):

        instance = EntryModel(
            datetime = validated_data.get('datetime'),
            concept = validated_data.get('concept'),
            amount = validated_data.get('amount')
        )

        instance.save()
        return instance


    def update(self, instance, validated_data):
        instance.datetime = validated_data.get('datetime')
        instance.amount = validated_data.get('amount')
        instance.concept = validated_data.get('concept')
        instance.save()
        return instance


    def validate_datetime(self, data):
        entry = EntryModel.objects.filter(datetime=data)
        if entry > datetime.today():      
            if self.instance is not None and self.instance.datetime != data: 
                raise serializers.ValidationError("La fecha tiene que ser anterior a hoy")
        return data


    def validate_amount(self, data):
        entry = EntryModel.objects.filter(amount=data)
        if  entry == 0:
            if self.instance is not None and self.instance.amount != data: 
                raise serializers.validate_error("Error : Cantidad no puede ser 0")
        return data