#include <iostream>
using namespace std;
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        // 设置一个小于这个范围的数字 -101
        ListNode *preHead = new ListNode(-101);
        // 设置当前节点
        ListNode *prev = preHead;
        // 判断是否为空
        while (list1 != nullptr && list2 != nullptr)
        {
            // 看list1 和 list2 哪个小
            if (list1->val < list2->val)
            {
                prev->next = list1;
                list1 = list1->next;
            }
            else
            {
                prev->next = list2;
                list2 = list2->next;
            }
            // 移除前一个 让下一个等待被插入
            prev = prev->next;
        }

        // 合并后 list1 和 list2 最多只有一个还未被合并完
        // 我们直接将链表末尾指向未合并完的链表
        prev->next = list1 == nullptr ? list2 : list1;

        return preHead->next;
    }
};

//执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
//内存消耗：14.4 MB, 在所有 C++ 提交中击败了52.19%的用户