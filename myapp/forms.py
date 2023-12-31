from django import forms
from myapp.models import Review

class CartForm(forms.Form):
    quantity=forms.IntegerField(initial='1')
    product_id=forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self,request,*args,**Kwargs):
       self.request=request
       super(CartForm,self).__init__(*args,**Kwargs)

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review']      


