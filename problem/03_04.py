#coding:shift-jis

def Goldbach(max_n=101, printer=print):

    if max_n<=4:
        return True

    printer(4,2,2)

    if max_n<=6:
        return True

    p_list=[]

    for n in range(3,max_n,2):
        flag=True
        for p in p_list:
            if n%p==0:
                flag=False
                break
            elif n<p**2:
#               p_list.append(n) �������ł�����C�t���O�𗧂ĂȂ��Ă��݂���
                break
        if flag==True:
            p_list.append(n)

    f=True

    for n in range(6,max_n,2):
        flag=False
        for m in p_list:
            M=n-m
            if M in p_list:
                printer(n,m,M)
                flag=True
                break
            elif m>M:
#               printer(n, '-', '-')
#               f=False
#               return False �Ƃ��΁C�t���O���S������Ȃ��Ȃ肻��
                break
        if not flag:
            printer(n,'-','-')
            f=False
#   return True
    return f

# �t���O���g���ƁC�ǂ݂ɂ����R�[�h���ł��邱�Ƃ������̂ŁC�t���O�𗧂ĂȂ��čςޕ��@���Ȃ��������l����Ȃ�����Ƃ�����������Ȃ��ł�

if __name__=="__main__":
    Goldbach()
