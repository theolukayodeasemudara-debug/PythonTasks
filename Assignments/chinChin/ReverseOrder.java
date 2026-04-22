import java.util.Scanner;
public class ReverseOrder {
                public static void main (String[] args) {
                        Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Give me a first number");
                        int numOne = userInput.nextInt();

                        System.out.println("Give me a second number");
                        int numTwo = userInput.nextInt();

                        System.out.println("Give me a third number");
                        int numThree = userInput.nextInt();

                        System.out.println("Give me a forth number");
                        int numFour = userInput.nextInt();

                        System.out.printf("%d%d%d%d ---- %d%d%d%d %n",numOne,numTwo,numThree,numFour,numFour,numThree,numTwo,numOne);

                }
}
