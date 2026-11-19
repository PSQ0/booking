from rest_framework import serializers


class ServiceOfferingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField()

    description = serializers.CharField()

    duration_minutes = serializers.IntegerField()

    price = serializers.IntegerField()

    is_active = serializers.BooleanField()

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("قیمت نمیتواند منفی باشد.")
        return value

    def validate_duration_minutes(self, value):
        if not 15 <= value <= 180:
            raise serializers.ValidationError(
                "مدت زمان خدمت باید بین 15 تا 180 دقیقه باشد"
            )
        return value


class ServicesSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration_minutes = serializers.IntegerField()