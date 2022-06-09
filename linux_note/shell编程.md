> Bash Shell 脚本

#!/bin/bash

bash hello.sh

ksh hello.sh

### 文本编辑器

#### 分类

字符界面编辑器 图形界面编辑器

#### vi/vim

Unix标准，所有兼容POSIX的系统中都包含该工具，消耗系统资源少，字符界面无需鼠标，包含有完整的内置用户手册

#### Emacs

宏编辑器

#### nano

小巧易用的全功能文本编辑器

Pico的复制品clone

遵守GNU GPLv3许可证

#### gedit

#### sublime

### 普通变量

#### 数据类型

只有一种数据类型——字符串

#### 变量声明 变量名

不用声明 或者 declare

字母开头，字母数字下划线，不能使用保留字

#### 变量取值

\$a

\${a}

echo \$a

echo "\$a"

echo "${a}" 

#### 变量赋值

[let] var=value  note: no space beside =

a?

a:?Info 自定义提示

a:=value 变量为空时赋值

a:-value 变量为空，临时赋值

a:+value 变量不为空，临时赋值

#### 清空变量

unset

#### 只读变量

readonly var

readonly show all read-only var singly

### 位置变量

\$0  启动脚本的命令

\$1, ..., \$9 命令后跟的值

超过9个时候使用shift，向左移一位

使用 \${10}, \${11} ...

直接赋值

set 1 2 3 4 5 6 7 8 9

### 特殊变量

#### \$?

最后一条命令状态

每条命令执行都有状态 0成功 1失败 2错误

与条件表达式的成立与否有区别

echo查看

#### \$#

传递给script的参数的个数

#### \$*

用一个单字符串显示所有script的参数，可以超过9个

### 输入输出 表达式

#### read

read ans

echo -n "plz enter username: "; read name

read -p "plz enter username: " name

无变量名输入 \$ENTER

read会一直等待用户输入

-t 指定等待秒数 正常输入返回零 计数满返回非零

read -t 5 -p "plz enter username: " name

-n 限制输入字符数达到就退出

read -n 1 -p "yes/no[y/n]: " ch

-s 静默输入，屏幕上不显示用户输入

read -s -p "plz enter password: " pswd

#### echo

输出字符串 带转义字符的字符串

echo "\\"Today is a good day. \\""

echo \$a

-n 不换行 disables output of the trailing new line

-e 显示特殊转义字符 enable interpretations of the backslash escaped characters

"" 任何取值

'' 原样输出

`` 执行命令

#### 特殊转义字符

\\b backspace

\\c inhibit the terminating newline

\\n carriage return and a line feed(newline)

\\r carriage return without the feed

\\t horizontal tab

\\v vertical tab

#### expr

\+ \- \* /

整数运算，注意空格。

expr 1 + 2

expr 1 - 2

expr 1 \\\* 2

expr 1 "\*" 2

#### let

注意空格

let a=\$a+1

let c=\$a*\$b

#### 算术扩展

((a=a+1))

a=$((a*5))

echo $((a=(a+5)*(j=4+3)))

#### bc

apt install -y bc

echo "3\*5" | bc

var=\$(echo "63/23" | bc)

echo "scale=4; 3\*8/7; last\*5" | bc

m=31; n=\$(echo "obase=16; \$m" | bc); echo \$n

m=1E; n=\$(echo "obase=10; ibase=16; \$m" | bc); echo \$n

#### test

字符比较 = > >= < <= != z n

\$? 0成功为真 1失败为假

变量可能为空，需加双引号

-n 变量非空 命令成功

-z 变量为空 命令成功

数值比较 eq lt le gt ge ne

-eq equal

文件

-f 测试文件

test \-f ~/test/file1; echo \$?

-d 测试目录

test \-d /etc ; echo \$?

-r -w -x 测试文件存在及权限

-nt -ot 比较两个文件的日期先后

file1 -nt file2

复合条件测试

-a and

-o or

test \$age -gt 10 -a \$age -lt 20

test \$age -lt 10 -o \$age -gt 20

test \$age -gt 10 && test \$age -lt 20

test \$age -lt 10 || test \$age -gt 20

test 可以用 []

test "\$a" = "\$b"

["\$a" = "\$b"]

test \$age -gt 10 -a \$age -lt 20

["\$age" -gt 10 -a "\$age" -lt 20]

#### 命令成功与条件表达式的关系

1 条件表达式成立 命令不成功

0 条件表达式不成立 命令成功

### 语块

#### if

```shell
if command; then
	commands
fi
```



```shell
if command
then
	commands
else
	commands
fi
```



```shell
if command
then
commands
elif command
then
	commands
elif command
then
	commands
else
	commands
fi
```



