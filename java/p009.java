// def compute():
//     """
//     We define a as the shortest side, and since a + b + c = 1000, a < 333.
//     """
//     for a in range(1, 333):
//         for b in range(a, 1000):
//             if a + b + sqrt(a**2 + b**2) > 1000:
//                 break
//             elif a + b + sqrt(a**2 + b**2) == 1000:
//                 return a * b * sqrt(a**2 + b**2)

public class p009 {
    public static void main(String[] args) {
        System.out.printf("%.0f", p009.run());
    }

    public static double run() {
        for (int i = 1; i < 333; i++) {
            for (int j = i; j < 1000; j++) {
                if (i + j + Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2)) > 1000) {
                    break;
                } else if (i + j + Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2)) == 1000) {
                    return i * j * Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2));
                }
            }
        }
        return 0;
    }
}