from django import forms


class ContactForm(forms.Form):
    def _media(self):
        return forms.Media(
            js=(
                'js/vendor/jquery.form.min.js',
                'js/vendor/parsley.min.js',
                'js/vendor/parsley-pt-br.js',
                'js/form.js')
        )

    media = property(_media)

    name = forms.CharField(
        label='Seu nome',
        max_length=100,
        widget=forms.TextInput(attrs={
            'id': 'template-contactform-name',
            'class': 'sm-form-control required',
        })
    )

    email = forms.EmailField(
        label='Seu email',
        max_length=60,
        widget=forms.EmailInput(attrs={
            'class': 'required email sm-form-control',
        })
    )

    phone = forms.CharField(
        label='Seu telefone',
        max_length=16,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'sm-form-control',
        })
    )

    subject = forms.CharField(
        label='Seu telefone',
        max_length=35,
        widget=forms.TextInput(attrs={
            'class': 'required sm-form-control',
        })
    )

    message = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'class': 'required sm-form-control',
            'cols': '30',
            'rows': '6'
        })
    )