import java.util.Scanner;
public class TaskTwentyEight {
                public static void main (String[] args) {
                        Scanner valueCollector = new Scanner(System.in);

                        System.out.println("What's your lucky number?");
                        int number = valueCollector.nextInt();

                        int byThree = number/3;
                        System.out.printf("You lucky number is %d, divided by 3 is %d %n%n", number, byThree);
                }
}
