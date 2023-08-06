# coding: utf-8
import requests, os, sys, tarfile, yaml, math, time
import numpy as np
import pandas as pd
import smtplib
import configparser as cfg
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def d_stamp():
    '''
    d_stamp()

    Call function to return date string, format show like: 2023-07-20 14:30:26
    呼叫後回傳日期字串, 字串格式: 2023-07-20 14:30:26
    '''
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return stamp

def tar_file(s_path, t_path):
    '''
    tar_file(s_path, t_path)

    Compress file by tar, the file name will add compress date string.
    壓縮檔案並於檔名加上日期字串

    Argument:
    參數說明

    s_path = Source file full path, string type
             原始檔案完整路徑, 字串類型

    t_path = Target folder path, string type
             壓縮檔放置目錄路徑, 字串類型

    '''
    tar_date = str(datetime.today().strftime('%Y%m%d'))
    with tarfile.open(f'{t_path}{os.path.basename(s_path)}_{tar_date}.tar.gz', 'w:gz') as tf:
        tf.add(s_path, arcname=os.path.basename(s_path))

    return None

def trc_file(file_path):
    '''
    trc_file(file_path)

    Truncate file content.
    清空檔案內容

    Argument:
    參數說明

    file_path = Full path of file you want to truncat content.
                要清除內容的檔案放置的完整路徑
    '''
    with open(file_path, 'r+') as tf:
        tf.truncate()

    return None

def s_mail(smail):
    '''
    s_mail(smail)

    Using custmize content to send email.
    自訂信件內容來傳送 email

    Argument:
    參數說明

    smail = Sending mail data, dictionary type.
            傳送郵件內容, 字典類型

    smail = {
    'smtp' : 'SMTP server', # SMTP server hostname or IP ( SMTP 伺服器主機名稱或IP位址)
    'from' : 'Sender', # Mail sender address (寄件者郵件位址)
    'to' : 'Reciver', # Reciver list string, use ", " to divide each address,
                        e.g.: user1@twsit.com, user2@twsit.com, user3@twsit.com
                        收件者清單字串, 以"逗號+空白"區隔每個郵件位址, 格式如上
    'subj' : 'Subject', # Mail subject, string typer.(郵件主旨)
    'content' : 'Content', # Mail content,string type, HTML format'. (郵件內容, 字串類型, HTML 格式)
    'file_path' : 'Path', # Mail attached file full path. (郵件附件完整路徑)
    'file_name' : 'Name' # Mail attached file name show in mail. (郵件附件在信中顯示名稱)

    }
    '''
    s_from = smail['from']
    s_to = smail['to']
    smtp_obj = smtplib.SMTP(smail['smtp'], 25)
    mail_msg = MIMEMultipart()
    mail_msg['From'] = s_from
    mail_msg['to'] = s_to
    mail_msg['Subject'] = smail['subj']
    mail_msg.attach(MIMEText(smail['content'], 'html'))
    if 'file_path' in smail.keys():
        with open (smail['file_path'], 'rb') as af:
            attach = af
            attachment = MIMEApplication(attach.read())

        attachment.add_header('Content-Disposition', 'attachment', filename=smail['file_name'])
        mail_msg.attach(attachment)

    else:
        pass

    smtp_obj.sendmail(s_from, s_to.split(','), mail_msg.as_string())
    smtp_obj.quit()
    return None

def f_modifydays(path):
    '''
    f_modifydays(path)

    Count days of file last modified untile now.
    計算檔案最後修改時間至今有幾日

    Argument:
    參數說明

    path = Full path of file wants to count days
    要計算日數的檔案所在完整絕對路徑
    '''
    m_time = datetime.fromtimestamp(os.path.getmtime(path))
    now = datetime.now()
    m_days = (now - m_time).days
    return m_days

def l_tolist(path):
    '''
    l_tolist(path)

    Read file then convert to list by each line.
    讀取檔案內容並轉換為串列(list), 每一行做為一個串列元素

    Argument:
    參數說明

    path = Full path of file wants convert to list
    要轉換為串列的檔案所在完整絕對路徑
    '''
    with open(path, 'r') as rf:
        f_list = rf.read().split('\n')

    return f_list

def csv_todict(path):
    '''
    csv_todict(path)

    Read CSV file then convert to dictionary.
    讀取 CSV 格式檔案並將內容轉換為字典類型變數

    Argument:
    參數說明

    path = Full path of file wants to convert
    要轉換為字典的檔案所在完整絕對路徑
    '''
    df = pd.read_csv(path, header=None)
    c_dict = df.set_index(0).to_dict()[1]
    return c_dict

