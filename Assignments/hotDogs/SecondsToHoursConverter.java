import java.util.Scanner;
public class SecondsToHoursConverter {    
                public static void main(String[] args) {
                                Scanner inputCollector = new Scanner(System.in);

                                System.out.print("Enter number of seconds: ");
                                long totalSecs = inputCollector.nextLong();

//                             3600 seconds = 1 hour
                                long hours   = totalSecs / 3600;
//                              calculate for the remainder
                                long remain  = totalSecs % 3600;
//                              60 secs = 1 minute
                                long minutes = remain / 60;
//                              calculate for the remainder again
                                long seconds = remain % 60;
                                System.out.printf("%d = %d hour, %d minutes, %d seconds %n%n",totalSecs,hours,minutes,seconds);
    }
}
