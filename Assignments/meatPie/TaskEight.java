import java.util.Scanner; 
public class TaskEight{
                public static void main (String[] args) {
                        Scanner inputCollector = new Scanner(System.in);

                        System.out.println("What's your first number?");
                        int value = inputCollector.nextInt();   

                        int cube = value * value * value;

                        System.out.printf("The cube of %d is %d %n%n", value, cube);
                }
}
