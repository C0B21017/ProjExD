import random
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=list(alphabet)
all_num=26
choice_num=8
loss_num=3

def mondai():
    choiced_num=random.sample(alphabet,choice_num)
    print("対象文字:"+"\n"+" ".join(choiced_num))
    #print("表示文字:"+"\n"+???)

mondai()
#print("対象文字:"+"\n"+choiced_num)
#ans=print(input("欠損文字はいくつありますか？"))
#if ans == loss_num:
# def kaitou(n):
#     if ans==len:
#         while True:
            