#### mymk

```bash
#!/bin/bash
read fname
vim $fname
chmod u+x $fname
./$fname
```



```bash
#!/bin/bash
vim "$1"
chmod u+x ""$1"
./"$1"
```



```bash
#!/bin/bash
if [ -n "$1"]
then
    vim "$1"
	chmod u+x ""$1"
    ./"$1"
fi
```



```bash
#!/bin/bash
if [ -n "$1"]
then
    vim "$1"
    if [-e "$1"]; then
		chmod u+x ""$1"
    	./"$1"
    fi
fi
```



#### case

```shell
case $var in
	value1)
		commands;;
	value2)
		commands;;
	*)
		commands;;
esac
```



#### cal

display a calendar

cal 2022

cal 5 2022

```bash
#!/bin/bash
case $# in
	0) set `date`; m=$2; y=$6;;
	1) m=$1; set `date`; y=$6;;
	*) m=$1; y=$2;;
esac

case $# in
	jan*|Jan*) m=1;;
	feb*|Feb*) m=2;;
	mar*|Mar*) m=3;;
	apr*|Apr*) m=4;;
	may*|May*) m=5;;
	jun*|Jun*) m=6;;
	jul*|Jul*) m=7;;
	aug*|Aug*) m=8;;
	sep*|Sep*) m=9;;
	oct*|Oct*) m=10;;
	noc*|Nov*) m=11;;
	dec*|Dec*) m=12;;
	[1-9]|10|11|12) ;;
	*) y=$m; m="";;
esac

cal $m $y
```



#### for

```shell
for var in valuelist
do
	commands
done
```



```bash
#!/bin/bash
for num in 1 2 3 4 5
do 
	echo $num
done
```



```shell
for num in 1 2 3 4 5; do echo $num; done
```



```bash
#!/bin/bash
for num in {1..5}
do 
	echo $num
done
```



```bash
#!/bin/bash
for num in `seq 1 1 5`
do 
	echo $num
done
```



```shell
for ((exp1; exp2; exp3))
do
	commands
done
```



```shell
for((num=1; num<=5; num++)); do echo $num; done
```



#### while

```shell
while command
do
	commands
done
```



```bash
#!/bin/bash
count=10
while[$count -ge 0]
do 
	echo $count
	count=`expr $count - 1`
done
```



```bash
#!/bin/bash
count=10
while((count>=0))
do 
	echo $count
	((count--))
done
```



```bash
#!/bin/bash
i=1
cat "$1" | while read line
do
	echo "$i: $line"
	((i++))
done
```



```bash
#!/bin/bash
if [-f "$1"]; then
	i=1
    cat "$1" | while read line
    do
        echo "$i: $line"
        ((i++))
    done
fi
```



#### until

直到表达式成功

```shell
until command
do
	commands
done
```



```shell
until who | grep "$1" > /dev/null 2>&1
do 
	sleep 30
done
echo "Becareful, $1 is online now!"
```

第一个重定向是把标准输出重定向

2>&1 是把标准错误输出重定向

/dev/null 系统的一个设备文件，所有传送进去的数据都直接丢弃，系统垃圾堆。

该用户没有登录，命令不成功就是一直执行循环。一旦用户出现在列表中命令就成功，此时退出循环。

#### who

显示当前登录的用户

#### select

```shell
select var in menu
do
	commands
done
```

select后面跟变量名，in关键字后面是菜单取值，以空格隔开

用户选择数字对应菜单值

变量var获取值后执行循环一次

```bash
select m in new insert modify delete
do 
	echo $m
done
```



```bash
#!/bin/bash
PS3="plz select[1-4]: "
select m in new insert modify delete
do 
	echo $m
done
```



```bash
#!/bin/bash
PS3="plz select[1-4]: "
select m in new insert modify delete
do 
	break
done
echo $m
```

Ctrl+C则推出脚本

#### func

函数

```shell
function Func_name(){
	func_body
}
```

```shell
function Func_name()
{
	func_body
}
```

括号中没有参数，关键字function可以不写

要求函数的定义在调用之前

函数的参数利用位置变量传递

直接写函数名调用

```bash
#!/bin/bash

func1(){
	echo hello1
}
func2(){
	echo hello2
}
func1
func2
```

函数载入可以用点命令

```bash
func1(){
	echo hello1
}
func2(){
	echo hello2
}

# this is funcfile
```

```bash
#!/bin/bash

. ./funcfile
func1
func2
```

没有形参，传入参数使用位置变量

set 查看当前内存中已经定义和载入的函数

unset清除函数

函数修改以后必须重新载入（内存）

