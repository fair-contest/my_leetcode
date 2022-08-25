class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;
        int[] arr = new int[26];
        for (char m : magazine.toCharArray()) arr[m - 'a']++;
        for (char r : ransomNote.toCharArray()) {
            if (arr[r - 'a'] == 0) return false;
            arr[r - 'a']--;
        }
        return true;
    }
}
