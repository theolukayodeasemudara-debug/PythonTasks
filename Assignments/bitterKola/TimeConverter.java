import java.util.Scanner;
public class TimeConverter {
        public static void main (String[] args) {
            Scanner input = new Scanner(System.in);

//          Collecting num of minutes'
            System.out.println("Kinly enter your salary range");
            int numOfMins = input.nextInt(); 

//          calculating days, hours, mins
            int day = numOfMins/1440;
            int remMin = numOfMins % 1440;
            int hour = remMin/60;
            int min = remMin % 60;

            System.out.printf("%d days: %d hours: %d minutes %n",day,hour,min);
        }
}
