class Solution {
    public int atMostNGivenDigitSet(String[] digits, int n) {
        int[] nums = nToArray(n);
        int nlen = nums.length;
        int dlen = digits.length;
        int res = 0;
        int[] plist = new int[nlen];
        plist[nlen-1] = 1;
        if (nlen > 1) {
            plist[nlen-2] = dlen;
            res += dlen;
            if (nlen > 2) {
                for (int i=nlen-3;i>=0;i--) {
                //题目digits长度不超9和n不大于10的9次方，所以下面这行乘法代码计算最大也只是9的9次方，不会溢出。
                    plist[i] = plist[i+1] * dlen;
                    res += plist[i];
                }
            }
        }
        int i = 0, check = 0, opt= 0, cur = 0;
        for (i=0;i<nlen;i++) {
            check = 0; opt = 0;
            cur = nums[i];
            for (String s : digits) {
                int tmp = Integer.valueOf(s);
                if (tmp <= cur) check++;
                if (tmp < cur) opt++;
            }
            if (check == 0) break;
            res += plist[i] * opt;
            if (check == opt) break;
        }
        nums = null;
        plist = null;
        return (i == nlen && check != 0) ? res + check - opt : res;
    }

    private int[] nToArray(int n) {
        int[] arr = new int[10];
        int i = 0;
        while (n > 0) {
            arr[i] = n % 10;
            n /= 10;
            i++;
        }
        int[] res = new int[i];
        for (int j = 0; j < i; j++) {
            res[j] = arr[i-j-1];
        }
        arr = null;
        return res;
    }
}
