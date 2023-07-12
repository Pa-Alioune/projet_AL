package utils;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Caracter {
    public static String writeCaracterWithGoodString(String message) {
        Scanner scan = new Scanner(System.in);
        String value;
        while (true) {
            System.out.print(message);
            value = scan.nextLine();
            if (value.length() > 2) {
                break;
            } else {
                System.out.println("Vous devez fournir une chaine de taille supérieur à 2");
            }
        }
        return value;
    }

    public static String passwordCorrect(String message) {
        Scanner scan = new Scanner(System.in);
        String value;
        while (true) {
            System.out.print(message);
            value = scan.nextLine();
            if (value.length() > 2) {
                break;
            } else {
                System.out.println("Le mot de passe doit avoir une taille supérieur à 6");
            }
        }
        return value;
    }

    public static String verifyEmail() {
        Scanner scan = new Scanner(System.in);
        String email;
        Pattern emailPattern = Pattern.compile("^[A-Za-z0-9+_.-]+@[A-Za-z]+.[A-Za-z]+$");
        while (true) {
            System.out.print("Veillez renseigner votre email : ");
            email = scan.nextLine();
            Matcher matcher = emailPattern.matcher(email);
            if (!matcher.find()) {
                System.out.println("Format d'email invalid ");
            } else {
                break;
            }
        }
        return email;
    }
}
