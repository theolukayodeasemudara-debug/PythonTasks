import java.util.Scanner;
public class HypotenusFinder {
                public static void main (String[] args) {
                                         Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Give me the value of your opposite.");
                        int oppVal = userInput.nextInt();
                        System.out.println("Give me the value of your adjacent.");
                        int adjVal = userInput.nextInt();

//                      hypotenus formular is Asq+Bsq=Csq
                         int hypCalc = (oppVal * oppVal) +  (adjVal + adjVal);
                         int hyp = (hypCalc*hypCalc);

                        System.out.println("Hypotenus is = " + hyp);
                }
}
