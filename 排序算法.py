# A冒泡排序(Bubble Sort)
"""
算法描述
- 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
- 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
- 针对所有的元素重复以上的步骤，除了最后一个；
- 重复步骤1~3，直到排序完成。
"""

def bubbleSort(lst):
    n = len(lst)
    if n<=1:
        return lst
    for i in range(0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1]) = (lst[j+1],lst[j])
    return lst

# B快速排序(Quick Sort)
"""
从数列中挑出一个元素，称为 “基准”（pivot）；
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

"""
def QuickSort(lst):
    #此函数完成分区操作
    def partition(arr,left,right):
        key = left # 划分参考数索引，默认第一个数为基准数，可优化
        while left < right:
            #如果列表后边的数，比基准数大或者相等，则前移一位直到比技术小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            #如果列表前边的数，比基数小或者相等，则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            #此时已经找到一个比基准大的数，和一个比基准小的数，将它们互换位置
            (arr[left],arr[key]) = (arr[key],arr[left])
            #返回目前基准所在位置的索引
        return left
    def quicksort(arr,left,right):
        if left >= right:
            return
        #从基准开始分区
        mid = partition(arr,left,right)
        #递归调用
        quicksort(arr,left,mid-1)
        quicksort(arr,mid+1,right)

    #main
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst,0,n-1)
    return lst

#C 插入排序（Insert Sort）
"""
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；
重复步骤2~5。
"""

def InsertSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1,n):
        j=i
        target = lst[i] #每次循环的一个待插入的数
        while j>0 and target<lst[j-1]:
            lst[j] = lst[j-1]
            j = j-1
        lst[j] = target
    return lst

#D 希尔排序（shell Sort）
"""
选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；
每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
分别对各子表进行直接插入排序。
仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
"""
def ShellSort(lst):
    def shellinsert(arr,d):
        n = len(arr)
        for i in range(d,n):
            j = i-d
            temp = arr[i] #记录要出入的数
            while(j>=0 and arr[j]>temp):
                arr[j+d] = arr[j]
                j-=d
            if j!=i-d:
                arr[j+d]=temp

    n = len(lst)
    if n<=1:
        return lst
    d = n//2
    while d>=1:
        shellinsert(lst,d)
        d = d//2
    return lst

#E 简单选择排序(select Sort)
"""
初始状态：无序区为R[1..n]，有序区为空；
第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
n-1趟结束，数组有序化了。
"""
def SelectSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range(0,n-1):
        minIndex = i
        for j in range(i+1,n):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex!=i:
            (lst[minIndex],lst[i]) = (lst[i],lst[minIndex])
    return lst


#F 堆排序(Heap Sort)
"""
将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。
不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
"""
def HeapSort(lst):
    def heapadjust(arr,start,end): #将以start为根节点的堆调整为大顶堆
        temp = arr[start]
        son = 2*start+1
        while son <= end:
            if son<=end and arr[son]<arr[son+1]:
                son += 1
            if temp>=arr[son]:
                break
            arr[start]=arr[son]
            start = son
            son = 2*son+1
        arr[start]=temp

    n=len(lst)
    if n<=1:
        return lst
    #建立大顶堆
    root = n//2-1
    while(root>=0):
        heapadjust(lst,root,n-1)
        root-=1
    i = n-1
    while(i>=0):
        (lst[0],lst[i])=(lst[i],lst[0])
        heapadjust(lst,0,i-1)
        i-=1
    return lst

lst = [4,1,3,7,85,52,43,9]
bs_lst = bubbleSort(lst)
qs_lst = QuickSort(lst)
is_lst = InsertSort(lst)
ss_lst = SelectSort(lst)
print('bubbleSorted:{}'.format(bs_lst))
print('QuickSorted:{}'.format(qs_lst))
print('InsertSorted:{}'.format(is_lst))
print('SelectSorted:{}'.format(ss_lst))
