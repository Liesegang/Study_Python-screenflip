#coding:shift-jis

def Goldbach(max_n=101, printer=print):

    if max_n<=4:
        return True

    printer(4,2,2)

    if max_n<=6:
        return True

    p_list=[]

    for n in range(3,max_n,2):
        for p in p_list:
            if n%p==0:
                break
            elif n<p**2:
                p_list.append(n)
                break
#       p_list���ŏ��͋�ŁA�����Ƌ�̂܂܂ɂȂ�̂�else��t���܂���
        else:
            p_list.append(n)

    f=True

    for n in range(6,max_n,2):
        for m in p_list:
            M=n-m
            if M in p_list:
                printer(n,m,M)
                break
            elif m>M:
                printer(n, '-', '-')
                f=False
#               �����ł́A��O���������Ă��Ō�܂ő�����悤�ɂ����������̂ŁAf�͎c���܂�
                break
    return f

if __name__=="__main__":
    Goldbach()
