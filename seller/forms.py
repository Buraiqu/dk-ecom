# from django import forms
# from .models import Products

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if 'category' in self.data and self.data['category'] == 'accessories':
#             # exclude the fields you don't want to show
#             self.fields.pop('sleeve', None)
#             self.fields.pop('fit', None)
#             self.fields.pop('neck', None)