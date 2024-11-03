#read
import asyncio
#import ctypes.windll.user32 as win32api
import win32con
import win32api
import time


VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           '゛':0xC0,
           ';':0xBA,
           '~':0xC0,
           '+':0xBB,
           '[':0xDB,
           '_':0xE2,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0,
           'convert':0x1c,
           }


Two_char={
    'け':[0x10,0xba],
    'を':[0x10,0x30],
    '、':[0x10,0xbc],
    '。':[0x10,0xbe],


    }

Romaji={
     'num0':0x30,
     'num1':0x31,
     'num2':0x32,
     'num3':0x33,
     'num4':0x34,
     'num5':0x35,
     'num6':0x36,
     'num7':0x37,
     'num8':0x38,
     'num9':0x39,

    }


Changetoinput={
       "あ":"3",
    "い":"e",
    "う":"4",
    "え":"5",
    "お":"6",
    "か":"t",
    "き":"g",
    "く":"h",
    #け　shift 0x10 + け 0xBA
    "こ":"b",
    "さ":"x",
    "し":"d",
    "す":"r",
    "せ":"p",
    "そ":"c",
    "た":"q",
    "ち":"a",
    "つ":"z",
    "て":"w",
    "と":"s",
    "な":"u",
    "に":"i",
    "ぬ":"1",
    "ね":",",
    "の":"k",
    "は":"f",
    "ひ":"v",
    "ふ":"2",
    "へ":"'",
    "ほ":"-",
    "ま":"j",
    "み":"n",
    "む":"]",
    "め":"/",
    "も":"m",
    "ら":"o",
    "り":"l",
    "る":".",
    "れ":"+",
    "ろ":"_",
    #0xe2
    "や":"7",
    "ゆ":"8",
    "よ":"9",
    "わ":"0",
    #を
    "ん":"y",
    "0":"num0",
    "1":"num1",
    "2":"num2",
    "3":"num3",
    "4":"num4",
    "5":"num5",
    "6":"num6",
    "7":"num7",
    "8":"num8",
    "9":"num9",
    "↑":"up_arrow",
    "↓":"down_arrow",
    "←":"left_arrow",
    "→":"right_arrow",
    "削除":"backspace",
    "空白":"spacebar",
    "゛\n濁点":"`",
    "゜":"[",
    "変換":"convert",
    "決定":"enter",
    "。\n句点":"。",
    "、\n読点":"、",
    "小文字":"F8",


    }


# mac_address = "76:95:E3:BB:43:7B"
# CHARACTERISTIC_UUID = "aaaaaaaa-dddd-bbbb-bbbb-bbbbbbbbbbbb"
# UUID = "aaaaaaaa-bbbb-bbbb-bbbb-bbbbbbbbbbbb"


def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0,0,0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

def press2(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    print("pressss2")
    win32api.keybd_event(0xa4, 0,0,0)
    win32api.keybd_event(0xf2, 0,0,0)
    win32api.keybd_event(0xa4, 0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0xf2, 0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(.05)
    win32api.keybd_event(0x30, 0,0,0)


    win32api.keybd_event(0x30, 0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(.05)
    win32api.keybd_event(0xa4, 0,0,0)
    win32api.keybd_event(0xf2, 0,0,0)
    win32api.keybd_event(0xa4, 0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0xf2, 0,win32con.KEYEVENTF_KEYUP,0)

  #  time.sleep(.05)

  #  win32api.keybd_event(0x15, 0,0,0)
   # win32api.keybd_event(0x15, 0,win32con.KEYEVENTF_KEYUP,0)
    #win32api.keybd_event(0x60, 0,win32con.KEYEVENTF_KEYUP,0)
   # win32api.keybd_event(0x30, 0,0,0)
    #win32api.keybd_event(0x30,0 ,win32con.KEYEVENTF_KEYUP,0)
   # win32api.keybd_event(0x4E, 0,win32con.KEYEVENTF_KEYUP,0)
    #win32api.keybd_event(0xf5, 0,0,0)
    #win32api.keybd_event(0xf5, 0,win32con.KEYEVENTF_KEYUP,0)



def press3(str):#に文字入力用
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    p1 = Two_char[str][0]
    p2 = Two_char[str][1]
    win32api.keybd_event(p1, 0,0,0)
    win32api.keybd_event(p2, 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(p1,0 ,win32con.KEYEVENTF_KEYUP ,0)
    win32api.keybd_event(p2,0 ,win32con.KEYEVENTF_KEYUP ,0)


def press4(str):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    p1 = Romaji[str]
    print("pressss2")
    win32api.keybd_event(0xa4, 0,0,0)
    win32api.keybd_event(0xf2, 0,0,0)
    win32api.keybd_event(0xa4, 0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0xf2, 0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(.05)
    win32api.keybd_event(p1, 0,0,0)


    win32api.keybd_event(p1, 0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(.05)
    win32api.keybd_event(0xa4, 0,0,0)
    win32api.keybd_event(0xf2, 0,0,0)
    win32api.keybd_event(0xa4, 0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0xf2, 0,win32con.KEYEVENTF_KEYUP,0)

  #  time.sleep(.05)

  #  win32api.keybd_event(0x15, 0,0,0)
   # win32api.keybd_event(0x15, 0,win32con.KEYEVENTF_KEYUP,0)
    #win32api.keybd_event(0x60, 0,win32con.KEYEVENTF_KEYUP,0)
   # win32api.keybd_event(0x30, 0,0,0)
    #win32api.keybd_event(0x30,0 ,win32con.KEYEVENTF_KEYUP,0)
   # win32api.keybd_event(0x4E, 0,win32con.KEYEVENTF_KEYUP,0)
    #win32api.keybd_event(0xf5, 0,0,0)
    #win32api.keybd_event(0xf5, 0,win32con.KEYEVENTF_KEYUP,0)

async def scan(prefix='TEST BLE'):
    while True:
        print('scan...')
        try:
            return next(d for d in await discover() if d.name and d.name.startswith(prefix))
        except StopIteration:
            continue



def notification_handler(sender, data):
    print("BUTTON {0}: {1}".format(sender, data))
    str = data.decode()
    print(str)

    if str in Changetoinput.keys():
        st = str
        str = Changetoinput[st]

    if str in VK_CODE.keys():
       press(str)
    elif str in Two_char.keys():
        press3(str)
        print(str)
    elif str in Romaji.keys():
        print(str)
        press4(str)

    else:
       print("aaaaa" + data.decode())
       for i in str:
           press(i)
