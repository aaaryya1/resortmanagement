from django import forms
from account.models import Room,Event,Booking,UserInfo






class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['room_number','room_type','capacity','price_per_night','description','image']
        widgets={
            "room_number":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter room name"}),
            "room_type":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the type of the room"}),
            "capacity":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the no:of people can accomodate in the room"}),
            
            "price_per_night":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter price per night"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Enter Room description"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
                }
        


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date']
       



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['check_in','check_out', 'userinfo']




class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name','email', 'address', 'phone_number',]








