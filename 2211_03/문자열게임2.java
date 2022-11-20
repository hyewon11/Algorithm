import java.util.*;

public class Main {

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i++) {
            String W = sc.next();
            int K = sc.nextInt();
            HashMap<Character, Integer> map = new HashMap<>();

            for (int j = 0; j < W.length(); j++) {
                char ch = W.charAt(j);
                if (map.containsKey(ch)) {
                    int cnt = map.get(ch);
                    map.replace(ch, ++cnt);
                } else {
                    map.put(ch, 1);
                }
            }

            Iterator<Character> keys = map.keySet().iterator();
            int short_length = 10001;
            int long_length = -1;
            while(keys.hasNext()){
                Character ch = keys.next();
                if(map.get(ch) >= K){
                    ArrayList<Integer> arr = new ArrayList<>();
                    int idx = W.indexOf(ch);
                    while(idx != -1){
                        arr.add(idx);
                        idx = W.indexOf(ch, idx + 1);
                    }
                    for(int j =0;j<arr.size()-K + 1;j++){
                        int length = arr.get(j + K - 1) - arr.get(j) + 1;
                        short_length = Math.min(short_length, length);
                        long_length = Math.max(long_length, length);
                    }
                }
            }
            if(short_length == 10001 || long_length == -1){
                System.out.println(-1);
            }else{
                System.out.print(short_length);
                System.out.print(" ");
                System.out.println(long_length);
            }
        }
    }
}
