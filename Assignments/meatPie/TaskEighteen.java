import java.util.Scanner; 
public class TaskEighteen {
                public static void main (String[] args) {
                           Scanner valueCollector = new Scanner(System.in);

                           System.out.println("What's your lucky number?");
                           int luckyNum = valueCollector.nextInt(); 

                           int byFive = luckyNum - 5;

                           System.out.printf("Your lucky number %d subtracted by 5 is %d %n%n", luckyNum, byFive);                           
                }
}
