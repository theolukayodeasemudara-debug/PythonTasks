import java.util.Scanner;
public class SpeedCalc {
                public static void main (String[] args) {
                Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Enter a speed value");
                        int userSpeed = userInput.nextInt();    

                        if(userSpeed == 0 ) {
                                    System.out.println("Car is stationary");
                         } else if (userSpeed >= 1 && userSpeed <= 40) {
                                    System.out.println("Car speed is slow");
                        } else if (userSpeed >= 41 && userSpeed <=80) {
                                    System.out.println("Car speed is moderate");
                        } else if (userSpeed >= 81 && userSpeed <= 120) {
                                    System.out.println ("Car speed is fast");
                        } else if (userSpeed > 120) {
                                    System.out.println("Car is moving dangerously fast");
                        }                
                }
}
