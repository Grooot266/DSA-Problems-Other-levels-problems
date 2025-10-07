class Solution {
    public String reverseVowels(String s) {
        int n=s.length(); 
        char[] ch = s.toCharArray();
        int start = 0;
        int end = s.length()-1;

        while(start < end){
            if(!isVowel(ch[start])){
                start++;
            }
            else if(!isVowel(ch[end])){
                end --; 
            }
            else{
                char temp = ch[start];
                ch[start] = ch[end];
                ch[end] = temp;
                start ++;
                end -- ; 

            }
        }
        return String.valueOf(ch);

    }

    public static boolean isVowel(char ch){
        if(ch=='A' || ch=='a' || ch=='E' || ch=='e' || ch=='I' || ch=='i' || ch=='O' || ch=='o' || ch == 'U'|| ch =='u'){
            return true;
        }
        return false ;
    }
}