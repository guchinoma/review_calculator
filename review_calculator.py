#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
コーディング規則
関数を書く上で、単語ごとには必ず大文字にする(前置詞も、冠詞も含む）
しかし、変数に関しては、全て小文字にする。
単語ごとにはアンダーバーを入れる
（例）
URL_Download_To_File
Return_Arguments_In_the_Fuction
int retrutn_of_arguments = 32;
'''

import datetime


# 一日後
def Day_Plus_1(a):
    
    day_plus_1 = a  + datetime.timedelta(days=1)
    print day_plus_1
    return day_plus_1

# 三日後
def Day_Plus_3(a):

    day_plus_3 = a  + datetime.timedelta(days=3)
    print day_plus_3
    return day_plus_3

# 五日後
def Day_Plus_5(a):

    day_plus_5 = a  + datetime.timedelta(days=5)
    print day_plus_5
    return day_plus_5

# 一週間後
def Day_Plus_7(a):

    day_plus_7 = a  + datetime.timedelta(days=7)
    print day_plus_7
    return day_plus_7

# 二週間後
def Day_Plus_14(a):

    day_plus_14 =  a  + datetime.timedelta(days=14)
    print day_plus_14
    return day_plus_14

# 一週間後
def Day_Plus_21(a):

    day_plus_21 =  a  + datetime.timedelta(days=21)
    print day_plus_21
    return day_plus_21

# 一ヶ月後
def Day_Plus_28(a):

    day_plus_28 = a  + datetime.timedelta(days=28)
    print day_plus_28
    return day_plus_28

# 三ヶ月後
def Day_Plus_84(a):

    day_plus_84 = a  + datetime.timedelta(days=84)
    print day_plus_84
    return day_plus_84


