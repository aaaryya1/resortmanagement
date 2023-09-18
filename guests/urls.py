from django.urls import path
from .views import *

urlpatterns=[
    
    path('room_list/',RoomList.as_view(),name='RoomList'),
    path('booking_list/',BookingList.as_view(),name='BookingList'),
    path('rdetails/<int:id>',RoomDetails.as_view(),name='rdetails'),
    path('ghm',Ghomview.as_view(),name='ghm'),
    path('About',Aboutview.as_view(),name='About'),
    path('viewevent',Viewevents,name='viewevent'),
    path('glgout',LogoutView.as_view(),name='glgout'),
    path('available/<int:room_id>',BookingView,name='available'),
    path('addpaydet',Addpaydet,name='addpaydet'),
    path('userinfo',UserInfoView,name='userinfo'),
    path('bookingdt',UserBookingsView.as_view(),name='bookingdt'),
    path('cancel<int:booking_id>',Cancelbooking,name='cancel'),
    path('payment',Pay.as_view(),name='pay'),
    
    
    
   



]
