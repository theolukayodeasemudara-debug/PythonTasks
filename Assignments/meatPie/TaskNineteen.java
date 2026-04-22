import java.util.Scanner; 
public class TaskNineteen {
                public static void main (String[] args) {
                           Scanner valueCollector = new Scanner(System.in);

                           System.out.println("What's your lucky number?");
                           int luckyNum = valueCollector.nextInt(); 

                           int byFive = luckyNum/2;

                           System.out.printf("Your lucky number %d divided by 2 is %d %n%n", luckyNum, byFive);                           
                }
}
