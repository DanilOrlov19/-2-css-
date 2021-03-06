from django import forms
from django.contrib.auth.models import User
from .models import Order

from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type',
        )

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label= 'Логин'
        self.fields['password'].label= 'Пароль'
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter (username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден')
        user= User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
    class Meta:
        model= User
        fields = ['username', 'password']

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required = False)
    address = forms.CharField(required = False)
    email = forms.EmailField(required=True)

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['first_name'].label = 'Ваше имя'
        self.fields['last_name'].label = 'Ваша фамилия'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Ваша почта'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Данный email уже зарегистрирован')
        return email
    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Имя занято')
        return username
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data
    class Meta:
        model= User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name','last_name', 'address','phone']

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


