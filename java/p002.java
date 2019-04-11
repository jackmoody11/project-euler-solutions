public class p002 {

    public static void main(String[] args) {
        System.out.println(p002.run());
    }

    public static int run() {
        int a = 1, b = 1;
        int total = 0;
        while (a <= 4000000) {
            int a_old = a;
            a = b;
            b = a_old + b;
            if (a % 2 == 0) {
                total += a;
            }
        }
        return total;
    }
}