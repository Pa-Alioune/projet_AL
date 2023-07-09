import threading
import os
import django

from pysimplesoap.server import SoapDispatcher
from http.server import BaseHTTPRequestHandler, HTTPServer
from actu_polytech.models import User
from pysimplesoap.server import SoapDispatcher
from http.server import ThreadingHTTPServer

django.setup()
os.environ['DJANGO_SETTINGS_MODULE'] = 'site_dactualite.settings'

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
                return "Mot de passe incorrect"
        except User.DoesNotExist:
            return "Login ou mot de passe incorrecte !"           

dispatcher = SoapDispatcher(
    name="user_service",
    location="http://localhost:8001/soap",
    action="http://localhost:8001/soap",
    namespace="urn:UserService"
)
# Enregistrez les méthodes de service web
dispatcher.register_function('list_users', UserService.list_users, returns={'users': str})
dispatcher.register_function('add_user', UserService.add_user, args={'username': str, 'password': str, 'first_name': str, 'last_name': str, 'email': str, 'token': str}, returns={'result': str})
dispatcher.register_function('delete_user', UserService.delete_user, args={'username': str, 'token': str}, returns={'result': str})
dispatcher.register_function('update_user', UserService.update_user, args={'username': str, 'new_password': str, 'first_name': str, 'last_name': str, 'email': str, 'token': str}, returns={'result': str})
dispatcher.register_function('authenticate_user', UserService.authenticate_user, args={'username': str, 'password': str}, returns={'result': str})

class SoapHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length).decode('utf-8')

        try:
            response = dispatcher.dispatch(request_body)
        except Exception as e:
            # Créer une réponse d'erreur SOAP personnalisée
            faultcode = 'Server'
            faultstring = str(e)
            response = self.create_fault_response(faultcode, faultstring)

        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def create_fault_response(self, faultcode, faultstring):
        template = '''
            <?xml version="1.0" encoding="UTF-8"?>
            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
                <SOAP-ENV:Body>
                    <SOAP-ENV:Fault>
                        <faultcode>{}</faultcode>
                        <faultstring>{}</faultstring>
                    </SOAP-ENV:Fault>
                </SOAP-ENV:Body>
            </SOAP-ENV:Envelope>
        '''
        return template.format(faultcode, faultstring)
# Créez une instance du serveur SOAP
soap_server = ThreadingHTTPServer(('localhost', 8001), SoapHandler)

# Lancez le serveur SOAP en arrière-plan
server_thread = threading.Thread(target=soap_server.serve_forever)
server_thread.daemon = True
server_thread.start()

print('Serveur SOAP démarré sur http://localhost:8001/soap')