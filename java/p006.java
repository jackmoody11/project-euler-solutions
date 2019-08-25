public class p006{
    public static void main(String[] args) {
        System.out.println(p006.run());
    }

    public static int run() {
        int sumOfSquares = 0;
        int squareOfSum = 0;
        for (int i = 1; i <= 100; i++) {
            sumOfSquares += Math.pow(i, 2);
            squareOfSum += i;
        }
        squareOfSum = (int) Math.pow(squareOfSum, 2);
        return squareOfSum - sumOfSquares;
    }
}