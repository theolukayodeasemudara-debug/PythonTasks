import java.util.Scanner;
public class AreaOfTriangle {
                public static void main (String[] args) {
                                 Scanner inputCollector = new Scanner(System.in);

                                System.out.println("What is the length of the sides?!");
                                int length = inputCollector.nextInt();
                                
                                float num = 0.433f;
                                int lengthSquare = length * length;
                                double calcArea =  num * lengthSquare;
                                System.out.printf("The area of an Equilaterial Triangle with length:%d is %f %n%n",length, calcArea);           
                }
}
