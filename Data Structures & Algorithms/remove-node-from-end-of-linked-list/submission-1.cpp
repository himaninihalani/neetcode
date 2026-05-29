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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
       
        ListNode* temp = head;
        ListNode* prev = NULL;
        int cnt  = 0;
        while(temp!=NULL){
            cnt++;
            temp=temp->next;
        }
        if(n==1 && cnt==1) return NULL;
        int n1 = cnt - n;
        if(n1==0){
        ListNode* newHead = head->next;
        delete head;
        return newHead;
        }
        temp = head;
        int j = 0;
        while(temp!=NULL && j<=cnt){
            if(j == n1){
              prev->next = prev->next->next;  
             }
            j++;
            prev = temp;
            temp = temp->next;
        }
        return head;
    }
};
