from pathlib import Path
from time import ctime
import shutil

path  = Path("./ecommerce/Hello.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(path.stat()) # gives all the details likr size
# print(path.stat().st_ctime)
print(path.read_text())
print(path.read_bytes())
path.write_text("...")
path.write_bytes("...")

# copying files one directary to another

source=Path("./ecommerce/Hello.py")
target = Path()/"init.py"
shutil.copy(source,target)
