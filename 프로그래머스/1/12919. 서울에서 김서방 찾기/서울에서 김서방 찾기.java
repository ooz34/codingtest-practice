import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(String[] seoul) {
        int idx = Arrays.stream(seoul).collect(Collectors.toList()).indexOf("Kim");
        return "김서방은 " + idx + "에 있다";
    }
}