import java.util.Scanner; 
public class TaskThree{
                public static void main (String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int firstValue = valueCollector.nextInt();   


                    System.out.println("What's your second number?");
                    int secondValue = valueCollector.nextInt();

                    int sumTotal = firstValue + secondValue;
                    System.out.printf("The sum of %d nd %d is equal to = %d%n%n", firstValue, secondValue, sumTotal);        
                }
}
