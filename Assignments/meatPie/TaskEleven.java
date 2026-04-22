import java.util.Scanner;
public class TaskEleven {
            public static void main (String[] args) {
                        Scanner input = new Scanner(System.in);

                        System.out.print("enter your number:");
                        int num = input.nextInt();
                        
                        int calcHalf = num/2;
                        System.out.printf("The half of %d is %d %n%n", num, calcHalf);       
            }
}
