#!/usr/bin/env python3

condition_1 = '需要实名 :('
condition_2 = '不记名车站 :D'
condition_3 = '交通联合卡 :D'
condition_4 = '发放全新卡 :D'
condition_5 = '发放二手卡 :('

def print_stations():
    print("地铁站列表:\n")
    print("[1] 中关村站\n")
    print("[2] 金安桥站\n")
    print("[3] 海淀黄庄站\n")
    print("[4] 国家图书馆站\n")
    print("[5] 奥林匹克公园站\n")
    print("[6] 森林公园南门站\n")
    print("[7] 巴沟站\n")
    print("[8] 北京西站\n\n")

def print_conditions(selected_station):
    if selected_station in ['1', '2', '3', '4']:
        print(condition_1)
    elif selected_station in ['5', '8']:
        print(condition_2)
        print(condition_3)
        print(condition_4)
    elif selected_station in ['6', '7']:
        print(condition_2)
        print(condition_3)
        print(condition_5)
    else:
        print("输入不正确 :(")

print_stations()
station = input("请输入车站序号: ")
print("")
print_conditions(station)
input("\n")
