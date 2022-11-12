char * customSortString(char * order, char * s){
    int cnt[123];
    for (int i=97;i<123;++i) cnt[i] = 0;
    for (int i=0;i<strlen(s);++i) cnt[s[i]]++;
    int p = 0;
    for (int i=0;i<strlen(order);++i) {
        while (cnt[order[i]]) {
            s[p++] = order[i];
            cnt[order[i]]--;
        }
    }
    for (int i=97;i<123;++i) while (cnt[i]--) s[p++] = i;
    return s;
}
