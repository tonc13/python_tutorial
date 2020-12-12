import random

defo_hand_list = ["ブタ","ワンペア","ツーペア","スリーカード","ストレート","フラッシュ","フルハウス","フォーカード","ストレートフラッシュ","ロイヤルストレートフラッシュ"]
defo_design_list = ["♡", "♢", "♤", "♧"]

#山札の生成
def deck_generation():
    deck = []
    for a in range(1,14):
        for b in range(4):
            deck.append(defo_design_list[b] + str(a))
    return deck

#手札の配布
def hand_distribution(deck,hand,num):
    for a in range(num):
        i = random.randint(0,len(deck)-1)
        hand.append(deck[i])
        deck.pop(i)
    return hand,deck

def func(hand):
    return int(hand[1:])

#手札の整理
def hand_organize(hands):
    new_number_folder = sorted(hands,key=func)
    return new_number_folder

#リストと各要素の割合を示すリストから乱数によって要素を決定
def gen_prop(list, rate_list):
    S=0
    for a in range(0,len(rate_list)):
        S += rate_list[a]
    r = random.uniform(0,S)
    S = 0
    for k in range(0,len(rate_list)):
        S += rate_list[k]
        if r < S:
            number = k
            return list[number]
    number = len(rate_list)-1
    return list[number]

#cpuの役決め
def cpu_hand(level):
    if level == 1:
        rate_list = [30,55,5,8,2,2,2,1,0,0]
    if level == 2:
        rate_list = [20,45,5,10,2,2,3,1,0,0]
    if level == 3:
        rate_list = [5,25,7,15,3,3,6,1,1,1]
    if level == 4:
        rate_list = [0,1,5,10,15,15,35,5,5,5]
    hand = gen_prop(defo_hand_list, rate_list)
    if hand == "ロイヤルストレートフラッシュ":
        return (hand)
    else:
        number = str(random.randint(1,13))
        return (number + "の" + hand)

#手札から役を判断する
def confirm(hand):
    design_list = []
    number_list = []
    hand_record = [True, False, False, False, False, False, False, False, False, False]

    #手札のカードを数と絵柄に分ける
    for a in range(5):
        design = hand[a][-1]
        number = int(hand[a][:-1])
        design_list.append(design)
        number_list.append(number)
        number_list = sorted(number_list)

    #絵柄が揃っているかどうかを判断する
    for a in range(4):
        confirm_list = [defo_design_list[a]] * 5
        if design_list == confirm_list:
            hand_record[5] = True
    
    #ストレートかどうかを判断する
    for a in range(1,14):
        confirm_list = []
        for b in range(5):
            c = a + b
            if c > 13:
                c = c - 13
            confirm_list.append(c)
        if sorted(number_list) == sorted(confirm_list):
            hand_record[4] = True

    #(ロイヤル)ストレートフラッシュかどうかを判断する
    if (hand_record[4] and hand_record[5]):
        if (10 in number_list) and (1 in number_list):
            hand_record[9] = True
        else:
            hand_record[8] = True

    #ペアがあるかどうかを判断する
    count = 0
    for a in range(1,14):
        if count < number_list.count(a):
            count = number_list.count(a)
    if count == 2:
        hand_record[1] = True
    if count == 3:
        hand_record[3] = True
    if count == 4:
        hand_record[7] = True

    #フルハウスかどうか判断する
    if hand_record[3]:
        for a in range(1,14):
            if number_list.count(a) == 2:
                hand_record[6] = True

    #ツーペアかどうかを判断する
    if hand_record[1]:
        count = 0
        for a in range(1,14):
            if number_list.count(a) == 2:
                count += 1
        if count == 2:
            hand_record[2] = True

    if hand_record[9]:
        return (defo_hand_list[9])
    if hand_record[8]:
        num = str(number_list[4])
        return (num + "の" + defo_hand_list[8])
    if hand_record[7]:
        count = 0
        for a in range(1,14):
            if number_list.count(a) == 4:
                num = str(a)
        return (num + "の" + defo_hand_list[7])
    if hand_record[6]:
        for a in range(1,14):
            if number_list.count(a) == 3:
                num = str(a)
        return (num + "の" + defo_hand_list[6])
    if hand_record[5]:
        num = str(max(number_list))
        return (num + "の" + defo_hand_list[5])
    if hand_record[4]:
        num = str(max(number_list))
        return (num + "の" + defo_hand_list[4])
    if hand_record[3]:
        for a in range(1,14):
            if number_list.count(a) == 3:
                num = str(a)
        return (num + "の" + defo_hand_list[3])
    if hand_record[2]:
        num = 0
        for a in range(1,14):
            if number_list.count(a) == 2:
                if num < a:
                    num = a
        num = str(num)
        return (num + "の" + defo_hand_list[2])
    if hand_record[1]:
        for a in range(1,14):
            if number_list.count(a) == 2:
                num = str(a)
        return (num + "の" + defo_hand_list[1])
    if hand_record[0]:
        num = str(max(number_list))
        return (num + "の" + defo_hand_list[0])


