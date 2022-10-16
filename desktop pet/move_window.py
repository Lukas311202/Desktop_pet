import pygetwindow as gw

def main():
    #print(gw.getAllTitles())
    vs_window = gw.getWindowsWithTitle("Visual Studio Code")[0]
    #vs_window.moveTo(20,20)
    print(vs_window._getWindowRect())

def move_window(title, pos):
    window = gw.getWindowsWithTitle(title)[0]
    window.moveTo(pos[0],pos[1])

def get_window_position(title) -> gw.Rect:
    window = gw.getWindowsWithTitle(title)[0]
    return window._getWindowRect()

def window_exists(title):
    return len(gw.getWindowsWithTitle(title)) > 0

if __name__ == "__main__":
    main()
