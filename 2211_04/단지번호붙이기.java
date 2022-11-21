// https://www.acmicpc.net/problem/2667
import java.util.*;

public class Main {
    public static int N;
    public static boolean[][] MAP;
    public static boolean[][] visit;
    public static int[] dr = {0, 0, 1, -1};
    public static int[] dc = {1, -1, 0, 0};

    static class Pair{
        int r;
        int c;
        Pair(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    static int get_townN(int r, int c){
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(r, c));
        visit[r][c] = true;
        int cnt = 1;

        while(!q.isEmpty()){
            Pair p = q.poll();

            for(int i=0;i<4;i++){
                int nr = p.r + dr[i];
                int nc = p.c + dc[i];
                if(0 <= nr && nr < N && 0 <= nc && nc < N && MAP[nr][nc] && !visit[nr][nc]){
                    q.add(new Pair(nr, nc));
                    visit[nr][nc] = true;
                    cnt += 1;
                }
            }
        }
        return cnt;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        MAP = new boolean[N][N];
        visit = new boolean[N][N];
        for(int i =0;i<N;i++){
            String tmp = sc.next();
            for(int j=0;j<N;j++) {
                if(tmp.charAt(j) == '1'){
                    MAP[i][j] = true;
                }else{
                    MAP[i][j] = false;
                }
            }
        }

        ArrayList<Integer> res = new ArrayList<>();
        for(int i =0;i<N;i++){
            for(int j=0;j<N;j++) {
                if(MAP[i][j] && !visit[i][j]){
                    int cnt = get_townN(i, j);
                    res.add(cnt);
                }
            }
        }
        
        Collections.sort(res);
        System.out.println(res.size());
        for(int i=0;i<res.size();i++){
            System.out.println(res.get(i));
        }
    }
}
