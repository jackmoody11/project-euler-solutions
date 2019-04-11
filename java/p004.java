public class p004 {

    public static void main(String[] args) {
        System.out.println(p004.run());
    }

    public static long run() {
        long maxP = 0;
        long num = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < i + 1; j++) {
                num = i * j;
                if (isPalindrome(Long.toString(num)) && num > maxP) {
                    maxP = num;
                }
            }
        }
        return maxP;
    }

    public static boolean isPalindrome(String s) {
        String sReverse = new StringBuilder(s).reverse().toString();
        return sReverse.equals(s);
    }

}