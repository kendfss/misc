from pathlib import Path
from sl4ng import show

v = Path('f:/ytdls')


find = lambda word: show(v.rglob(f'*{word}*'))
