from django import forms

class FormularioUsuarios(forms.Form):
    rut = forms.CharField               (label="Rut", required = True, max_length=12,
                                        error_messages={
                                            'required': 'Ingrese el RUT del usuario',
                                            'max_length': 'El RUT no puede tener más de 12 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su Rut',
                                            'class':'form-control'})
                                        )
    nombreUsuario = forms.CharField  (label="NombreUsuario", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre de usuario es obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 10 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre de usuario',
                                            'class':'form-control'}),
                                        )
    nombre = forms.CharField            (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El nombre del usuario es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del usuario',
                                            'class':'form-control'}),
                                        )

    apellido = forms.CharField          (label="Apellido", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El apellido del usuario es obligatorio',
                                            'max_length': 'El apellido debe tener como maximo 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el apellido del usuario',
                                            'class':'form-control'}),
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email del usuario',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'Ingrese su correo electrónico',
                                            'class':'form-control',
                                            'type':'email'})
                                        )