#八皇后问题
num=8
count=0
#存放标记的列表
place=[0 for x in range(num)]#放置标志。表示皇后放置在第row行的的col列,place[1]=0表示第2行的第1列放置了一个皇后

#定义行和列以及对角线不能防止的标志
flag=[0 for x in range(num)]#若flag[]==1，则表示第n列被标记了。
diah=[0 for x in range(num*2-1)]#上对角线，表示对角线也被标记了，num*num个棋盘上共有num*2-1个上对角线。
dial=[0 for x in range(num*2-1)]#下对角线，表示对角线也被标记了，num*num个棋盘上共有num*2-1个下对角线。

#定义一个打印函数
def printf(place):
    for i in range(num):
        for j in range(num):
            if place[i] == j:
                print('*', end=' ')
            else:
                print('无', end=' ')
        print('')
    print('')
#定义查找函数search（）,以行为基础进行列搜索
def search(row):
    global count
    for col in range(num):
        if flag[col]==0 and diah[col+row]==0 and dial[row-col+num-1]==0:#要是列以及对角线没有被标记,则进行放置皇后
            place[row]=col#防止一个皇后
            #放置后要进行标记
            flag[col] = 1
            diah[col+row]=1
            dial[row-col+num-1]=1
            if row == (num-1):#到达最后一行
                count+=1
                printf(place)
            else:
                search(row+1)
            #回溯部分,若是在某一行中出现了无法放置的部分，则需要将标志清零，回溯至上一行中进行后面一列的放置尝试
            flag[col] = 0
            diah[col+row] = 0
            dial[row-col+num-1] = 0
print('放置方案如下：')
search(0)
print(num,'皇后总共放置方法有',count,'种')



