from django.shortcuts import render
from django.views import View
from .forms import Mpesadata
from django_daraja.mpesa.core import MpesaClient

# Create your views here.

class Mpesapay(View):
    formClass=Mpesadata
    template_name="mpesapay/lipanampesa.html"
    initial={'keny':'value'}
    def get(self,request):
        form=self.formClass(initial=self.initial)
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        form=self.formClass(request.POST)
        if form.is_valid():
            #Access the varius variables passed in the form to process payments 
            name= request.POST['name']
            id_number= request.POST['id_number']
            means= request.POST['means']
            description= request.POST['description']
            #Switch the means so as to process payments based on user selection
            match means:
                case "Direct deposit":
                    pass
                case "Pay bill":
                    pass
                case "Till number":
                    pass
                case "Pochi":
                    pass
        return render(request, self.template_name,{'form':form})