def dt_check(chk_str):
    '''
    dt_check(chk_str)

    Check date time now and return value assigned by yourself.
    You can assign to get which hour, day, weekday, month for now.
    透過指定欄位可取得目前日期時間的相關數值.
    你可以指定要取得目前是幾點? 幾日? 禮拜幾? 幾月?

    Argument:
    參數說明

    chk_str = 要確認的日期欄位, 字串類型
              可接受欄位: hour, day, week, month
              每次呼叫只能指定一個欄位

    函式內可以查詢的日期時間欄位參數如下所列: (供日後修改函式存參)
        %y 兩位數的年份表示（00-99）
        %Y 四位數的年份表示（0000-9999）
        %m 月份（01-12）
        %d 月內中的一天（0-31）
        %H 24小時制小時數（0-23）
        %I 12小時制小時數（01-12）
        %M 分鐘數（00-59）
        %S 秒（00-59）
        %a 本地簡化星期名稱 ( Mon, Tue, Wed... )
        %A 本地完整星期名稱 ( Monday, Tuesday, Wednesday... )
        %b 本地簡化的月份名稱 ( Jan, Feb, Mar... )
        %B 本地完整的月份名稱 ( January, February, March... )
        %c 本地相應的日期表示和時間表示
        %j 年內的一天（001-366）
        %p 本地A.M.或P.M.的等價符
        %U 一年中的星期數（00-53）星期天為星期的開始
        %w 星期（0-6），星期天為星期的開始
        %W 一年中的星期數（00-53）星期一為星期的開始
        %x 本地相應的日期表示
        %X 本地相應的時間表示
        %Z 當前時區的名稱
    '''
    dt_type = ''
    if chk_str == 'hour':
        dt_type = '%H'
    elif chk_str == 'day':
        dt_type = '%d'
    elif chk_str == 'week':
        dt_type = '%a'
    elif chk_str == 'month':
        dt_type = '%m'

    dt = datetime.now().strftime(dt_type)

    if chk_str != 'week':
        dt = int(dt)
    return dt

def f_rounding(f_num , d_num):
    '''
    f_rounding(f_num, d_num)

    Give a float number to function then assign decimal place number for the number you want to get.
    呼叫函式並帶入浮點數，取得指定位數四捨五入後的結果

    Argument:
    參數說明

    f_num = Float number you want to rounding
            要四捨五入的浮點數

    d_num = Decimal place number
            指定的進位數
    '''
    f_num = np.round(f_num, d_num)
    f_num = float(f_num)
    return f_num

def key_found(dic, value):
    '''
    key_found(dic, value)

    Give a dictionary to function then assign a value to found it's key in dictionary.
    呼叫函式在帶入的字典類型變數中尋找 key 值

    Argument:
    參數說明

    dic = Dictionary you want to get key.
          要尋找 key 的字典類型變數

    value = The value in dictionary you want to found key.
            在字典類型變數中的值, 透過值找出對應的 key

    '''
    key = [k for k, v in dic.items() if value in v]

    if len(key) != 1:
        key = ['error']
    elif key == []:
        key = ['null']
    return key[0]

    def read_ini(self, path):
        '''
        read_ini(path)
        
        To get setting in .ini file you defined.
        讀取你定義的 ini 檔案並取得檔案內的設定值
        
        Argument:
        參數說明
        
        path = .ini file full path
               自定義的 .ini 設定檔完整絕對路徑
        '''
        parser = cfg.ConfigParser()
        parser.read(path)
        return parser
    
def add_log(path, log):
    '''
    add_log(path, log)

    Add log to log file you assign.
    - File not exist: Creat new file then write new log.
    - File exist: Write new log after the last line in log file.
    將 log 紀錄新增到指定的 log 檔案中
    - 檔案不存在 : 建立新檔案並寫入 log
    - 檔案存在 : 由最後一行起開始追加寫入 log

    Argument:
    參數說明

    path = Full path of log file your want to create / add.
           要新增/建立的 log 檔案完整絕對路徑

    log = log content you want add to file. String type.
          要新增到檔案內的 log 紀錄內容, 字串類型
    '''
    if os.path.isfile(path):
        mode = 'a'
    else:
        mode = 'w'

    with open(path, mode) as al:
        al.write(log)
    return None

def read_yaml(path):
    '''
    read_yaml(path)

    Get setting from YAML you defined.
    由自定義的 YAML 檔案取得設定, 設定為字典類型

    Argument:
    參數說明

    path = Full paht of YAML file
           自定義的 YAML 檔案完整絕對路徑
    '''
    try:
        with open(path, 'r') as ry:
            setting = yaml.load(ry, Loader=yaml.SafeLoader)

    except Exception as err:
        return err

    else:
        return setting
    return None

def p_bar(bar_len , prog, targ):
    '''
    p_bar(bar_len, prog, targ)

    To show progress bar on screen.
    在螢幕上顯示處理進度條

    Argument:
    參數說明

    bar_len = Length of bar to show.(Unit: Char)
              進度條總長度(單位: 字元)

    prog = Progress of now processed.
           目前處理進度

    targ = Target of completed.
           完成目標數字
    '''
    b_len = bar_len #進度條字元長度
    f_char = math.ceil( b_len * (prog / float(targ)) ) # 目前進度填入字元長度
    percent = math.ceil(100.0 * ( prog / float(targ) )) # 目前進度百分比
    b_show = '=' * f_char + '-' * (b_len - f_char)
    size = f'{math.ceil(prog / 1024):,} KB' if prog > 1024 else f'{prog} byte' # 以處理資料大小計算
    sys.stdout.write(f'[{b_show}] {percent} % {size}\r')
    sys.stdout.flush()
    return None

