from django import forms


class Mpesadata(forms.Form):
    name= forms.CharField(label='name', max_length=20)
    id_number= forms.IntegerField(label='id_number')
    description = forms.CharField(label='description',widget=forms.Textarea)
    #implement the means as choices 
    #predefine choices 
    payment_choices=[
        ('', '--select--'),
        ('D', 'direct deposit'),
        ('T', 'till number'),
        ('P', 'paybill'),
        ('PO', 'pochi la biashara')
    ]
    means=forms.ChoiceField(
        choices=payment_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),  
        label='Select Payment method'
    )


