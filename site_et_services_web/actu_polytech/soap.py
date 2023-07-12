import io
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'site_dactualite.settings'
import django
django.setup()

from django.conf import settings
from pysimplesoap.server import SoapDispatcher
from http.server import BaseHTTPRequestHandler, HTTPServer
from actu_polytech.models import User
from pysimplesoap.server import SoapDispatcher
from http.server import ThreadingHTTPServer
from django.http import HttpResponse


class UserService(object):
    @staticmethod
    def list_users(token):
        try:
            user = User.objects.get(token=token)
            users = User.objects.all().values()
            return list(users)
        except User.DoesNotExist:
            return "Accès non autorisé"

    @staticmethod
    def add_user(username, password, first_name, last_name, email, token):
        try:
            user = User.objects.get(token=token)
            new_user = User(username=username, token=token, first_name=first_name, last_name=last_name, email=email)
            new_user.set_password(password)
            new_user.save()
            return "Utilisateur ajouté avec succès"
        except User.DoesNotExist:
            return "Accès non autorisé"

    @staticmethod
    def delete_user(username, token):
        try:
            user = User.objects.get(username=username, token=token)
            user.delete()
            return "Utilisateur supprimé avec succès"
        except User.DoesNotExist:
            return "Accès non autorisé"

    @staticmethod
    def update_user(username, new_password, first_name, last_name, email, token):
        try:
            user = User.objects.get(username=username, token=token)
            user.set_password(new_password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return "Utilisateur mis à jour avec succès"
        except User.DoesNotExist:
            return "Accès non autorisé"
        
    @staticmethod
    def authenticate_user(username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user.token
            else:
                return "Mot de passe incorrecte !"
        except User.DoesNotExist:
            return "Login ou mot de passe incorrecte !"           

dispatcher = SoapDispatcher("user_service")
# Enregistrez les méthodes de service web
dispatcher.register_function('list_users', UserService.list_users, args={'token': str}, returns={'users': str})
dispatcher.register_function('add_user', UserService.add_user, args={'username': str, 'password': str, 'first_name': str, 'last_name': str, 'email': str, 'token': str}, returns={'result': str})
dispatcher.register_function('delete_user', UserService.delete_user, args={'username': str, 'token': str}, returns={'result': str})
dispatcher.register_function('update_user', UserService.update_user, args={'username': str, 'new_password': str, 'first_name': str, 'last_name': str, 'email': str, 'token': str}, returns={'result': str})
dispatcher.register_function('authenticate_user', UserService.authenticate_user, args={'username': str, 'password': str}, returns={'result': str})

# Générez le contenu du fichier WSDL
wsdl_content = dispatcher.wsdl()

# Chemin vers le fichier WSDL
wsdl_file_path = os.path.join(settings.BASE_DIR, 'actu_polytech', 'wsdl', 'my_service.wsdl')
# Écrivez le contenu du fichier WSDL dans le fichier
with open(wsdl_file_path, 'w', encoding='utf-8') as wsdl_file:
    wsdl_file.write(wsdl_content.decode('utf-8'))

# Classe pour gérer les requêtes SOAP
class SOAPHandler:
    def __init__(self, request):
        self.request = request

    def soap_GET(self):
       # Convertir le corps de la requête en une chaîne de caractères
        request_body = self.request.body.decode('utf-8')

        # Logique pour gérer les requêtes POST SOAP
        response = dispatcher.dispatch(request_body)

        # Retourner la réponse avec le bon en-tête Content-Type
        return HttpResponse(response, content_type='text/xml; charset=utf-8')


    def soap_POST(self):
        # Convertir le corps de la requête en une chaîne de caractères
        request_body = self.request.body.decode('utf-8')

        # Logique pour gérer les requêtes POST SOAP
        response = dispatcher.dispatch(request_body)

        # Retourner la réponse avec le bon en-tête Content-Type
        return HttpResponse(response, content_type='text/xml; charset=utf-8')




# Créez une instance du serveur SOAP
# soap_server = HTTPServer(('localhost', 8001), SoapHandler)

# print('Serveur SOAP démarré sur http://localhost:8001/soap')

# # Lancez le serveur SOAP dans le flux principal
# soap_server.serve_forever()