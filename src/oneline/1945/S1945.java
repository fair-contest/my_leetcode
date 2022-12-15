class Solution {
    public int getLucky(String s, int k) {
        return IntStream.range(0, k-1).reduce(s.chars().map(a->a-96).map(b->b/10+b%10).sum(), (x, y)->Integer.toString(x).chars().map(c->c-48).sum());
    }
}
