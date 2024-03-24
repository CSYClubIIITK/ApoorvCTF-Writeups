import java.io.*;
import java.util.*;  

public class message {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String message = "";
        String pin = "";
        int i = 0;
        boolean check;

        

        System.out.print("What's the pin: ");
        pin = keyboard.readLine();

        message = encoder.encodeToString(pin.getBytes());
        
              
        check = decodeMsg(message);
        if (check) {
            System.out.println("Yay!You found it");
        }
        else {
            System.out.println("Try again comrade\n");
        }
    }
    
    public static boolean decodeMsg(String secret) {
        String message = "dzRybTFuZ191cF95M3MwN2s5";
        
        if (secret.equals(message)) {
            return true;
        }
        else {
            return false;
        }
    }
}
