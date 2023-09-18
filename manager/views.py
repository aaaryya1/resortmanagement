from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from manager.forms import RoomForm,EventForm
from account.models import Room,Event,Booking
from django.contrib.auth import logout

# Create your views here.

class Mhome(View):
    def get(self,request):
        return render(request,"managerhome.html")




class RoomAddview(View):
    def get(self,request):
        form=RoomForm()
        return render(request,"addroom.html",{"form":form})
    def post(self,request):
        form_data=RoomForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save('Mhome')
            messages.success(request,"Room Added Successfully!!!")
            return redirect('Mhome')
        messages.error(request,"Room Adding Failed !!!Try Again!!") 
        return render(request,"addroom.html",{"form":form_data})
    


class ViewRoomlist(View):
    def get(self,request):
        res=Room.objects.all()
        return render(request,"viewroomlist.html",{"data":res})
    

    
class Editroomdetails(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        ob=Room.objects.get(id=eid)
        form=RoomForm(instance=ob)
        return render(request,"editrmdetails.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        ob=Room.objects.get(id=eid)
        form_data=RoomForm(data=request.POST,instance=ob)
        if form_data.is_valid():
                       
                       form_data.save()
                       return redirect('viewroomlist')
        return render(request,"editrmdetails.html",{"form":form_data})
    


class Deleteroom(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        res=Room.objects.get(id=eid) 
        res.delete()
        return redirect("viewroomlist") 
    


class AddEvent(View):
    template_name = 'addevent.html' 

    def get(self, request):
        form = EventForm() 
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EventForm(request.POST)  
        if form.is_valid():
            event = form.save() 
            return redirect('Mhome')  
        return render(request, self.template_name, {'form': form})
    

class EditEvent(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        ob=Event.objects.get(id=eid)
        form=EventForm(instance=ob)
        return render(request,"editevent.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        ob=Event.objects.get(id=eid)
        form_data=EventForm(data=request.POST,instance=ob)
        if form_data.is_valid():
                       
                       form_data.save()
                       return redirect('Mhome')
        return render(request,"editevent.html",{"form":form_data})


def Eventlist(request):
    events = Event.objects.all() 
    return render(request, 'vieweventlist.html', {'events': events})


class DeleteEvent(View):
    def get(self, request, id):
        try:
            event = Event.objects.get(id=id)
            event.delete()
            messages.success(request, 'Event added successfully.')
            return redirect('Mhome')  
        except Event.DoesNotExist:
            messages.error(request, 'Failed to add event')
            pass
        return redirect('Mhome') 
    




def ViewBookinglist(request):
    bookings = Booking.objects.select_related('userinfo').all()
    return render(request, 'viewbookings.html', {'bookings': bookings})


  
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('hm')
