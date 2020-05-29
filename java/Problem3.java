public class Problem3 {

    public static void main(String[] args) {
        long number = 600851475143L;

        while(number % 2 == 0) {
            number /= 2;
        }

        for(long i=3; i<number; i=i+2) {
            while(number % i == 0 && i<number ) {
                number /= i;
            }
        }
        System.out.println("The largest prime factor of the number 600851475143 is: "+number);
    }
}
