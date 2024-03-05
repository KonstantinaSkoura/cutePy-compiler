#$Konstantina Skoura AM:4168 #$
#$Konstantinos Retsas AM:4163 #$
def main_compute():
#{
	#declare x,z
	def compute(x):
	#{
		#declare k,m,f
		def iscube(num):
		#{
			#declare i,cub
			i = 0;
			cub = 0;
			while (cub < num):
				#{
					i = i + 3;
					f = 7;
					x = x + 1;
						
					cub = i * i * i;
				#}
			if (cub == num):
				return(1); #$if the num is cube returns 1 ,otherwise returns0 #$
			else:
				return(0);
		#}

		#$ main body of compute #$
		k = int(input());
		f = 2;
		m = iscube(k);
		print(f);
		print(m);
		print(x);
		return(m);

	#}
	def issquare(d):
	#{
		#declare p,sq
		p = 0;
		sq = 0;
		while (sq < d):
		#{
			p = p + 1;
			sq = p * p;
		#}
		if (sq == d):
			return (1); #$if the num is square returns 1 ,otherwise returns 0 #$
		else:
			return (0);
	#}
	#$ main body of main_compute #$
	x = 4;
	z = compute(x);
	print(issquare(x));
	
#}


if __name__ == "__main__":
	main_compute();
