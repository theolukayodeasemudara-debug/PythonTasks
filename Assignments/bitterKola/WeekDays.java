import java.util.Scanner;
public class WeekDays {
            public static void main (String[] args) {
                Scanner input = new Scanner(System.in);

//               User instructions
                 System.out.println("Enter a day of the week!");
//               The input is expected to take a charcter
                  int userInput = input.nextInt();

//                checking user input to match day
                  if (userInput == 0) {
                           System.out.println("Today is Monday!");
                   } else if (userInput == 1) {
                           System.out.println("Today is Tuesday!'");
                   } else if (userInput == 2) {
                           System.out.println("Today is Wednesday!");
                   } else if (userInput == 3) {
                           System.out.println("Today is Thursday!");
                   } else if (userInput == 4) {
                           System.out.println("Today is Friday!");
                   } else if (userInput == 5) {
                           System.out.println("Today is Saturday!");
                   } else if (userInput == 6) {
                           System.out.println("Today is Sunday!");
                   } else {
                        System.out.println("Day does not exist!");
                  }
            }
}
