class Solution {
    static int answer = 0;
    static int cnt = 0;
    
    public int solution(String word) {
        String[] vowels = {"A", "E", "I", "O", "U"};
        dfs(vowels, word, "");
        return answer;
    }
    
    public static void dfs(String[] vowels, String word, String str){
        if (str.equals(word)){
            answer = cnt;
            return;
        }
        if (str.length() == 5 || answer != 0){
            return;
        }
        for (String vowel: vowels) {
            cnt++;
            dfs(vowels, word, str + vowel);
            if (answer != 0) {
                cnt--;
            }
        }
    }
}