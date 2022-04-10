#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        //设置 是否完成+1操作的标记
        bool flag = false;
        //设置 指针到最后一位
        int cur = digits.size() - 1;
        // 没有+1 就不停的while
        while (flag == false)
        {
            //判断是不是为9
            if (digits[cur] != 9)
            {
                digits[cur] = digits[cur] + 1;
                flag = true;
            }
            else
            {
                digits[cur] = 0;
                //判断是不是最高位已经满 需要进位
                if (cur == 0)
                {
                    //这边没有想到什么好方法 可以使用原数组进行赋值
                    //所以我只能重新开一个 然后赋值回去
                    vector<int> result;
                    result.push_back(1);
                    for (int i = 0; i < digits.size(); i++)
                    {
                        result.push_back(digits[i]);
                    }
                    digits = result;
                    flag = true;
                }
                else
                {
                    //进位了到前一位+1
                    cur--;
                }
            }
        }
        return digits;
    }
};

//执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
//内存消耗：8.4 MB, 在所有 C++ 提交中击败了88.01%的用户