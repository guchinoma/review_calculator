#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import gdata.calendar.client

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


def insert_event(theme, contents, date):

    print "Insert Event into Google Calendar"

    login_password = 'YOUR_PASSWORD'
    login_email = 'YOUR_GMAIL@gmail.com'

    calendar_service = gdata.calendar.client.CalendarClient()
    calendar_service.ssl = True
    calendar_service.ClientLogin(login_email, login_password, "test python script")

    event = gdata.calendar.data.CalendarEventEntry()
    event.title = atom.data.Title(text="theme")
    event.content = atom.data.Content(text="contents")
    start_time = 'date.year-date.month-date.day'
    event.when.append(gdata.data.When(start=start_time, end=start_time))

    calendar_service.InsertEvent(event)


