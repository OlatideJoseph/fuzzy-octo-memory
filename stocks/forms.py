from django import forms

class StockForm(forms.Form):
    checkbox = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, 
                                         choices=[
            ('panadol', 'panadol'), ('paracetamol', 'paracetamol'),
            ('panadol xtra', 'panadol xtra'), ('procold', 'procold'), ('vitamin c', 'vitamin C'),
        ])
    quantity = forms.IntegerField(required=True)
    cost_price = forms.IntegerField(required=True)
    selling_price = forms.IntegerField(required=True)
