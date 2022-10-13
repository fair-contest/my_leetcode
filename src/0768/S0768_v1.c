int maxChunksToSorted(int* arr, int arrSize){
    int *rec = malloc(sizeof(int) * (arrSize+1));
    rec[0] = 0;
    int cur = arr[0];
    int p = 0;
    for (int i = 0; i < arrSize; i++) {
        while (arr[i] < rec[p]) p--;
        if (arr[i] > cur) cur = arr[i];
        rec[++p] = cur;
    }
    free(rec);
    return p;
}
