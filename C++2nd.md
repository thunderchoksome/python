#C++2nd
##循环
- ***while循环***

``` 

  	while(condition)
  	 {
  		 statement(s);
  	 }
```

条件为真时执行循环

+ ***for循环***


```

  	for ( init; condition; increment )  
	{
   		statement(s);
	}
```

init 会首先被执行，且只会执行一次。

+ ***do...while循环***

```

  	do
	{
   		statement(s);

	}while( condition );
```

循环中的 statement(s) 会在条件被测试之前至少执行一次。

+ 定义函数

```

     return_type function_name( parameter list )

     {

   		body of the function

	 }
```

+ ***Lambda匿名函数***

```

 	[capture](parameters)->return-type{body}
```
例如：
```
	
	[](int x, int y){ return x < y ; }
```

+ ***C++ 随机数***
  
  随机数生成器，有两个相关的函数。一个是 rand()，该函数只返回一个伪随机数。生成随机数之前必须先调用 srand() 函数。

+ ***C++ 中的 String 类***
  
```

	 // 复制 str1 到 str3
  		str3 = str1;
  		
  	 // 连接 str1 和 str2
   		str3 = str1 + str2;
   		;
 
   	 // 连接后，str3 的总长度
   		len = str3.size();
```

string类提供了一系列针对字符串的操作，比如：

 1. append() -- 在字符串的末尾添加字符
 2. find() -- 在字符串中查找字符串
 3. insert() -- 插入字符
 4. length() -- 返回字符串的长度
 5. replace() -- 替换字符串
 6. substr() -- 返回某个子字符串

等等


* ***C++ 指针***

	使用指针时会频繁进行以下几个操作：定义一个指针变量、把变量地址赋值给指针、访问指针变量中可用地址的值。这些是通过使用一元运算符 * 来返回位于操作数所指定地址的变量的值

```

	#include <iostream>
 
	using namespace std;
 
	int main ()
	{
  	 int  var = 20;   // 实际变量的声明
   	 int  *ip;        // 指针变量的声明
 
   	 ip = &var;       // 在指针变量中存储 var 的地址
 
     cout << "Value of var variable: ";
     cout << var << endl;
 
     // 输出在指针变量中存储的地址
     cout << "Address stored in ip variable: ";
     cout << ip << endl;
 
     // 访问指针中地址的值
     cout << "Value of *ip variable: ";
     cout << *ip << endl;
 
     return 0;
	}

```
输出结果为：

Value of var variable: 20

Address stored in ip variable: 0xbfc601ac

Value of *ip variable: 20

在指针变量声明的时候，如果没有确切的地址可以赋值，为指针变量赋一个 NULL 值是一个良好的编程习惯。赋为 NULL 值的指针被称为空指针。
NULL 指针是一个定义在标准库中的值为零的常量。

注意：假设 ptr 是一个指向地址 1000 的整型指针，是一个 32 位的整数，让我们对该指针执行下列的算术运算：ptr++  
则ptr 将指向位置 1004，因为 ptr 每增加一次，它都将指向下一个整数位置，即当前位置往后移 4 个字节

另外，C++ 指向指针的指针（多级间接寻址）：int **var;


