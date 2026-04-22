import java.util.Scanner;
public class TaskTwo{
            public static void main (String[] args) {
                     Scanner ageCollector = new Scanner(System.in);

                    System.out.println("How old are you?");
                     int ageValue = ageCollector.nextInt();

                    System.out.printf("You are %d years old!!!%n%n", ageValue);
            }
}
