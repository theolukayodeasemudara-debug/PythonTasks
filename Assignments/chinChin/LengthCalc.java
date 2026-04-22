import java.util.Scanner;
public class LengthCalc {
            public static void main (String[] args) {
                Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Write any value lets calculate whether it is a 3 digit number.");
                        int userVal = userInput.nextInt();

//                      Get the length of the value
//                      0 - Head   1- Tail
                        int lengthOfNum = userVal.length;
            }
}
