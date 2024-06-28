import pyautogui
from time import sleep, time
import gooeypie as gp
import threading


screen_res = pyautogui.size()
screen_x = screen_res[0]
screen_y = screen_res[1]

mouse_pos = []
starttime = None
running = False

def startmacro(event):
    global running
    global mouse_pos
    global time_interval
    global starttime

    time_interval = int(interval_num.value)
    monitor = int(mon_sel_dd.selected_index)
    starttime = time()

    if monitor == 0:
        mouse_pos.append((screen_x/2.2, screen_y/4.2))
        mouse_pos.append((screen_x/1.8, screen_y/4.1))
        mouse_pos.append((screen_x/1.8, screen_y/1.4))
        mouse_pos.append((screen_x/2.3, screen_y/1.4))

    elif monitor == 1:
        mouse_pos.append((2717, 312))
        mouse_pos.append((3003, 313))
        mouse_pos.append((2962, 772))
        mouse_pos.append((2753, 785))

    running = True
    loop_thread = threading.Thread(target=macro)
    loop_thread.start()

def endmacro(event):
    global running
    running = False

def macro():
    win_layout = int(win_layout_dd.selected_index)
    while running:
        endtime = time()
        runtime = endtime - starttime
        runtime_lbl.text = f"Runtime: {runtime:.2f}s"
        if win_layout == 0:
            for _ in range(2):
                pyautogui.click(mouse_pos[1])
                sleep(0.3)
            sleep(time_interval)

        elif win_layout == 1:
            for _ in range(2):
                pyautogui.click(mouse_pos[0])
                sleep(0.3)
            for _ in range(2):
                pyautogui.click(mouse_pos[1])
                sleep(0.3)
            sleep(time_interval)

        elif win_layout == 2:
            for _ in range(2):
                pyautogui.click(mouse_pos[0])
                sleep(0.3)
            for _ in  range(2):
                pyautogui.click(mouse_pos[1])
                sleep(0.3)
            for _ in  range(2):
                pyautogui.click(mouse_pos[2])
                sleep(0.3)
            sleep(time_interval)

        elif win_layout == 3:
            for _ in range(2):
                pyautogui.click(mouse_pos[0])
                sleep(0.3)
            for _ in  range(2):
                pyautogui.click(mouse_pos[1])
                sleep(0.3)
            for _ in  range(2):
                pyautogui.click(mouse_pos[2])
                sleep(0.3)
            for _ in  range(2):
                pyautogui.click(mouse_pos[3])
                sleep(0.3)
            sleep(time_interval)

app = gp.GooeyPieApp("Multiautoclicker")

#win2 = gp.Image(app, 'images/win2.png')

header_lbl = gp.StyleLabel(app, "Multiclicker by Jason")
header_lbl.font_size = 20

mon_sel_lbl = gp.Label(app, "Monitor selection:")
mon_sel_dd = gp.Dropdown(app, ["Monitor 1", "Monitor 2"])
mon_sel_dd.selected_index = 0

interval_lbl = gp.Label(app, "Time interval in seconds:")
interval_num = gp.Number(app, 5, 1200)

win_layout_lbl = gp.Label(app, "Windows layout:")
win_layout_dd = gp.Dropdown(app, ["1 window", "2 windows", "3 windows", "4 windows"])
win_layout_dd.selected_index = 3

runtime_lbl = gp.Label(app, "Runtime:")

start_btn = gp.Button(app, "Start macro", startmacro)
end_btn = gp.Button(app, "End macro", endmacro)

#####################################

app.set_grid(7, 3)
app.add(header_lbl, 1, 1)

app.add(mon_sel_lbl, 2, 1)
app.add(mon_sel_dd, 2, 2)

app.add(interval_lbl, 3, 1)
app.add(interval_num, 3, 2)

app.add(win_layout_lbl, 4, 1)
app.add(win_layout_dd, 4, 2)

app.add(start_btn, 5, 1, align="left")
app.add(end_btn, 5, 2, align="right")

app.add(runtime_lbl, 6, 1)

### windows visualizer, doesnt look good
#app.add(win2, 7, 1, column_span=2)


app.run()