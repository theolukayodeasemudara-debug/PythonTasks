import java.util.Scanner; 
public class TaskTwelve{
                public static void main (String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int firstValue = valueCollector.nextInt();   


                    System.out.println("What's your second number?");
                    int secondValue = valueCollector.nextInt();

                    System.out.printf("These are the two numbers you gave me, %d & %d %n%n", firstValue, secondValue);        
                }
}
