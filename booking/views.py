from django.shortcuts import render

# Create your views here.
def movieDetailPage(request):
    
    return render(request, 'booking/movieDetail.html')
