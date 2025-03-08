
```cpp
/*
pointer sequence: |h1_p h2_p ··· hn_p|: the pointer sequence table

                         ↓ptr

relational table: | p_1 p_2 p_3 ... p_n |: the relation between elems to Bucket sequence table
            
                       ↓index

            data: | d_1 d_2 d_3... d_n  |
*/

const int N = 1e5+10;
int h[N] ,e[N],ne[N],idx;
```