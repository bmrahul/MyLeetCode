public class Solution {
    public int RomanToInt(string s) {
        int total = 0;
        Dictionary<char, int> romanNumberDictionary = new Dictionary<char, int>() {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };

        for(int i = 0; i < s.Length; i++) {
            char currentRomanChar = s[i];
            romanNumberDictionary.TryGetValue(currentRomanChar, out int num);
            if(s.Length > i + 1 && romanNumberDictionary[s[i + 1]] > romanNumberDictionary[currentRomanChar])
            {
                total -= num;
            }
            else 
            {
                total += num;    
            }
        }
        return total;
    }
}