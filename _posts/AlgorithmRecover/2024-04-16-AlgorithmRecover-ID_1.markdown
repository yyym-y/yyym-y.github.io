---
layout : post
title : "算法复健::ID_1"
githubUrl : ""
pdfUrl : "/pdf/"
cover : "/assets/cover/"
previousUrl : ""
nextUrl : ""
---
* awsl
{:toc}


#  D. Another Problem About Dividing Numbers

题目传送门 : https://codeforces.com/problemset/problem/1538/D

复健后第一道成功 AC 的题, 好像还是 [普及+/提高]

我们先分析特殊情况, 如果 $c = 1$ 的时候, 那么如果可以, 那么要么 $a = kb$ 成立或者 $b = ka$ 成立

> 注意, $c = 1$ 的时候 $a, b$ 不能相等, 即 $k \ne 1$, 因为题目要求 $c > 1$

所以如果 $c = 1$ ,如果有一方是另一方的倍数, 且 $a,b$ 不相等那么就可以, 否则一定不行

接下来分析 $c \ne 1$ 的情况, 我们知道最少需要两步就一定可以让两个数相等

那就是 $a$ 除 $b$, $b$ 除 $a$

我们就考虑如何能将 $a$ 和 $b$ 拆分成 $k$ 个数相乘就可以得到最大的拆分次数了

$k$ 的最大值可以用分解质因数获得, 直接分解会超时, 所以我们将质数打表即可

```c++
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

vector<lli>info;
bitset<lli(1e8 + 10)> Check;
void Euler_sieve(lli Limit){
    for(lli temp = 2 ; temp <= Limit ; temp++){
        if(Check[temp] == 0) info.push_back(temp);
        for(lli temp2 = 0 ; temp*info[temp2] <= Limit ; temp2++){
            Check[temp*info[temp2]] = 1;
            if(temp % info[temp2] == 0) break;
        }
    }
}

void solve() {
    lli a, b, c;
    cin >> a >> b >> c;
    if(c == 1) {
        if(max(a, b) % min(a, b) == 0 && a != b) cout << "YES\n";
        else cout << "NO\n";
        return;
    }
    lli count1 = 0, count2 = 0;
    for(int i = 0 ; i < info.size() && info[i] * info[i] <= a ; i ++) {
        while (a % (info[i]) == 0) {
            count2 ++; a /= info[i];
        }
    }
    if(a != 1) count2 ++;
    for(int i = 0 ; i < info.size() && info[i] * info[i] <= b ; i ++) {
        while (b % info[i] == 0) {
            count1 ++; b /= info[i];
        }
    }
    if(b != 1) count1 ++;
    if(c > count1 + count2) {
        cout << "NO\n"; return;
    }
    if(c == 1 && (count1 && count2)) {
        cout << "NO\n"; return;
    }
    cout << "YES\n";
}

signed main()
{
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    lli ask; cin >> ask;
    Euler_sieve(1e5);
    while (ask --)
        solve();
    return 0;
}
```

# D. Sum of XOR Functions

题目链接: https://codeforces.com/problemset/problem/1879/D

第二道过的题目, 好像也是 [普及+/提高], 感觉写起来挺 caodan 的

思路倒是不是很困难的想出来, 但是写起来巨麻烦和恶心, 一直在理清自己的思路

但这好像有套路 (感觉可以回去看看题解总结一下) : https://www.luogu.com.cn/problem/solution/CF1879D

具体的做法就是 :

每一位算贡献, 计算这一位在答案中总共被加上了多少次

我们重点关注从 $[a_0, a_1, a_2] \Rightarrow [a_0, a_1, a_2, a_3]$ 增加的值

假设我们有一个序列 $[1, 0, 1, 0]$, 我们用递推的思维简单看一下:

> $[1]$ : 答案就是 $1$
>
> $[1,0]$ : 相比于上一个序列增加了 $1\times0 + 2\times1$
>
> $[1,0,1]$ : 相比于上一个序列增加了 $1\times1 + 2\times1 + 3\times0$
>
> $[1,0,1,0]$ : 相比于上一个序列增加了 $1\times0 + 2\times1 + 3\times1 + 4\times0$

到这里规律其实就很明显了, [不想说了, 自己看....]

所以难写的点在于怎么滤清需要什么变量来维护这些变化

直接上代码吧:

```c++
#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
lli len;
const int N = 5e5;
const int P = 998244353;

lli arr[N];
lli bit[33][N];

lli queryNum(int pos) {
    lli ans = bit[pos][1] ? 1 : 0;
    lli last_add = bit[pos][1] ? 1 : 0;
    lli one_num = bit[pos][1] ? 1 : 0;
    lli sum = 1;
    for(int i = 2 ; i <= len; sum += i, i ++, sum %= P) {
        lli add = 0;
        if(bit[pos][i] == 0) {
            add = last_add + one_num;
            add %= P;
        }else {
            lli tem = (sum - last_add + P) % P;
            tem %= P;
            one_num = (i - one_num - 1 + P) % P;
            add = (tem + one_num) % P;
            one_num ++; add ++;
            one_num %= P; add %= P;
        }
        ans += add;
        ans %= P;
        last_add = add;
    }
    return ans;
}

signed main()
{
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    cin >> len;
    for(int i = 1 ; i <= len ; i ++) cin >> arr[i];
    for(int i = 0 ; i <= 32 ; i ++) {
        for(int j = 1 ; j <= len ; j ++)
            bit[i][j] = arr[j] >> i & 1;
    }
    lli ans = 0;
    for(int i = 0 ; i <= 32 ; i ++) {
        lli num = queryNum(i); num %= P;
        ans += (num * ((1LL << i) % P)) % P;
        ans %= P;
    }

    cout << ans << "\n";
    return 0;
}
```

