class Solution {
    public int[] threeEqualParts(int[] arr) {
        int alen = arr.length;
        int cnt = 0;
        // 首先求第一段实体的起点a1
        int a1 = 0;
        for (int v=0;v<alen;v++) if (arr[v]==1) {a1=v;break;}
        // 再求1的总数
        for (int v=a1;v<alen;v++) if (arr[v]==1) ++cnt;
        int[] all_zero = {0, alen - 1};
        if (cnt == 0) return all_zero;
        int[] fail = {-1, -1};
        if (cnt % 3 != 0) return fail;
        // 其次取第二段和第三段实体起点a2, a3
        int a2 = 2 * cnt/3;
        int a3 = cnt/3;
        cnt = 0;
        for (int v=alen-1;v>0;v--) {
            if (arr[v] == 1) {
                cnt++;
                if (cnt == a3) {
                    a3 = v;
                    break;
                }
            }
        }
        for (int v=a3-1;v>0;v--) {
            if (arr[v] == 1) {
                cnt++;
                if (cnt == a2) {
                    a2 = v;
                    break;
                }
            }
        }
        int r = alen - a3; // 每段实体的长度应等于第三段长度，这里用r代表
        if (a1 + r > a2 || a2 + r > a3) return fail; 
        // 以第三段为基础与第一二段比较
        int i = a1;
        int j = a2;
        for (int v=a3; v<alen; v++) {
            if (arr[v] != arr[i] || arr[v] != arr[j]) {
                return fail;
            }
            i++;
            j++;
        }
        // 到这一步时，必然已有三段相同实体
        // 前面比较时的中间变量i,j其实已经辅助求出了答案。
        return new int[]{--i, j};
    }
}
