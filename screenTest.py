import tkinter as tk
from central import  start_central
import threading
#read 
import asyncio
from bleak import BleakClient, discover
from bleak import BleakScanner
import time


# mac_address = "76:95:E3:BB:43:7B"
CHARACTERISTIC_UUID = "aaaaaaaa-dddd-bbbb-bbbb-bbbbbbbbbbbb"
UUID = "aaaaaaaa-bbbb-bbbb-bbbb-bbbbbbbbbbbb"



async def maincentral():
    # Scan device
    print("main")
    device = await scan('TEST BLE')
    #print('found', device.name, device.address)

    async with BleakClient(device, timeout=None) as client:
        x = await client.write_gatt_char(UUID,b"\0x01")
        label.config(text="繋がったよ")
        print("Connected: {0}".format(x))
       # await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        await client.start_notify(CHARACTERISTIC_UUID,  notify_izunya)
        print("noti1111")
        await asyncio.sleep(30.0)
        print("not22222")
        await client.stop_notify(CHARACTERISTIC_UUID)
        
def notify_izunya():
    print("notifyyy")


async def scan(prefix='TEST BLE'):
    while True:
        try:
            print('scan...')
            devices = await BleakScanner.discover()
            for d in devices:
                print(f"address: {d.address}, name: {d.name}, uuid: {d.metadata['uuids']}")
                if d.name == 'TEST BLE' or d.metadata['uuids'] == ['aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee']:
                    return d
        except StopIteration:
            print('continue..')
            continue

def update_label_after_scan():
    device = asyncio.run(scan())
    print("見つかった！")
    label.config(text="ババババb")


   

def on_button_click():
    print("接続中")
    #asyncio.run(scan())
    thread1 = threading.Thread(target=update_label_after_scan)
    thread1.start() 
    #終わったら何か表示させる
   

# メインウィンドウを作成
root = tk.Tk()
root.title("iPad5重音キーボード")
root.geometry("500x300")

# ボタンを作成
button = tk.Button(root, text="非同期処理を開始", command=on_button_click)
button.pack(pady=10)

# ラベルを作成
label = tk.Label(root, text="ボタンをクリックしてください。")
label.pack(pady=10) #paddingを設定

# イベントループを開始
root.mainloop()