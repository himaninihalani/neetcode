class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n  = tokens.size();
        int a  = 0;
        int b = 0;
        int c = 0;
        int pushing = 0;
        stack<int> ans;
        for(int i=0;i<n;i++){
           if(tokens[i]=="+" || tokens[i]=="-" || tokens[i]=="*" || tokens[i]=="/"){
            a=ans.top();
            ans.pop();
            b=ans.top();
            ans.pop();
            if(tokens[i]=="+"){
                c = b+a;
            }
            if(tokens[i]=="-"){
                c = b-a;
            }
            if(tokens[i]=="*"){
                c = b*a;
            }
            if(tokens[i]=="/"){
                c = b/a;
            }
            ans.push(c);
           }
           else{
            pushing = std::stoi(tokens[i]);
            ans.push(pushing);
           }
        }
        int final = ans.top();
        return final;
    }
};
