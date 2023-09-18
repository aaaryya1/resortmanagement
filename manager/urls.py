from django.urls import path
from .views import *



urlpatterns =[
    path('mhm',Mhome.as_view(),name='Mhome'),
    path('roomadd',RoomAddview.as_view(),name='roomaddview'),
    path('viewroomlist',ViewRoomlist.as_view(),name='viewroomlist'),
    path('delrm/<int:id>',Deleteroom.as_view(),name='delrm'),
    path('editrm/<int:id>',Editroomdetails.as_view(),name='editrm'),
    path('addevent',AddEvent.as_view(),name='addevent'),
    path('vieweventlist',Eventlist,name='vieweventlist'),
    path('editevent/<int:id>',EditEvent.as_view(),name='editevent'),
    path('deleteevent/<int:id>',DeleteEvent.as_view(),name='deleteevent'),
    path('viewbklst',ViewBookinglist,name='viewbklst'),
    path('lgout',LogoutView.as_view(),name='lgout')
]