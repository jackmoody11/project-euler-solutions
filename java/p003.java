import java.lang.Math;

public class p003 {

    public static void main(String[] args) {
        System.out.println(p003.run());
    }

    public static long run() {
        long maxDiv = 0;
        long x = 600851475143L;
        for (long i = 2; i < Math.floor(Math.sqrt(x)); i++) {
            if (x % i == 0 && isPrime(i)) {
                maxDiv = i;
            }
        }
        return maxDiv;
    }

    public static boolean isPrime(long n) {
        if (n < 2) {
            return false;
        }
        else if (n == 2 || n == 3) {
            return true;
        }
        else if (n % 2 == 0) {
            return false;
        }
        else {
            for (int i = 3; i < Math.ceil(Math.sqrt(n)) + 1; i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
    }
}