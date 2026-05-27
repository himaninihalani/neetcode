/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        stack<ListNode*> st;
        ListNode* front = head;
        while(front!=NULL){
            st.push(front);
            front=front->next;
        }
        ListNode* temp = head;
        int half_size = st.size() / 2;
        for(int i = 0; i < half_size; i++){
            ListNode* fron = temp->next;
            temp->next = st.top();
            st.pop();
            temp = temp->next;
            temp->next=fron;
            temp = temp->next;
           }
           if(temp!=NULL){
            temp->next = NULL;
           }
    }
};