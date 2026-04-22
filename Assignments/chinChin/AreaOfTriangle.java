import java.util.Scanner;
public class AreaOfTriangle {
            public static void main (String[] args) {
                            Scanner userInput = new Scanner(System.in);

//                      Base of  the traingle given
                        System.out.println("What is the base of your triangle?");
                        int base = userInput.nextInt();

//                      Height of  the traingle given
                        System.out.println("What is the height of your triangle?");
                        int height = userInput.nextInt();
                
//                        formular for area of a triangle = 1/2bh, where 1/2 = 0.5
                        float half = 0.5f;
                        float area = (half * base * height); 
                        System.out.printf("The are of your triangle is  %f %n",area);
            }
}
