from pynput.mouse import Listener

def on_move(x,y):
    print("Mouse moved to:",int(x),int(y))


def on_click(x,y):
    print("Mouse is clicked: ",)
def on_moves(x,y):
    x=50
    y=60
    print("Mouse id moved")
with Listener(on_move=on_move, on_click=on_click,on_moves=on_moves) as listener:
    listener.join()
