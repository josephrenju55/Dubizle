from django.contrib import admin
from . models import Hotel, Manager, Guest, Room, Booking
from django import forms

# Register your models here.


class HotelAdmin(admin.ModelAdmin):
     list_display = ( 'hotel_name', 'hotel_location', 'hotel_contact','no_of_rooms',)
    # form=HotelAdminForm


class ManagerAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ManagerAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        mananger_contact_no=self.cleaned_data.get("max_guests")
        if len(mananger_contact_no) >= 10:
            raise forms.ValidationError("Maximum number of guests can only be 3")
        return self.cleaned_data
    
    
    def save(self, commit=True):
        return super(ManagerAdminForm,self).save(commit=commit)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('hotel_manager_name', 'manager_contact_no', 'hotel_manager_id', 'hotel_name',)
    # form=ManagerAdminForm
#
#
class GuestAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(GuestAdminForm,self).__init__(*args,**kwargs)
    
    def clean(self):
        guest_contact=self.cleaned_data.get('guest_contact')
        if len(guest_contact) >= 10:
            raise forms.ValidationError('Unvalid contact number')
        return self.cleaned_data
    
    def save(self, commit=True):
        return super(GuestAdminForm,self).save(commit=commit)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'guest_address', 'hotel_name', 'guest_contact',)
    # form=GuestAdminForm

class RoomAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(RoomAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        max_guests=self.cleaned_data.get("max_guests")
        if max_guests >= 4:
            raise forms.ValidationError("Maximum number of guests can only be 3")
        return self.cleaned_data


    def save(self, commit=True):
        return super(RoomAdminForm,self).save(commit=commit)

#
class RoomAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(RoomAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        room_number=self.cleaned_data.get("room_number")
        if room_number :
            raise forms.ValidationError("Room Unavailable")
        return self.cleaned_data


    def save(self, commit=True):
        return super(RoomAdminForm,self).save(commit=commit)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel_name', 'max_guests', 'price', 'available',)
    form=RoomAdminForm

class BookingAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookingAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        room_number = self.cleaned_data.get('room_number')
        if not room_number.available :
            raise forms.ValidationError("Room Not Available")
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookingAdminForm,self).save(commit=commit)


class BookingAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookingAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        check_out = self.cleaned_data.get('check_out')
        if not self.check_out :
            raise forms.ValidationError("Checked out")
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookingAdminForm,self).save(commit=commit)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'guest_name', 'room_number', 'total_price','check_out',)
    form = BookingAdminForm

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Booking,BookingAdmin)
