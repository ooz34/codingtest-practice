class Solution {
    public String solution(String phone_number) {
        int masked = phone_number.length() - 4;
        return "*".repeat(masked) + phone_number.substring(masked);
    }
}