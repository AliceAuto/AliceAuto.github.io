
# 归并排序

### 分治算法的实现
**在这个模板中可看出:**
> - 分治算法精髓在于：
>    - 问题拆解
>    - 假设性成立

```cpp
const int N =10010;
int tmp[N];

void merge_sort(int q[],int l ,int r){
	if(l>=r)return;
	int mid = (l + r)  >>1;
	merge_sort(q,l,mid);
	merge_sort(q,mid+1,r);
	int k = 0, i = l, j = mid+1;
	while(i<=mid&&j<=r){
		if(q[i]<=q[j])tmp[k++] = q[i++];
		else tmp[k++]= q[j++];
	}
	while(i<=mid)tmp[k++] = q[i++];
	while(j<=r)tmp[k++] = q[j++];
	for(int i = 0,j = l;j<=r;i++,j++) q[j]=tmp[i];
}
```