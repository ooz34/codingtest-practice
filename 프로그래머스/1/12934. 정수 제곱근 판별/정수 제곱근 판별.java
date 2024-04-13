class Solution {
    public long solution(long n) {
        double rn = Math.sqrt(n);
        if(rn == (int)rn){
            return (long)((rn+1)*(rn+1));
            }
        return -1;
    }
}