import pyautogui
from time import sleep, time
from sys import argv

### Get mousepositions ###
#for i in range (4):
#    sleep(2)
#    print(pyautogui.position())

### To stop macro, press ctrl+c in the terminal ###

print("Press ctrl+c in terminal to stop")
loop_iterations = 0
start = time()
runtime = None
monitor = None

win1_mousepos = None
win2_mousepos = None
win3_mousepos = None
win4_mousepos = None

# Get argv input as monitor selection
try:
    monitor = int(argv[1])
except:
    monitor = 1

# Mouseclick coordinates
# First monitor
if monitor == 1:
    win1_mousepos = (863, 260)
    win2_mousepos = (1083, 264)
    win3_mousepos = (1075, 755)
    win4_mousepos = (822, 759)

# Second monitor
elif monitor == 2:
    win1_mousepos = (2717, 312)
    win2_mousepos = (3003, 313)
    win3_mousepos = (2962, 772)
    win4_mousepos = (2753, 785)

def main():
    global loop_iterations
    global start
    sleep(55)
    print("Runs in 5 seconds...")
    sleep(5)

    for _ in range(2):
        pyautogui.click(win1_mousepos)
        sleep(0.5)

    for _ in range(2):
        pyautogui.click(win2_mousepos)
        sleep(0.5)

    for _ in range(2):
        pyautogui.click(win3_mousepos)
        sleep(0.5)

    for _ in range(2):
        pyautogui.click(win4_mousepos)
        sleep(0.5)
        
    loop_iterations += 1
    end = time()

    runtime = float(end - start)
    print("loop iteration:", loop_iterations)
    print(f"Runtime: {runtime:.2f}s")

if __name__ == "__main__":
    try:
        while True:
            main()

    except KeyboardInterrupt:
        print("Macro stopped")
