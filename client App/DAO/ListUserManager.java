package DAO;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import Models.User;

public class ListUserManager {
    public static List<User> get(String soapRequest) throws Exception {
        // URL de l'API SOAP
        URL url = new URL("http://localhost:8000/soap/");

        // Ouverture de la connexion HTTP
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Content-Type", "text/xml;charset=UTF-8");
        connection.setDoOutput(true);

        // Corps de la requête SOAP

        OutputStream outputStream = connection.getOutputStream();
        outputStream.write(soapRequest.getBytes("UTF-8"));
        outputStream.flush();

        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }

        reader.close();
        outputStream.close();
        connection.disconnect();

        return Serializer(response);

    }

    public static List<User> Serializer(StringBuilder response) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        InputSource inputSource = new InputSource(new StringReader(response.toString()));
        Document document = builder.parse(inputSource);
        List<User> users = new ArrayList<>();

        NodeList usersResult = document.getElementsByTagName("users");
        for (int i = 0; i < usersResult.getLength(); i++) {
            Element element = (Element) usersResult.item(i);

            int id = Integer.parseInt(element.getElementsByTagName("id").item(0).getTextContent());
            String firstName = element.getElementsByTagName("first_name").item(0).getTextContent();
            String lastName = element.getElementsByTagName("last_name").item(0).getTextContent();
            String email = element.getElementsByTagName("email").item(0).getTextContent();
            String userName = element.getElementsByTagName("username").item(0).getTextContent();
            if (!firstName.equals("")) {
                User user = new User(id, userName, firstName, lastName, email);
                users.add(user);
            }
        }
        return users;
    }
}
