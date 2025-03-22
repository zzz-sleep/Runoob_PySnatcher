# Python 数组翻转指定个数的元素

## 题目描述
Python3 实例
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n)将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
以下演示了将数组的前面两个元素放到数组后面。
原始数组:
翻转后：

## 实例 1
### 代码
```python
defleftRotate(arr,d,n):
     foriinrange(d):
         leftRotatebyOne(arr,n)
 defleftRotatebyOne(arr,n):
     temp=arr[0]
     foriinrange(n-1):
         arr[i]=arr[i+1]
     arr[n-1]=temp
 defprintArray(arr,size):
     foriinrange(size):
         print("%d"% arr[i],end=" ")
 arr=[1,2,3,4,5,6,7]
 leftRotate(arr,2,7)
 printArray(arr,7)
```
### 输出结果
```

3 4 5 6 7 1 2

```
## 实例 2
### 代码
```python
defleftRotate(arr,d,n):
     foriinrange(gcd(d,n)):
         temp=arr[i]
         j=i
         while1:
             k=j + d
             ifk>=n:
                 k=k - n
             ifk==i:
                 break
             arr[j]=arr[k]
             j=k
         arr[j]=temp
 defprintArray(arr,size):
     foriinrange(size):
         print("%d"% arr[i],end=" ")
 defgcd(a,b):
     ifb==0:
         returna;
     else:
         returngcd(b,a%b)
 arr=[1,2,3,4,5,6,7]
 leftRotate(arr,2,7)
 printArray(arr,7)
```
### 输出结果
```

3 4 5 6 7 1 2

```
## 实例 3
### 代码
```python
defrverseArray(arr,start,end):
     while(start<end):
         temp=arr[start]
         arr[start]=arr[end]
         arr[end]=temp
         start +=1
         end=end-1
 defleftRotate(arr,d):
     n=len(arr)
     rverseArray(arr,0,d-1)
     rverseArray(arr,d,n-1)
     rverseArray(arr,0,n-1)
 defprintArray(arr):
     foriinrange(0,len(arr)):
         print(arr[i],end=' ')
 arr=[1,2,3,4,5,6,7]
 leftRotate(arr,2)
 printArray(arr)
```
### 输出结果
```

3 4 5 6 7 1 2

```
源链接: [https://www.runoob.com/python3/python3-array-rotation.html](https://www.runoob.com/python3/python3-array-rotation.html)