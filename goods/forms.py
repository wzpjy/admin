from django import forms
from .models import TGoods


class GoodsModelForm(forms.ModelForm):
    class Meta:
        model = TGoods

        fields = "__all__"
