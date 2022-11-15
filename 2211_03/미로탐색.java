//
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static public class Pair{
        int r;
        int c;
        Pair(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    static int[] NR = {0, 0, 1, -1};
    static int[] NC = {1, -1, 0, 0};
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] MAZE = new int[N][M];
        int[][] visited = new int [N][M];
        for(int r=0;r<N;r++){
            String tmp = br.readLine();
            for(int c=0;c<M;c++){
                MAZE[r][c] = Integer.parseInt(String.valueOf(tmp.charAt(c)));
            }
        }
        
        //bfs
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(0,0));
        visited[0][0] = 1;
        while(!q.isEmpty()){
            Pair cur = q.poll();
            for(int i=0;i<4;i++){
                int nr = cur.r + NR[i];
                int nc = cur.c + NC[i];
                if(nr>=0 && nr< N && nc >=0 && nc < M && MAZE[nr][nc] == 1 && visited[nr][nc] == 0){
                    visited[nr][nc] = 1;
                    MAZE[nr][nc] = MAZE[cur.r][cur.c] + 1;
                    q.add(new Pair(nr,nc));
                }
            }
        }
        System.out.println(MAZE[N-1][M-1]);
    }
}
