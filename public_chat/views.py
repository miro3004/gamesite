from django.shortcuts import render

def public_chat_view(request):
    return render(request, 'public_chat/chat.html')



def room(request, room_name):
    
    return render(request, 'public_chat/room.html', {
    'room_name': room_name
    })
        