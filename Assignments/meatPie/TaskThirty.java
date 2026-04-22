import java.util.Scanner;
public class TaskThirty {
               public static void main (String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int firstNum = valueCollector.nextInt();   


                    System.out.println("What's your second number?");
                    int secondNum = valueCollector.nextInt();

                    int sum = firstNum + secondNum;
                    int prod = firstNum * secondNum;
                    
                System.out.printf("The sum between %d nd %d is equal to = %d %n%n", firstNum, secondNum, sum);
                System.out.printf("The product of %d nd %d is equal to = %d %n%n", firstNum, secondNum, prod);
               }
}
