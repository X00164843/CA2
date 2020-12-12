from django import forms

class VoucherApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert voucher here'}))