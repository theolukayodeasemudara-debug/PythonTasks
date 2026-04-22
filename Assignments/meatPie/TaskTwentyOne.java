import java.util.Scanner; 
public class TaskTwentyOne {
                public static void main (String[] args) {
                           Scanner valueCollector = new Scanner(System.in);

                           System.out.println("What's your base?");
                           int base = valueCollector.nextInt(); 

                           System.out.println("What's your height?");
                           int height = valueCollector.nextInt();     

                           int area =  base * height/2;
                           System.out.printf("The area of Traingle with b:%d and h:%d is %d %n%n", base,height,area);
                }
}
