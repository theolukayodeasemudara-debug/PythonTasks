import java.util.Scanner;
public class PinReader {
                public static void main (String[] args) {
                Scanner userInput = new Scanner(System.in);

//                      Collecting user's pin'
                        System.out.println("Kinly enter your 4 digit PIN");
                        int userPin = userInput.nextInt();   

//                      checking pin length    
                        if (userPin >= 1000 && userPin <= 9999) {
                                System.out.println("PIN is Valid");
                        } else {
                                System.out.println("Invalid PIN");
                        }        
                }
}
