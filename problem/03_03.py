#coding:shift-jis
# �ǂ��ł��� ���Ɍ������Ƃ��Ȃ������ł�
for n in range(1,101):
    if n%15==0:
        print("Fizz Buzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)
