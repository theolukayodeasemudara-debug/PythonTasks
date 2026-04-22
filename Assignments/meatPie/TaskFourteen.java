import java.util.Scanner; 
public class TaskFourteen {
                public static void main (String[] args) {
                             Scanner valueCollector = new Scanner(System.in);

                             System.out.println("Let's find the average of (3) numbers that you would give me!!!'");
                             System.out.println("What's your first number?");
                             int firstNum = valueCollector.nextInt();     
  
                            System.out.println("What's your second number?");
                            int secondNum = valueCollector.nextInt();           
                            
                            System.out.println("What's your third number?");
                            int thirdNum = valueCollector.nextInt();

                            int sum =    firstNum + secondNum + thirdNum;

                            int avg = sum/3;

                           System.out.printf("The average of %d, %d, %d is %d %n%n", firstNum,secondNum,thirdNum,avg);
                }
}

