from django.shortcuts import render

# Create your views here.




def tic_tac(request, *args, **kwargs):



	return render(request, "game/tic_tac.html")
