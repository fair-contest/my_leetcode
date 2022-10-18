class Solution {
    public int atMostNGivenDigitSet(String[] digits, int n) {
        String strn = String.valueOf(n);
        int nlen = strn.length();
        int dlen = digits.length;
        int res = 0;
        int[] plist = new int[nlen];
        plist[nlen-1] = 1;
        if (nlen > 1) {
            plist[nlen-2] = dlen;
            res += dlen;
            if (nlen > 2) {
                for (int i=nlen-3;i>=0;i--) {
                    plist[i] = plist[i+1] * dlen;
                    res += plist[i];
                }
            }
        }
        int i = 0, check = 0, opt= 0;
        for (i=0;i<nlen;i++) {
            check = 0; opt = 0;
            for (String s : digits) {
                if (Integer.valueOf(s) <= Integer.valueOf(strn.charAt(i))-48) check++;
                if (Integer.valueOf(s) < Integer.valueOf(strn.charAt(i))-48) opt++;
            }
            if (check == 0) break;
            res += plist[i] * opt;
            if (check == opt) break;
        }
        return (i == nlen && check != 0) ? res + check - opt : res;
    }
}
