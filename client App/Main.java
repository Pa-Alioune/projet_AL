import java.util.Scanner;

import Controllers.UserController;
import Models.User;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String login, password;

        User user = null;
        int tentatives = 3;
        System.out.println("----Bonjour Bienvenue dans l'application de gestion des utilisateur --------");
        System.out.println("----Pour Continuer à utiliser notre application Il vous faut vous connecter-------");
        while (tentatives > 0) {
            System.out.print("Veuillez renseigner votre login : ");
            login = scanner.nextLine();
            System.out.print("\n Veuillez renseigner votre mot de passe : ");
            password = scanner.nextLine();
            try {

                user = UserController.connexion(login, password);
            } catch (Exception e) {
                System.out.println(e.getMessage());
                System.out.println("Au revoir ....");
                break;
            }
            if (user != null) {
                Menu.show(user);
                break;
            } else {
                System.out.println("Login ou mot de passe incorrect");
                tentatives--;
            }
            if (tentatives == 0) {
                System.out.println("Trop de tentatives revenez plut tard...........");

            }
        }
        scanner.close();
    }
}
