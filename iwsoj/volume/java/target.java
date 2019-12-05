class Main {

    public static int fact(final int n) {
        if (n == 0) {
            return 1;
        }
        return n * fact(n-1);
    }

    public static void main(String[] args) {
        final int n = 4;
        System.out.println("Factorial of " + n + " is " +fact(n));
    }

}