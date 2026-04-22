import java.util.Scanner; 
public class TaskTwenty {
                public static void main (String[] args) {
                        Scanner valueCollector = new Scanner(System.in);
                        System.out.println("What's your length?");
                        int length = valueCollector.nextInt();    

                        System.out.println("What's your width?");
                        int width = valueCollector.nextInt();

                        int product = length * width;
                        int area = product * product;

                        System.out.printf("The area of your length:%d and the width:%d is %d %n%n", length,width,area);                   
                }
}
