// https://www.acmicpc.net/problem/1260
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, V;
    static int[][] EDGES;
    static int[] visited;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        EDGES = new int[N + 1][N + 1];
        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            EDGES[node1][node2] = EDGES[node2][node1] = 1;
        }

        // dfs
        visited = new int[N + 1];
        visited[V] = 1;
        System.out.print(V);
        dfs(V);
        System.out.println();

        // bfs
        Queue<Integer> q = new LinkedList<>();
        q.add(V);
        visited = new int[N + 1];
        visited[V] = 1;
        System.out.print(V);
        while (!q.isEmpty()){
            int node = q.poll();
            for(int i=1;i<N+1;i++){
                if(EDGES[node][i] == 1 && visited[i] == 0){
                    visited[i] = 1;
                    System.out.print(" " + Integer.toString(i));
                    q.add(i);
                }
            }
        }
    }
    public static void dfs(int node){
        for(int i=1;i<N+1;i++){
            if(EDGES[node][i] == 1 && visited[i] == 0){
                visited[i] = 1;
                System.out.print(" " + Integer.toString(i));
                dfs(i);
            }
        }
    }
}
