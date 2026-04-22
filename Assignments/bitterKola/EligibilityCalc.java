import java.util.Scanner;
public class EligibilityCalc {
                public static void main (String[] args) {
                Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("What is your birth year?");
                        int birthYear = userInput.nextInt();

                        int currentYear = 2026;
                        int age = currentYear - birthYear;

                        if (age >= 65) {
                                System.out.println("You are eligble for a senior citizen discount.");
                         } else {
                                System.out.println("Sorry, you'll have to wait till you're 65+ years'");
                        }
                }
}
