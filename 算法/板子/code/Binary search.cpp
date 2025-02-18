bool check(int x /*mid*/){
	
	//check the position of res in the right side of mid
	
}

int binary_search(int l/*left*/ ,int r/*right*/) {
	int mid ;
	while(l < r)
	{
		mid = (l+r+1)>>1;
		if(check(mid))//res在mid或其右侧
		{
			l = mid;
		}
		else//res在不包括mid的左侧
		{
			r = mid -1;
		}
	}
	
	
}