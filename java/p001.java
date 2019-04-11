
public class p001 {

    public static void main(String[] args) {
        System.out.println(p001.run());
    }

    public static int run() {
        int total = 0;
        for (int i = 1; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                total += i;
            }
        }
        return total;
    }

}