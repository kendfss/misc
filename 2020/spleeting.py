from pyperclip import copy

src = r""
dst = r""
cmd = f"E:\Languages\Python37-64\python.exe -m spleeter separate -i '{src}' -p spleeter:2stems -o '{dst}'"

print(cmd)
copy(cmd)