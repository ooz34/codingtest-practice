class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int[] answer = new int[str.length()];
        for(int i=str.length()-1, j=0; i>=0; i--, j++){
            answer[j] = Character.getNumericValue(str.charAt(i));
        }
        return answer;
    }
}