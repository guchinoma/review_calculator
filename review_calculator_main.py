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

import review_calculator
import datetime
import google_write
 

if __name__ ==  "__main__":


#    l = raw_input().split()

    today = datetime.date.today()

    a = review_calculator.Day_Plus_1(today)
    b = review_calculator.Day_Plus_3(today)
    c = review_calculator.Day_Plus_5(today)
    d = review_calculator.Day_Plus_7(today)
    e = review_calculator.Day_Plus_14(today)
    f = review_calculator.Day_Plus_21(today)
    g = review_calculator.Day_Plus_28(today)
    h = review_calculator.Day_Plus_84(today)


#    google_write.insert_event(l[0], l[1], a)
#    google_write.insert_event(l[0], l[1], b)
#    google_write.insert_event(l[0], l[1], c)
#    google_write.insert_event(l[0], l[1], d)
#    google_write.insert_event(l[0], l[1], e)
#    google_write.insert_event(l[0], l[1], f)
#    google_write.insert_event(l[0], l[1], g)
#    google_write.insert_event(l[0], l[1], h)


