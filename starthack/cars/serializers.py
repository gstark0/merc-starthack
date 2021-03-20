from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    image = serializers.CharField()
    

class OtherInputSerializer(serializers.Serializer):
    type_of_car = serializers.CharField()

class OutputSerializer(serializers.Serializer):
	string = serializers.CharField()
	image_url = serializers.URLField()
	sound_url = serializers.URLField()
    