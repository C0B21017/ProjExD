import random
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=list(alphabet)
choice_num=8
loss_num=3
chalenge=3

def mondai():
    choiced_num=" ".join(random.sample(alphabet,choice_num))
    choiced_num2=" ".join(random.sample(choiced_num,choice_num-loss_num))
    print("対象文字:"+"\n"+choiced_num)
    print("表示文字:"+"\n"+choiced_num2)
    t_choiced=set(choiced_num)
    t_choiced2=set(choiced_num2)
    return  (t_choiced)-(t_choiced2)

def kaitou(d):
    ans=print(input("欠損文字はいくつありますか？"))
    if ans == len(d):
        for i in range(chalenge):
            a=input(f"{i+1}文字目の文字を入力してください？")
            if a in d:
                d=d-a
                if len(d)==0:
                    print("おめでとう！正解だよ")
            else:
                print("失敗！またチャレンジしてね")

loss=mondai()
kaitou(loss)
            

            

            



