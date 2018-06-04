import ctypes
from ctypes import windll, Structure, c_ulong, byref
import struct, commctrl, win32gui, win32con, win32api
import random


class LVITEMW(ctypes.Structure):
        _fields_ = [
            ('mask', ctypes.c_uint32),
            ('iItem', ctypes.c_int32),
            ('iSubItem', ctypes.c_int32),
            ('state', ctypes.c_uint32),
            ('stateMask', ctypes.c_uint32),
            ('pszText', ctypes.c_uint64),
            ('cchTextMax', ctypes.c_int32),
            ('iImage', ctypes.c_int32),
            ('lParam', ctypes.c_uint64),
            ('iIndent',ctypes.c_int32),
            ('iGroupId', ctypes.c_int32),
            ('cColumns', ctypes.c_uint32),
            ('puColumns', ctypes.c_uint64),
            ('piColFmt', ctypes.c_int64),
            ('iGroup', ctypes.c_int32),
        ]

class Point(Structure):
        _fields_ = [("x", c_ulong),("y", c_ulong)]


def queryMousePosition():
        pt = Point()
        windll.user32.GetCursorPos(byref(pt))
        return (int(pt.x),int(pt.y))



def glav():        
    print icons
    pos = queryMousePosition()
    for i in range(len(icons)):
        if(pos[0]-25<=icons[i][0]<=pos[0]+25 and pos[1]-43<=icons[i][1]<=pos[1]+43):
            pB = random.randrange(1099185664,2299185664)
            print pB
            win32api.SendMessage(slvhwnd, commctrl.LVM_SETITEMPOSITION, i, pB)
    for i in xrange(num_items):
        # Get icon position
        win32api.SendMessage(slvhwnd, commctrl.LVM_GETITEMPOSITION, i, pBufferpnt)
        p = Point()
        ctypes.windll.kernel32.ReadProcessMemory(hProcHnd, pBufferpnt, ctypes.addressof(p), ctypes.sizeof(p), p_copied)
        icons[i] = int(p.x),int(p.y)

old_pos = 0
dthwnd = win32gui.FindWindow(None, 'Program Manager')
ukhwnd = win32gui.GetWindow(dthwnd, win32con.GW_CHILD)
slvhwnd = win32gui.GetWindow(ukhwnd, win32con.GW_CHILD)
pid = ctypes.create_string_buffer(4)
p_pid = ctypes.addressof(pid)
ctypes.windll.user32.GetWindowThreadProcessId(slvhwnd, p_pid)
hProcHnd = ctypes.windll.kernel32.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, struct.unpack("i",pid)[0])
pBuffertxt = ctypes.windll.kernel32.VirtualAllocEx(hProcHnd, 0, 4096, win32con.MEM_RESERVE|win32con.MEM_COMMIT, win32con.PAGE_READWRITE)
copied = ctypes.create_string_buffer(4)
p_copied = ctypes.addressof(copied)
lvitem = LVITEMW()
lvitem.mask = ctypes.c_uint32(commctrl.LVIF_TEXT)
lvitem.pszText = ctypes.c_uint64(pBuffertxt)
lvitem.cchTextMax = ctypes.c_int32(4096)
lvitem.iSubItem = ctypes.c_int32(0)
pLVI = ctypes.windll.kernel32.VirtualAllocEx(hProcHnd, 0, 4096, win32con.MEM_RESERVE| win32con.MEM_COMMIT,  win32con.PAGE_READWRITE)
win32api.SetLastError(0)
ctypes.windll.kernel32.WriteProcessMemory(hProcHnd, pLVI, ctypes.addressof(lvitem), ctypes.sizeof(lvitem), p_copied)
num_items = win32gui.SendMessage(slvhwnd, commctrl.LVM_GETITEMCOUNT)
hProcHnd = ctypes.windll.kernel32.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, struct.unpack("i",pid)[0])
    
p = Point()
pBufferpnt = ctypes.windll.kernel32.VirtualAllocEx(hProcHnd, 0, ctypes.sizeof(p), win32con.MEM_RESERVE|win32con.MEM_COMMIT, win32con.PAGE_READWRITE)
icons = [(0,0)]*num_items
for i in xrange(num_items):
    # Get icon position
    win32api.SendMessage(slvhwnd, commctrl.LVM_GETITEMPOSITION, i, pBufferpnt)
    p = Point()
    ctypes.windll.kernel32.ReadProcessMemory(hProcHnd, pBufferpnt, ctypes.addressof(p), ctypes.sizeof(p), p_copied)
    icons[i] = int(p.x),int(p.y)

    
while(True):
    pos = queryMousePosition()
    
    if(old_pos!=pos):
        print pos
        glav()
        old_pos=pos
