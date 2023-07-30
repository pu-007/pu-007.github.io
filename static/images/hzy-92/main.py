import zhconv
from pathlib import Path
from rich import print
import numpy as np

from easyocr import Reader

ocr = Reader(["ch_tra"])

errno = 1
for fp in Path().glob("*.png"):
    cnt = ocr.readtext(str(fp))
    cnt = ''.join(map(lambda A: A[1], cnt)) or f"ERROR-{errno}"
    cnt = zhconv.convert(cnt, "zh-hans")
    cnt = cnt + ".png"
    print(fp, "-->", cnt)
    Path(fp).rename(cnt)
    errno += 1
