from django.shortcuts import render

# Create your views here.
def makePayment(request):
    return render(request,"payments/payment.html")