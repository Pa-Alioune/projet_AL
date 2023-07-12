import java.util.Scanner;

import Controllers.UserController;
import Models.User;

public class Menu {
    private static Scanner scanner = new Scanner(System.in);

    public static void show(User user) throws Exception {
        UserController userController = new UserController(user);

        int choix;
        boolean onContinue = true;
        while (onContinue) {
            System.out.println("----- Menu -----");
            System.out.println("Veuillez choisir une options de l'application: ");
            System.out.println("1. Lister les utilisateurs");
            System.out.println("2. Ajouter un utilisateur");
            System.out.println("3. Modifier un utilisateur");
            System.out.println("4. supprimer un utilisateur");
            System.out.println("5. quitter");
            System.out.print("Votre choix : ");

            choix = scanner.nextInt();
            scanner.nextLine();
            switch (choix) {
                case 1:
                    System.out.println("liste");
                    userController.list();
                    break;
                case 2:
                    userController.ajout();
                    break;
                case 3:
                    userController.update();
                    break;
                case 4:
                    userController.delete();
                    break;
                case 5:
                    System.out.println("Au revoir à bientôt......");
                    user = null;
                    onContinue = false;
                    break;
                default:
                    System.out.println("Choix invalide");
                    break;
            }
        }
    }
}
