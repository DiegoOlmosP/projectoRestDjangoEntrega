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
        pass