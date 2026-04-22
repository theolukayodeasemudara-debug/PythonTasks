import java.util.Scanner;
public class mileToKilometerConverter {
                public static void main (String[] args) {
                        Scanner inputCollector = new Scanner(System.in);

                        System.out.println("What mile do you want to convert to Kilometer?");
                        int value = inputCollector.nextInt(); 

                        int calcOne = value/2;
                        int calcTwo = calcOne/4;
                        int toKilometer = calcOne + calcTwo;

                        System.out.printf("%d to kilometer is %d %n%n",value,toKilometer);  
                }
}
