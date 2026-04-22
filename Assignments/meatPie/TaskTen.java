import java.util.Scanner; 
public class TaskTen{
                public static void main(String[] args) {
                    Scanner valueCollector = new Scanner(System.in);

                    System.out.println("What's your first number?");
                    int num = valueCollector.nextInt();   
                    
                    int doubleNum = num *2;
                    System.out.printf("your original num is %d, its double is %d %n%n",num,doubleNum );
                }
}
