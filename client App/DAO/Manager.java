package DAO;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.URL;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

public class Manager {
    public static String post(String soapRequest) throws Exception {
        // URL de l'API SOAP
        URL url = new URL("http://localhost:8000/soap/");

        // Ouverture de la connexion HTTP
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
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

    public static String Serializer(StringBuilder response) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        InputSource inputSource = new InputSource(new StringReader(response.toString()));
        Document document = builder.parse(inputSource);

        NodeList resultNodes = document.getElementsByTagName("result");
        if (resultNodes.getLength() == 0) {
            return "";
        }
        String resultValue = resultNodes.item(0).getTextContent();

        return resultValue;
    }
}
