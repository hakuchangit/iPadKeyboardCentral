import tkinter as tk
from central import  start_central
import threading
#read 
import asyncio
from bleak import BleakClient, discover
from bleak import BleakScanner
import time

is_running = True

# mac_address = "76:95:E3:BB:43:7B"
CHARACTERISTIC_UUID = "aaaaaaaa-dddd-bbbb-bbbb-bbbbbbbbbbbb"
UUID = "aaaaaaaa-bbbb-bbbb-bbbb-bbbbbbbbbbbb"

def notify_izunya(sender: int, data: bytearray):
    print("notifyyy")


async def maincentral(device):
    global is_running
    #Scan device
    #print("main")
    #device = await scan('TEST BLE')
    #print('found', device.name, device.address)

    async with BleakClient(device, timeout=None) as client:
        x = await client.write_gatt_char(UUID,b"\0x01")
        label.config(text="繋がったよ")
        print("Connected: {0}".format(x))
       # await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        await client.start_notify(CHARACTERISTIC_UUID,  notify_izunya)
        print("noti1111")
        #await asyncio.sleep(30.0)
        for _ in range(30):
            await asyncio.sleep(1)  # 中断を可能にするための短いスリープ
            if not is_running:
                print("is_runningがFalseに変わったため、停止...")
                break  # is_runningがFalseの場合、ループから抜け出す

        print("not22222")
        await client.stop_notify(CHARACTERISTIC_UUID)
        


async def scan(prefix='TEST BLE'):
    global is_running
    while is_running:
        try:
            print('scan...')
            devices = await BleakScanner.discover()
            for d in devices:
                print(f"address: {d.address}, name: {d.name}, uuid: {d.metadata['uuids']}")
                if d.name == 'TEST BLE' or d.metadata['uuids'] == ['aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee']:
                    #return d
                    label.config(text="接続完了")
                    button.config(state=tk.NORMAL)
                    await maincentral(d)
                    continue
            continue
        except StopIteration:
            print('continue..')
            continue



def update_label_after_scan():
    label.config(text="接続中...")
    button.config(state=tk.DISABLED)
    device = asyncio.run(scan())
    
    #asyncio.run(maincentral(device))
   
   

def on_button_click():
    global is_running
    is_running = True
    thread1 = threading.Thread(target=update_label_after_scan)
    thread1.start()

def on_button_click_stop():
    global is_running
    is_running = False

def on_close():
    global is_running
    is_running = False  # スレッドを停止させる
    root.destroy()  # ウィンドウを閉じる

# メインウィンドウを作成
root = tk.Tk()
root.title("iPad5重音キーボード")
root.geometry("500x300")

# ボタンを作成
button = tk.Button(root, text="デバイスに接続する", command=on_button_click)
button.pack(pady=10)

button_stop = tk.Button(root, text="stop", command=on_button_click_stop)
button_stop.pack(pady=10)

# ラベルを作成
label = tk.Label(root, text="接続を開始するにはボタンをクリックしてください")
label.pack(pady=10) #paddingを設定

# ウィンドウが閉じられるイベントに対する処理を設定
root.protocol("WM_DELETE_WINDOW", on_close)
# イベントループを開始
root.mainloop()
