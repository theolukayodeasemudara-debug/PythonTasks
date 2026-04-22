import java.util.Scanner;
public class PinApp {
            public static void main (String[] args) {
                     Scanner userInput = new Scanner(System.in);
    
                     //                      User instructions
                     System.out.println("Kindly enter your ATM 4 digit pin");
                    int atmPin = 1234;
                     int pinCode = userInput.nextInt();

                     if( pinCode == atmPin) {
                        System.out.printf("Your balance is $1000 %n");
                        } else if (pinCode != atmPin) {
                        System.out.printf("Wrong credentials!!! Please try again %n");                                
                        }
            }
}
