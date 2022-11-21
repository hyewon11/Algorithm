import java.util.*;

public class Main {
    public static void main(String args[]){
      
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] SCORE = new int[N];
        for(int i =0;i<N;i++){
            SCORE[i] = sc.nextInt();
        }
        
      int left = 0;
        int right = N - 1;
        int[] arr = new int[2];
        int res = Integer.MAX_VALUE;
        while(left < right){
            int tmp = SCORE[left] + SCORE[right];
            if(res > Math.abs(tmp)){
                res = Math.abs(tmp);
                arr[0] = SCORE[left];
                arr[1] = SCORE[right];
            }
            if(tmp < 0){
                left++;
            }else{
                right--;
            }
        }
        System.out.println(Integer.toString(arr[0])+" "+Integer.toString(arr[1]));
    }
}