print("ポーカーゲームを始めます。")
print()
x = 0
while (x != 1) and (x != 2):
    try:
        x = int(input("ルール説明を見ますか?(はい:1,いいえ:2)"))
    except:
       print("正しい入力ではありません。")
    else:
        if x == 1:
            print()
            print(" <ルール説明>")
            print("ポーカーは、5枚の手札の組み合わせでカードの強さを競うトランプゲームです。")
            print("・最初に、トランプカードが5枚配られます。")
            print("・その後手札を見て、決められた組み合わせを作るためにカードを山札と交換します。")
            print("　1回に交換するカードの枚数は任意ですが、交換の回数には上限があります。")
            print("・お互いが交換をやめる,または交換の上限に達したら、役を見せ合い勝敗を決定します。")
            print("　お互いに役が同じの場合は、数字の大きさで勝敗を決める事とします。")
            print()
        elif x == 2:
            print("分かりました。")
            print()
        else:
            print("正しい入力ではありません。")
x = 0
while (x != 1) and (x != 2):
    try:
        x = int(input("役一覧を見ますか?(はい:1,いいえ:2)"))
    except:
       print("正しい入力ではありません。")
    else:
        if x == 1:
            print()
            print(" <役一覧(弱い順)>")
            print("「ブタ」：何も役が揃ってない状態。ブタ同士は五枚の中で一番強い数で勝負。/[*,*,*,*,*]")
            print("「ワンペア」：同じ数が二枚ある状態。数字の強さ勝負になりがち。/[♡1,♢1,*,*,*]")
            print("「ツーペア」：ワンペアが二組ある状態。そんなに見ない。/[♡1,♢1,♡4,♢4,*]")
            print("「スリーカード」：同じ数が三枚ある状態。上の役を狙いやすい。/[♡2,♢2,♤2,*,*]")
            print("「ストレート」：五枚の数字が続いてる状態。下手に狙うとブタになる。/[♡12,♤13,♧1,♡2,♢3]")
            print("「フラッシュ」：五枚の模様が揃ってる状態。下手に狙うとブタになる。/[♡1,♡3,♡7,♡8,♡11]")
            print("「フルハウス」：ワンペア＋スリーカード。意外とみる。/[♡2,♢2,♤2,♡5,♧5]")
            print("「フォーカード」：同じ数が四枚ある状態。ジョーカーなしだときつい。/[♡2,♢2,♤2,♧2,*]")
            print("「ストレートフラッシュ」：ストレート＋フラッシュ。名前かっこいい。/[♡3,♡4,♡5,♡6,♡7]]")
            print("「ロイヤルストレートフラッシュ」：5枚が10・J・Q・K・Aのフラッシュ。あがったら死ぬ。/[♡10,♡11,♡12,♡13,♡1]")
            print()
        elif x == 2:
            print("分かりました。")
            print()
        else:
            print("正しい入力ではありません。")
            print("""
            a
            b
            """)

