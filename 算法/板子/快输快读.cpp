int I32(){
	char chace = getchar();
	int f= 1;
	int res = 0;
	while (chace -'0'<0||chace - '9'>0){
		if(chace==EOF)return res;
		if(chace == '-')f = -f;
		chace = getchar();
	}
	while(chace -'0'>=0&&chace -'9'<=0)	{
		res= res *10 +chace - '0';
		chace = getchar();
	}
	res *=f;
	return res;
}
long long I64(){    
	char chace = getchar();
	int f= 1;
	long long  res = 0;
	while (chace -'0'<0||chace - '9'>0){
		if(chace==EOF)return res;
		if(chace == '-')f = -f;
		chace = getchar();
	}
	while(chace -'0'>=0&&chace -'9'<=0)	{
		res= res *10 +chace - '0';
		chace = getchar();
	}
	res *=f;
	return res;
}

size_t I64t(){
	char chace = getchar();
	size_t res = 0;
	while (chace -'0'<0||chace - '9'>0){
		if(chace==EOF)return res;
		chace = getchar();
	}
	while(chace -'0'>=0&&chace -'9'<=0)	{
		res= res *10 +chace - '0';
		chace = getchar();
	}
	return res;
}
void O64t(size_t x){
	if(x<10)putchar(x+'0');
	else O64t(x/10),putchar(x%10+'0');
}

void O64(long long x){
	if(x<0)x= -x,putchar('-');
	if(x<10)putchar(x+'0');
	else O64t(x/10),putchar(x%10+'0');
}
void O32(int x){
	if(x<0)x= -x,putchar('-');
	if(x<10)putchar(x+'0');
	else O64t(x/10),putchar(x%10+'0');
}

