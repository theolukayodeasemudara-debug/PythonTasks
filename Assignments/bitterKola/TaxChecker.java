import java.util.Scanner;
public class TaxChecker {
            public static void main (String[] args) {
            Scanner input = new Scanner (System.in);

//                      Collecting user's salary amount'
                        System.out.println("Kinly enter your salary range");
                        int salaryRange = input.nextInt(); 

//                      checking salary range  
                        if (salaryRange <= 300000) {
                                System.out.println("No Tax");
                        } else if(salaryRange >= 300001 && salaryRange <= 600000) {
                                System.out.println("Tax is 15%");
                        } else if (salaryRange > 600000) {
                                System.out.println("Tax is 25%");
                        }             
            }
}
