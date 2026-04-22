import java.util.Scanner; 
public class TaskSeven{
                public static void main (String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int value = valueCollector.nextInt();   

                    int square = value * value;

                    System.out .printf("The square of %d is %d %n%n", value, square);
                }
}