change = -1
print("今回は山札にジョーカーはありません。(そんなプログラム無理)")
print("また、数字の強さは1が最弱、13が最強とします。(プログラムを簡単にするため)")
while not change >= 0:
    try:
        change = int(input("手札の交換の上限をいくつにしますか?"))
    except:
        print("正しい入力ではありません。")
    else:
        if change >= 0:
            print("分かりました。")
            print()
        else:
            print("正しい入力ではありません。")

level = 0
# while  (level != 1) and (level != 2) and (level != 3) and(level != 4):
while   all([level != i for i in range(1,5)])
    try:
        level = int(input("cpuのレベルはどうしますか?(よわい:1, ふつう:2, つよい:3, 最強:4)"))
    except:
       print("正しい入力ではありません。")
    else:
        # if (level  == 1) or (level  == 2) or (level  == 3) or (level  == 4):
        if level in range(1,5):
            print("分かりました。")
            print()
        else:
            print("正しい入力ではありません。")

print("では始めます。")
deck = deck_generation()

print("まずあなたの手札を配ります。")
print()
hand = []
record = hand_distribution(deck,hand,5)
hand = hand_organize(record[0])
deck = record[1]
print(hand)

count = 0
while change != count:
    x = 0
    while (x != 1) and (x != 2):
        try:
            x = int(input("手札を交換しますか?(残り回数は{}回)(はい:1,いいえ:2)".format(change-count)))
        except:
            print("正しい入力ではありません。")
        else:
            if x == 1:
                
                change_card = []
                while (len(change_card) <= 0):
                    print()
                    print("交換したいカードの順番を入力して下さい。")
                    print("(例：[11♢, 12♡, 12♢, 1♧, 4♢]で[11♢, 1♧, 4♢]を交換する場合、1,4,5と入力)")
                    try:
                        change_card = (input("現在の手札：{}".format(hand)))
                    except:
                        print("正しい入力ではありません。")
                    else:
                        change_card = change_card.split(",")
                        e = 1
                        y = False
                        for d in range(len(change_card)):
                            if 1 <= int(change_card[d]) <= 5:
                                hand.pop(int(change_card[d])-e)
                                e += 1
                            else:
                                print("正しい入力ではありません。")
                                print()
                                y = True
                                break
                        # if not y:
                        if y:
                            continue
                        record = hand_distribution(deck,hand,len(change_card))
                        hand = record[0]
                        hand = hand_organize(hand)
                        deck = record[1]
                        print()
                        print("交換した結果はこちらです。")
                        print(hand)
                        print()
                        count += 1
            elif x == 2:
                change = count
            
            else:
                print("正しい入力ではありません。")

print("では、この手札で確定します。")
x = 0
while (x != 1):
    try:
        x = int(input("祈りの時間が終わったら、1を押してください。"))
    except:
       print("正しい入力ではありません")
    else:
        if x == 1:
            print()
            print("あなたの役は、{}です。".format(confirm(hand)))
            cpu_hand = cpu_hand(level)
            print("cpuの役は、{}です。".format(cpu_hand))
            print(f"cpuの役は、{cpu_hand}です。")
            print()
            
            #勝敗判定
            if ("の" in confirm(hand)):
                player = confirm(hand).split("の")
                player_hand = player[1]
                player_number = int(player[0])
            else:
                player_hand = confirm(hand)
                player_number = 0
            if ("の" in cpu_hand):
                cpu = cpu_hand.split("の")
                cpu_hand = cpu[1]
                cpu_number = int(cpu[0])
            else:
                cpu_number = 0

            
            if defo_hand_list.index(player_hand) > defo_hand_list.index(cpu_hand):
                print("You Win! あなたの勝ちです!")
                print()
            elif defo_hand_list.index(player_hand) < defo_hand_list.index(cpu_hand):
                print("You Lose! あなたの負けです!")
                print()
            elif defo_hand_list.index(player_hand) == defo_hand_list.index(cpu_hand):
                if player_number > cpu_number:
                    print("You Win! 接戦でしたがあなたの勝ちです!")
                    print()
                elif player_number < cpu_number:
                    print("You Lose! 惜しいですがあなたの負けです!")
                    print()
                elif player_number == cpu_number:
                    print("なんと引き分けです!")
                    
        else:
            print("正しい入力ではありません。")