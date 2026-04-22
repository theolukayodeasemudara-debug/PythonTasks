import java.util.Scanner; 
public class TaskSeventeen {
                public static void main (String[] args) {
                           Scanner valueCollector = new Scanner(System.in);

                           System.out.println("What's your lucky number?");
                           int luckyNum = valueCollector.nextInt(); 

                           int byFive = luckyNum + 10;

                           System.out.printf("Your lucky number %d plus by 10 is %d %n%n", luckyNum, byFive);                           
                }
}
