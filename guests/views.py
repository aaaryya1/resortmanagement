import datetime
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from requests import request
from manager.forms import UserInfoForm 
from account.models import Room,Booking,Event,UserInfo
from django.views.generic import DetailView,ListView,View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from .forms import *
from manager.forms import BookingForm
from django.contrib.auth.decorators import login_required




class RoomList(ListView):
        def get(self,request):

            return render(request,"room_list.html")
    
class BookingList(ListView):
    model=Booking
class Guesthmview(ListView):
    template_name="guesthome.html"
    queryset= Room.objects.all()
    context_object_name="Room"

class Ghomview(View):
      def get(self,request):
        return render(request,"ghomeview.html")

class Aboutview(View):
      def get(self,request):
        return render(request,"info.html")

class RoomDetails(DetailView):
    template_name="rmdetails.html"
    pk_url_kwarg='id'
    queryset=Room.objects.all()
    context_object_name='data'




from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

def BookingView(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            
            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            )

            if overlapping_bookings.exists():
                messages.error(request, 'This room is already booked for the selected dates.')
            elif check_out <= check_in:
                messages.error(request, 'Invalid date selection. Check-out date must be after check-in date.')
            else:
                userinfo, created = UserInfo.objects.get_or_create(user=request.user)

             
                booking = Booking(
                    user=request.user,
                    room=room,
                    check_in=check_in,
                    check_out=check_out,
                    userinfo=userinfo,  
                    status='confirmed'
                )
                booking.save()

                messages.success(request, 'Room is available!!!!!!!')
                return redirect('userinfo')  
        else:
            messages.error(request, 'Invalid form data. Please check the form and try again.')

    else:
        form = BookingForm(initial={'room': room})

    return render(request, 'booking.html', {'room': room, 'form': form})



def UserInfoView(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user_info, created = UserInfo.objects.get_or_create(user=request.user)
            user_info.name = form.cleaned_data['name']
            user_info.email = form.cleaned_data['email']
            user_info.address = form.cleaned_data['address']
            user_info.phone_number = form.cleaned_data['phone_number']
            user_info.save()

            messages.success(request, 'User info saved successfully.')
            return redirect('ghm') 
        else:
            messages.error(request, 'Invalid form data. Please check the form and try again.')
    else:
        form = UserInfoForm()
    
    return render(request, 'user_info.html', {'form': form})



from django.db.models import Q

class UserBookingsView(View):
    template_name = 'roomorderlist.html'

    def get(self, request):
        user = request.user
        bookings = Booking.objects.filter(user=user).select_related('room')

        return render(request, self.template_name, {'bookings': bookings})


class Pay(View):
    def get(self,request):
        return render(request,'payment.html')


def Addpaydet(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('booking_success') 
    else:
        form = BookingForm()
    
    return render(request, 'addpaydet.html', {'form': form})



def Viewevents(request):
    events = Event.objects.all()
    return render(request, 'viewevent.html', {'events': events})



from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def Cancelbooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    print(f"Booking Status: {booking.status}")
    if booking.user == request.user and booking.status in ['pending', 'confirmed']:
        booking.status = 'canceled'
        booking.save()
        messages.success(request, 'Booking canceled successfully.')
    else:
        messages.error(request, 'Cannot cancel this booking.')
    return redirect('bookingdt') 



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('hm')
    











