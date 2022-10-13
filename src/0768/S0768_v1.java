class Solution {
    public int maxChunksToSorted(int[] arr) {
        int[] rec = new int[arr.length+1];
        rec[0] = 0;
        int cur = arr[0];
        int p = 0;
        for (int i = 0; i < arr.length; i++) {
            while (arr[i] < rec[p]) p--;
            if (arr[i] > cur) cur = arr[i];
            rec[++p] = cur;
        }
        rec = null;
        return p;        
    }
}
