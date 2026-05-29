/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* temp = head;
        unordered_map <Node* , Node*> old_new;
        while(temp!=NULL){
            old_new[temp] = new Node(temp->val);
            temp=temp->next;
        }
        temp = head;
        while(temp!=NULL){
            old_new[temp]->next = old_new[temp->next];
            old_new[temp]->random = old_new[temp->random];
            temp = temp->next;
        }
        return old_new[head]; 
        }
};
