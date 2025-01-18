import tkinter as tk
from central import  start_central
import threading
#read 
import asyncio
from bleak import BleakClient, discover
from bleak import BleakScanner
import time
# 接続画面だけのテストではimport keyboardをコメントアウト
# import keyboard
is_running = True
devices_list = []  # スキャンしたデバイスを保持


# mac_address = "76:95:E3:BB:43:7B"
CHARACTERISTIC_UUID = "C2CF9284-8903-4EA0-A873-FE3AB1A56FE8"
UUID = "aaaaaaaa-bbbb-bbbb-bbbb-bbbbbbbbbbbb"

def notify_izunya(sender: int, data: bytearray):
    # keyboard.notification_handler(sender, data)
    # 接続画面だけのテストでは上をコメントアウトし、print
    print("ノティファイド")


async def maincentral(device):
    global is_running
    #Scan device
    #print("main")
    #device = await scan('TEST BLE')
    #print('found', device.name, device.address)

    async with BleakClient(device, timeout=None) as client:
        # x = await client.write_gatt_char(UUID,b"\0x01")
        label.config(text="繋がったよ")
        #print("Connected: {0}".format(x))
       # await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        await client.start_notify(CHARACTERISTIC_UUID,  notify_izunya)
        #await asyncio.sleep(30.0)
        for _ in range(20000):
            await asyncio.sleep(1)  # 中断を可能にするための短いスリープ
            if not is_running:
                print("is_runningがFalseに変わったため、停止...")
                break  # is_runningがFalseの場合、ループから抜け出す

        await client.stop_notify(CHARACTERISTIC_UUID)
        


async def scan(prefix='TEST BLE'):
    global is_running
    while is_running:
        try:
            print('scan...')
            global devices_list
            devices_list.clear()
            scanner_label.config(text="スキャン中...")
            devices = await BleakScanner.discover()
            for device in devices:
                devices_list.append(device)
                device_listbox.insert(tk.END, f"{device.name or 'Unknown'} - {device.address}")
                print(f"address: {device.address}, name: {device.name}, uuid: {device.metadata['uuids']}")
                if device.name == 'TEST BLE': #or d.metadata['uuids'] == ['aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee']:
                    #return d
                    label.config(text="接続完了")
                    button.config(state=tk.NORMAL)
                    await maincentral(device)
                    continue
            continue
        except StopIteration:
            print('continue..')
            continue

def connect_selected_device():
    selected_index = device_listbox.curselection()
    if selected_index:
        device = devices_list[selected_index[0]]
        threading.Thread(target=lambda: asyncio.run(connect_to_device(device.address))).start()
        label.config(text=f"{device.name or 'Unknown'} に接続を試みています...")
    else:
        label.config(text="デバイスを選択してください")

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

# リストボックス
device_listbox = tk.Listbox(root, width=60, height=15)
device_listbox.pack(pady=10)

# スキャン状態ラベル
scanner_label = tk.Label(root, text="デバイスをスキャンしてください")
scanner_label.pack(pady=5)

# ラベルを作成
label = tk.Label(root, text="接続を開始するにはボタンをクリックしてください")
label.pack(pady=10) #paddingを設定

# ウィンドウが閉じられるイベントに対する処理を設定
root.protocol("WM_DELETE_WINDOW", on_close)
# イベントループを開始
root.mainloop()
