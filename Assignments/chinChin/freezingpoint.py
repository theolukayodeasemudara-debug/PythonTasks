import java.util.Scanner;
public class FreezingPoint {
                public static void main (String[] args) {
                         Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Give me a temperature value.");
                        int tempVal = userInput.nextInt();

                        if(tempVal < 0) {
                                    System.out.printf("It is freezing @ %d degrees %n", tempVal);
                        } else if (tempVal >= 0 && tempVal <= 15 ) {
                                    System.out.printf("It is cold @ %d degrees %n", tempVal);
                        } else if (tempVal >= 15 && tempVal <= 25 ) {
                                    System.out.printf("It is warm @ %d degrees %n", tempVal);
                        } else if (tempVal > 25 ) {
                                    System.out.printf("It is extremely hot @ %d degrees %n", tempVal);
                        }
                }
}
