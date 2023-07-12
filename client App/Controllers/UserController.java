package Controllers;

import java.util.List;

import Models.User;
import utils.Caracter;

public class UserController {
    private User user;

    public UserController(User user) {
        this.user = user;
    }

    public static User connexion(String login, String password) throws Exception {
        return User.Connection(login, password);
    }

    public void ajout() throws Exception {
        User user = new User();
        System.out.println("Ajouter d'utilisateur ");
        try {

            user.setFirstName(Caracter.writeCaracterWithGoodString("Entrer le prénom : "));
            user.setLastName(Caracter.writeCaracterWithGoodString("Entrer le nom  : "));
            user.setUserName(Caracter.writeCaracterWithGoodString("Entrer un login   : "));
            user.setPassword(Caracter.passwordCorrect("Entrer un mot de passe : "));
            user.setEmail(Caracter.verifyEmail());
            System.out.println("---------------------------------------------");

            System.out.println("\t" + this.user.add(user));
            System.out.println("---------------------------------------------");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

    public void list() throws Exception {
        List<User> users = this.user.list();
        System.out
                .printf("ID         Prénom                    Nom                       Email                     Login\n");
        for (User user : users) {
            System.out.printf("%-10s %-25s %-25s %-25s %-25s\n",
                    user.getId(), user.getFirstName(), user.getLastName(), user.getEmail(), user.getUserName());
        }
    }

    public void update() throws Exception {
        User user = new User();
        System.out.println("Mise à jour d'utilisateur ");
        try {
            user.setUserName(Caracter.writeCaracterWithGoodString("Veuillez renseigner son  login  : "));

            user.setFirstName(Caracter.writeCaracterWithGoodString("Entrer le nouveau prénom : "));
            user.setLastName(Caracter.writeCaracterWithGoodString("Entrer le nouveau nom  : "));
            user.setPassword(Caracter.passwordCorrect("Entrer un nouveau mot de passe : "));
            user.setEmail(Caracter.verifyEmail());
            System.out.println("---------------------------------------------");
            System.out.println("\t" + this.user.update(user));
            System.out.println("---------------------------------------------");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void delete() throws Exception {
        User user = new User();
        System.out.println("Suppression d'utilisateur ");
        try {
            user.setUserName(Caracter.writeCaracterWithGoodString("Entrer le nom d'utilisateur   : "));
            System.out.println("---------------------------------------------");
            System.out.println("\t" + this.user.delete(user));
            System.out.println("---------------------------------------------");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

}
