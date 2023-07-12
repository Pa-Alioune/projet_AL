package Models;

import java.util.List;

import DAO.ListUserManager;
import DAO.Manager;

public class User {
    private int id;
    private String userName;
    private String firstName;
    private String lastName;
    private String email;
    private String token;
    private String password;

    public User() {
    }

    public User(String userName, String token) throws Exception {
        this.setUserName(userName);
        this.token = token;
    }

    public User(int id, String userName, String firstName, String lastName, String email) {
        this.userName = userName;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.id = id;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public static User Connection(String login, String password) throws Exception {
        String request = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:urn=\"UserService\" encoding=\"utf-8\">\n"
                +
                "<soapenv:Header/>\n" +
                "    <soapenv:Body>\n" +
                "        <urn:authenticate_user>\n" +
                "            <username>" + login + "</username>\n" +
                "            <password>" + password + "</password>\n" +
                "        </urn:authenticate_user>\n" +
                "    </soapenv:Body>\n" +
                "</soapenv:Envelope>";

        String result = Manager.post(request);
        if (result.equals("Mot de passe incorrecte !") || result.equals("Login ou mot de passe incorrecte !")) {
            return null;
        }
        if (result.equals("")) {
            throw new Exception("Vous n'avez pas les droits d'administrations");
        }
        return new User(login, result);
    }

    public List<User> list() throws Exception {
        String request = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:urn=\"UserService\" encoding=\"utf-8\">\n"
                +
                "<soapenv:Header/>\n" +
                "    <soapenv:Body>\n" +
                "        <urn:list_users>\n" +
                "            <token>" + this.token + "</token>\n" +
                "        </urn:list_users>\n" +
                "    </soapenv:Body>\n" +
                "</soapenv:Envelope>";

        List<User> users = ListUserManager.get(request);
        return users;
    }

    public String add(User user) throws Exception {
        String request = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:urn=\"UserService\" encoding=\"utf-8\">\n"
                +
                "<soapenv:Header/>\n" +
                "    <soapenv:Body>\n" +
                "        <urn:add_user>\n" +
                "            <username>" + user.getUserName() + "</username>\n" +
                "            <password>" + user.getPassword() + "</password>\n" +
                "            <first_name>" + user.getFirstName() + "</first_name>\n" +
                "            <last_name>" + user.getLastName() + "</last_name>\n" +
                "            <email>" + user.getEmail() + "</email>\n" +
                "            <token>" + this.token + "</token>\n" +
                "        </urn:add_user>\n" +
                "    </soapenv:Body>\n" +
                "</soapenv:Envelope>";

        return Manager.post(request);
    }

    public String update(User user) throws Exception {
        String request = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:urn=\"UserService\" encoding=\"utf-8\">\n"
                +
                "<soapenv:Header/>\n" +
                "    <soapenv:Body>\n" +
                "        <urn:update_user>\n" +
                "            <username>" + user.getUserName() + "</username>\n" +
                "            <new_password>" + user.getPassword() + "</new_password>\n" +
                "            <first_name>" + user.getFirstName() + "</first_name>\n" +
                "            <last_name>" + user.getLastName() + "</last_name>\n" +
                "            <email>" + user.getEmail() + "</email>\n" +
                "            <token>" + this.token + "</token>\n" +
                "        </urn:update_user>\n" +
                "    </soapenv:Body>\n" +
                "</soapenv:Envelope>";

        return Manager.post(request);
    }

    public String delete(User user) throws Exception {
        String request = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:urn=\"UserService\" encoding=\"utf-8\">\n"
                +
                "<soapenv:Header/>\n" +
                "    <soapenv:Body>\n" +
                "        <urn:delete_user>\n" +
                "            <username>" + user.getUserName() + "</username>\n" +
                "            <token>" + this.token + "</token>\n" +
                "        </urn:delete_user>\n" +
                "    </soapenv:Body>\n" +
                "</soapenv:Envelope>";
        return Manager.post(request);
    }

    public String getUserName() {
        return userName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) throws Exception {
        if (firstName.length() > 2) {
            this.firstName = firstName;
        } else {
            throw new Exception("Le prénom d'un utilisateur doit contenir au moins 2 carractères");
        }
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) throws Exception {
        if (lastName.length() > 2) {
            this.lastName = lastName;
        } else {
            throw new Exception("Le prénom d'un utilisateur doit contenir au moins 2 carractères");
        }
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

}
