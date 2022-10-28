import time
import sys
import random

if __name__ != '__main__':
    print("えっ待ってなんでほかのプログラムにモジュールとして食われるの?()")
    input()
    sys.exit()

print("おはよ〜！みんなのアイドルまっちゃんだよ！！！")

while True:
    userinput = input("ねこまっちゃん>")
    if "おはよう" in userinput:
        rand = random.randint(1,3)
        if rand == 1:
            print("おはよおおおおお！")
        elif rand == 2:
            print("おはよ～う")
        elif rand == 3:
            print("おはようございません(?)")

    if "おやすみ" in userinput:
        rand = random.randint(1,3)
        if rand == 1:
            print("おやすみ～")
        elif rand == 2:
            print("おやすみんみんぜみ")
        elif rand == 3:
            print("おやすみなさい！！！！！")

    if "浮気だ" in userinput:
        rand = random.randint(1,3)
        if rand == 1:
            print("浮気じゃない！！！！！！！！！！()")
        elif rand == 2:
            print("おい()")
        elif rand == 3:
            print("えっなんでなんで()")

    if "さよなら" in userinput:
        rand = random.randint(1,3)
        if rand == 1:
            print("さよなら～!")
        elif rand == 2:
            print("さよならにゃー")
        elif rand == 3:
            print("またね～！！！！()")
        print("AIっちゃんとの接続を切りました")
        sys.exit()

    if "にゃん" in userinput:
        print("にゃん")

    if "version" in userinput:
        print("AIっちゃん v1 by niwatori_chicken")

    else:
        print("この単語は登録されてないよ！！")
