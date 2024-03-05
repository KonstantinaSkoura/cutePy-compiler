#$Konstantina Skoura AM:4168 #$
#$Konstantinos Retsas AM:4163 #$

def main_factorial():
#{
     #$ declarations #$
     #declare x
     #declare i,fact

     #$ body of main_factorial #$
     x = int(input());
     fact = 1;
     i = 1;
     while (i<=x):
     #{
          fact = fact * i;
          i = i + 1;
     #}
     print(fact);
#}

def main_fibonacci():
#{
     #declare x
     def fibonacci(x):
     #{
          if (x <=1):
               return(x);
          else:
               return (fibonacci(x-1)+fibonacci(x-2));
     #}
     x = int(input());
     print(fibonacci(x));
#}

def main_countdigits():
#{
     #declare x, count
     x = int(input());
     count = 0;
     while (x>0):
     #{
          x = x // 10;
          count = count + 1;
     #}
     print(count);
#}



if __name__ == "__main__":
     #$ call of main functions #$
     main_factorial();
     main_fibonacci();
     main_countdigits();
 
