#coding:shift-jis

# �f�t�H���g���������p����Ă��ėǂ��ł���
# �ċA�֐��ŃX�}�[�g�ɂ����Ă��Ă����Ǝv���܂�
def fib(n,f0=0,f1=1):
    if n<=1:
        if n==1:
            return f1
        elif n==0:
            return f0
        else:
            return
    else:
        return fib(n-1,f1,f0+f1)

print(fib(10))
