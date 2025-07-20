from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        help_text="Requis. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Prénom",
        help_text="Requis. Veuillez entrer votre prénom.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nom",
        help_text="Requis. Veuillez entrer votre nom.",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Adresse e-mail",
        help_text="Requis. Veuillez entrer une adresse e-mail valide.",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        label="Téléphone",
        help_text="Obligatoire. Ex: +2377671234567",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    country = forms.CharField(
        max_length=50,
        required=False,
        label="Pays",
        help_text="Obligatoire. Ex: France, Sénégal, Canada...",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Requis. 8 caractères minimum. Ne doit pas être similaire à vos autres informations personnelles. Ne doit pas être commun et ne peut pas être entièrement numérique."
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Entrez le même mot de passe qu’auparavant, pour vérification."
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # Ajouter les champs personnalisés (profile)
        self.fields['phone'] = forms.CharField(
            max_length=20,
            required=False,
            label="Téléphone",
            help_text="Obligatoire. Ex: +2376771234567",
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        self.fields['country'] = forms.CharField(
            max_length=50,
            required=False,
            label="Pays",
            help_text="Obligatoire. Ex: France, Sénégal, Canada...",
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )

        # Réordonner les champs
        field_order = ['username', 'first_name', 'last_name', 'email', 'phone', 'country', 'password1', 'password2']
        self.fields = {k: self.fields[k] for k in field_order}

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            # Enregistrer les champs supplémentaires dans le profil
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone = self.cleaned_data.get('phone')
            profile.country = self.cleaned_data.get('country')
            profile.save()
        return user