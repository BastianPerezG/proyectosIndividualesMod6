from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from aplicacion1.form import FormularioUsuarios
from aplicacion1.models import FormularioUsuariosDB
# Create your views here.

class LandingPage(TemplateView):
    template_name = "landing_page.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class Usuarios(TemplateView):
    template_name = "usuarios.html"

    def get(self, request, *args, **kwargs):
        titulo = "Lista de Usuarios"
        usuarios = [
        {   
            "nombreUsuario": "jsmith",
            "nombre": "John",
            "apellido": "Smith",
            "edad": 30,
            "email": "jsmith@example.com",
            "imagen": "https://randomuser.me/api/portraits/men/1.jpg"
        },
        {   
            "nombreUsuario": "ejohnson",
            "nombre": "Emily",
            "apellido": "Johnson",
            "edad": 25,
            "email": "ejohnson@example.com",
            "imagen": "https://randomuser.me/api/portraits/women/1.jpg"
        },
        {   
            "nombreUsuario": "mbrown",
            "nombre": "Michael",
            "apellido": "Brown",
            "edad": 35,
            "email": "mbrown@example.com",
            "imagen": "https://randomuser.me/api/portraits/men/2.jpg"
        },
        {   
            "nombreUsuario": "odavis",
            "nombre": "Olivia",
            "apellido": "Davis",
            "edad": 28,
            "email": "odavis@example.com",
            "imagen": "https://randomuser.me/api/portraits/women/2.jpg"
        },
        {   
            "nombreUsuario": "awilson",
            "nombre": "Alexander",
            "apellido": "Wilson",
            "edad": 32,
            "email": "awilson@example.com",
            "imagen": "https://randomuser.me/api/portraits/men/3.jpg"
        }]

        contexto = {
            "titulo": titulo,
            "usuarios": usuarios
        }
        return render(request, self.template_name, contexto)
    

class FormularioUsuariosView(TemplateView):
    template_name = 'formularioUsuarios.html'

    def get(self, request, *args, **kwargs):
        title = "Formulario de ingreso de usuarios"
        formulario = FormularioUsuarios()
        return render(request, self.template_name, {"formulario": formulario, "title": title})
    
    def post(self, request, *args, **kwargs):
        title = "Formulario de ingreso de usuarios"
        form = FormularioUsuarios(request.POST)
        mensajes = {
            "enviado" : True,
            "resultado": None
        }
        if form.is_valid():
            rut = form.cleaned_data["rut"]
            nombreUsuario = form.cleaned_data["nombreUsuario"]
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]


            registro = FormularioUsuariosDB(
                rut = rut,
                nombreUsuario = nombreUsuario,
                nombre = nombre,
                apellido = apellido,
                email = email
            )
            registro.save()
            mensajes = {"enviado": True, "resultado": "Has creado un nuevo usuario exitosamente."}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        
        return render(request, self.template_name, {"formulario": form, "mensajes": mensajes, "title": title})