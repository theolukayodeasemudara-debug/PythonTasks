import java.util.Scanner;
public class SumThreeNum {
            public static void main (String[] args) {
                        Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Give me a first number");
                        int one = userInput.nextInt();
                        System.out.println("Give me a second  number");
                        int two = userInput.nextInt();
                        System.out.println("Give me a third number");
                        int three = userInput.nextInt();

                        int subTotal = one+two+three;
                    
                        System.out.printf("%d%d%d is ---> %d+%d+%d = %d %n",one,two,three,one,two,three,subTotal);
            }
}
