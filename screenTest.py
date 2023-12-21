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



async def maincentral(device):
    # Scan device
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
    label.config(text="接続中...")
    button.config(state=tk.DISABLED)
    device = asyncio.run(scan())
    label.config(text="接続完了")
    button.config(state=tk.NORMAL)
    asyncio.run(maincentral(device))
   
   

def on_button_click():
    thread1 = threading.Thread(target=update_label_after_scan)
    thread1.start()
    

   

# メインウィンドウを作成
root = tk.Tk()
root.title("iPad5重音キーボード")
root.geometry("500x300")

# ボタンを作成
button = tk.Button(root, text="デバイスに接続する", command=on_button_click)
button.pack(pady=10)

# ラベルを作成
label = tk.Label(root, text="接続を開始するにはボタンをクリックしてください")
label.pack(pady=10) #paddingを設定

# イベントループを開始
root.mainloop()