public class Solution {
    public bool IsStrictlyPalindromic(int n) {
        for (int i = 2; i <= n - 2; i++)
        {
            string baseStr = convertNumber2Base(n, i);
            bool isPalindrom = checkPalindrom(baseStr);
            if (!isPalindrom)
            {
                return false;
            }
        }
        return true;
    }

    private string convertNumber2Base(int n, int b)
    {
        string str = "";
        while (n != 0)
        {
            str += (n % b).ToString();
            n = n / b;
        }
        return str;
    }

    private bool checkPalindrom(string str)
    {
        for(int i = 0; i < str.Length / 2; i++)
        {
            if (str[i] != str[str.Length - i - 1])
            {
                return false;
            }
        }
        return true;
    }
}