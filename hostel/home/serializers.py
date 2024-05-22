from rest_framework import serializers
from . models import Hotel,Manager,Guest,Room,Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'hotel_location', 'hotel_contact', 'no_of_rooms',)

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('hotel_manager_name','manager_contact_no','hotel_manager_id','hotel_name',)

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('guest_name','guest_address','hotel_name','guest_contact',)

class RoomSerializer(serializers.ModelSerializer):
    class Meta :
        model = Room
        fields = ('room_number','hotel_name','max_guests','price','available',)

class BookingSerializer(serializers.ModelSerializer):
    hotel_name=HotelSerializer()
    hotel_manager_name=ManagerSerializer()
    guest_name=GuestSerializer()
    room_number=RoomSerializer()
    class Meta :
        model = Booking
        fields = ('hotel_name','hotel_manager_name','guest_name','room_number','log_in','log_out',)

class HotelSerializer(serializers.ModelSerializer):
    hotel_name=serializers.CharField(max_length=100)
    hotel_location=serializers.CharField(max_length=100)
    hotel_contact=serializers.IntegerField()
    no_of_rooms=serializers.IntegerField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hotel_name=validated_data.get('hotel',instance.hotel_name)
        instance.hotel_location=validated_data.get('hotel_location',instance.hotel_location)
