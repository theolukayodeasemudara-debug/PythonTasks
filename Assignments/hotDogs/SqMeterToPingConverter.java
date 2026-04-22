import java.util.Scanner;
public class SqMeterToPingConverter {
                public static void main (String[] args) {
                         Scanner inputCollector = new Scanner(System.in);


                        System.out.println("What Square-Meter do you want to convert to Pings?");
                        int value = inputCollector.nextInt(); 

                        float squareMeter = 0.3025f;
                        double sqMetToPing = value * squareMeter;

                        System.out.printf("%d Sqm to Pings is %f Pings! %n%n",value,sqMetToPing);  
                }
}



//                      formular to be used
//                     1 squareMeter = 0.3025
//                      feet = (5 mi × 5,280) = 26,400'
