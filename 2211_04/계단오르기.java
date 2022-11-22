import java.util.*;

public class Main {
    public static int N;
    public static int[] STAIRS;
    public static int[] dp;

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        STAIRS = new int[N+1];
        dp = new int[N+1];
        for(int i =1;i<N+1;i++){
            STAIRS[i] = sc.nextInt();
        }
        
      dp[1] = STAIRS[1];
        if(N >= 2) {
            dp[2] = STAIRS[2] + STAIRS[1];

            for (int i = 3; i < N + 1; i++) {
                dp[i] = Math.max(dp[i - 3] + STAIRS[i - 1] + STAIRS[i], dp[i - 2] + STAIRS[i]);
            }
        }
        System.out.println(dp[N]);
    }
}
