public class RainbowColorDisplay {
                public static void main (String[] args) {
//                    generating random numbers
                      int randomNum = (int)(Math.random() * 7) + 1;

//                    displaying the colors based on the numbers displayed
   
                      if(randomNum == 1){
                            System.out.printf("The color picked is 'Violet': %d %n", randomNum);
                      } else if(randomNum == 2){
                            System.out.printf("The color picked is 'Indigo': %d %n", randomNum);
                     } else if(randomNum == 3){
                            System.out.printf("The color picked is 'Blue': %d %n",randomNum);                     
                     } else if(randomNum == 4){
                            System.out.printf("The color picked is 'Green': %d%n", randomNum);
                    } else if(randomNum == 5){
                            System.out.printf("The color picked is 'Yellow': %d%n", randomNum);
                    } else if(randomNum == 6){
                            System.out.printf("The color picked is 'Orange': %d%n", randomNum);        
                    } else if(randomNum == 7){
                            System.out.printf("The color picked is 'Red': %d", randomNum);
                    }
                }
}

//                  colors to be used are; violet, indigo, blue, green, yellow, orange and, red
