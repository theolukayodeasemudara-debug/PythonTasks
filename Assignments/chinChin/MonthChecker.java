import java.util.Scanner;
public class MonthChecker {
            public static void main (String[] args) {

                Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Pick a number between 1 and 12 to display which month matches it.");
                        int userVal = userInput.nextInt();

//                      logic for showing the moths that matches the user's value

                        if(userVal == 1) {
                        System.out.printf("January");
                        } else if (userVal == 2) {
                        System.out.printf("February");                                
                        } else if (userVal == 3) {
                        System.out.printf("March");                                
                        } else if (userVal == 4) {
                        System.out.printf("April");                                
                        } else if (userVal == 5) {
                        System.out.printf("May");                                
                        } else if (userVal == 6) {
                        System.out.printf("June");                                
                        } else if (userVal == 7) {
                        System.out.printf("July");                                
                        } else if (userVal == 8) {
                        System.out.printf("August");                                
                        } else if (userVal == 9) {
                        System.out.printf("Sept");                                
                        } else if (userVal == 10) {
                        System.out.printf("October");                                
                        } else if (userVal == 11) {
                        System.out.printf("November");                                
                        } else if (userVal == 12) {
                        System.out.printf("December");                                
                        } else if (userVal > 12 || userVal <1) {
                        System.out.printf("You too do aboiii %n");                                
                        }












            }
}
