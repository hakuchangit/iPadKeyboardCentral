#read 
import asyncio
from bleak import BleakClient, discover
from bleak import BleakScanner
import time

# mac_address = "76:95:E3:BB:43:7B"
CHARACTERISTIC_UUID = "C2CF9284-8903-4EA0-A873-FE3AB1A56FE8"#NotifyCharacteristic
#UUID = "aaaaaaaa-bbbb-bbbb-bbbb-bbbbbbbbbbbb" #WriteWithoutResponseCharacteristic

async def scan(prefix='TEST BLE'):
    while True:
        try:
            print('scan...')
            devices = await BleakScanner.discover()
            for d in devices:
                print(f"address: {d.address}, name: {d.name}, uuid: {d.metadata['uuids']}")
                if d.name == 'TEST BLE' or d.metadata['uuids'] == ['ACDD196E-C057-4133-AFD8-18E10378BFEB']:#BLEServiceUUID
                    return d
        except StopIteration:
            print('continue..')
            continue

def notify_izunya():
    print("notifyyy")
    


async def main():
    # Scan device
    print("main")
    device = await scan('TEST BLE')
    #print('found', device.name, device.address)

    async with BleakClient(device, timeout=None) as client:
        x = await client.write_gatt_char(UUID,b"\0x01")
        print("Connected: {0}".format(x))
       # await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        await client.start_notify(CHARACTERISTIC_UUID,  notify_izunya)
        print("noti1111")
        await asyncio.sleep(30.0)
        print("not22222")
        await client.stop_notify(CHARACTERISTIC_UUID)
        
        #while True:
         #   await asyncio.sleep(1)

#if __name__ ==  "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())
#    loop.close()


def start_central():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
 