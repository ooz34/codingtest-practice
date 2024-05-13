class Solution {
    private static int answer = 0;
    private static int cnt = 0;
    
    public int solution(String word) {
        String[] vowels = {"A", "E", "I", "O", "U"};
        dfs(vowels, word, "");
        return answer-1;
    }
    
    public static void dfs(String[] vowels, String word, String str){
        cnt++;
        if (str.equals(word)){
            answer = cnt;
        }
        if (str.length() == 5 || answer != 0){
            return;
        }
        for (String vowel: vowels) {
            dfs(vowels, word, str + vowel);
        }
    }
}