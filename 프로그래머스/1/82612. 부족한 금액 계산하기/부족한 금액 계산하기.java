class Solution {
    public long solution(int price, int money, int count) {
        long sum = 0;
        for(int i=1; i<=count; i++){
            sum += i;
        }
        return (price*sum -money) > 0 ? (long)(price*sum -money) : 0;
    }
}