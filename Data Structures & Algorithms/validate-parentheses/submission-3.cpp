class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        if(n==1 || n==0) return false;
        stack<char> st;
        for(int i=0 ; i<n ; i++){
            if(s[i]=='(' || s[i]=='[' ||s[i]=='{'){
               st.push(s[i]);
            }
            if(s[i]==')'){
                if (st.empty()) return false;
                char a = st.top();
                st.pop();
                if(a!='('){
                    return false;
                }
            }
            if(s[i]=='}'){
                if (st.empty()) return false;
                char a = st.top();
                st.pop();
                if(a!='{'){
                    return false;
                }
            }
            if(s[i]==']'){
                if (st.empty()) return false;
                char a = st.top();
                st.pop();
                if(a!='['){
                    return false;
                }
            }
        }
        return st.empty();
    }
};
