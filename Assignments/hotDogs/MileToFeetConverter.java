import java.util.Scanner;
public class MileToFeetConverter {
                public static void main (String[] args) {
                         Scanner inputCollector = new Scanner(System.in);


                        System.out.println("What mile do you want to convert to Kilometer?");
                        int value = inputCollector.nextInt(); 

                        int oneMileValue = 5280;
                        int calcMileToFeet = value * oneMileValue;

                        System.out.printf("%d mile to feet is %d feet! %n%n",value,calcMileToFeet);  
                }
}



//                      formular to be used
//                     1 mi = 5,280'
//                      feet = (5 mi × 5,280) = 26,400'
