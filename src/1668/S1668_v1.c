#define MIN(i, j) (((i) < (j)) ? (i) : (j))

bool cmpWord(char* p, int startp, int endp, char* q) {
    for (int i = 0; i < endp-startp; ++i) {
        if (p[startp+i] != q[i]) return false;
    }
    return true;
}

int maxRepeating(char * sequence, char * word){
    int m = strlen(sequence), n = strlen(word);
    if (m < n) return 0;
    int res = 0;
    int i = n, j = m - n + 1, cur = 0;
    for (int k = 0;k < MIN(j, n);++k) {
        if (cmpWord(sequence, k, n+k, word)) {
            res = 1;
            break;
        }
    }
    while (i < j) {
        if (cmpWord(sequence, i-n, i, word)) cur = 1;
        else cur = 0;
        if (cmpWord(sequence, i, i+n, word)) {
            cur++;
            i += n;
            while ((i < j) && (cmpWord(sequence, i, i+n, word))) {
                cur++;
                i += n;
            }
        } else i++;
        if (cur > res) res = cur;
    }
    return res;
}
