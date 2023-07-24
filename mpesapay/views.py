from django.shortcuts import render
from django.views import View

# Create your views here.

class Mpesapay(View):
    template_name="mpesapay/lipanampesa.html"
    def get(self,request):
        return render(request, self.template_name)
    
    def post(self,request):
        name=request.POST.get('names')
        id_number=request.POST.get("Id Number")
        means=request.POST.get("payments")
        description=request.POST.get("description")

        #USE SWITCH CASE ON PAYMENTS TO CHECK THE PAYMENT METHOD SELECTED AND 
        match means:
            case "Direct deposit":
                pass
            case "Pay bill":
                pass
            case "Till number":
                pass
            case "Pochi":
                pass
