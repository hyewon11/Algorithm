// https://www.acmicpc.net/problem/2606
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] PAIRS = new int[101][101];
        for(int i=0;i<M;i++){
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            PAIRS[n1][n2] = PAIRS[n2][n1] = 1;
        }

        int cnt = 0;
        int[] visited = new int[101];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = 1;
        while(!q.isEmpty()){
            int n = q.poll();
            for(int i=1;i<N+1;i++){
                if(PAIRS[n][i] == 1 && visited[i] == 0){
                    q.add(i);
                    visited[i] = 1;
                    cnt += 1;
                }
            }
        }
        System.out.println(cnt);
    }
}
