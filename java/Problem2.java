import java.util.ArrayList;
import java.util.List;

public class Problem2 {
    public static void main(String[] args) {
        int sum = 0;
        int fib1 = 0;
        int fib2 = 1;

        boolean flag = false;
        while(!flag) {
            int nextFib = fib1+fib2;
            fib1 = fib2;
            fib2 = nextFib;
            if(nextFib > 4000000) {
                flag = true;
                break;
            }
            if(nextFib % 2 == 0)
                sum += nextFib;
        }
        System.out.println("The sum of Fibonacci sequence of even-valued terms that are less then four million is: "+ sum);
    }
}
