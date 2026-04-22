import java.util.Scanner; 
public class TaskFour{
                public static void main (String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int firstValue = valueCollector.nextInt();   


                    System.out.println("What's your second number?");
                    int secondValue = valueCollector.nextInt();

                    int differences = firstValue - secondValue;
                    System.out.printf("The difference between %d nd %d is equal to = %d%n%n", firstValue, secondValue, differences);        
                }
}
