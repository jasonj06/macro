import pyautogui
from time import sleep, time
import gooeypie as gp

mouse_pos = []

def startmacro(event):
    global mouse_pos
    monitor = int(mon_sel_dd.selected_index)
    if monitor == 0:
        mouse_pos.append((863, 260))
        mouse_pos.append((1083, 264))
        mouse_pos.append((1075, 755))
        mouse_pos.append((822, 759))

    elif monitor == 2:
        mouse_pos.append((2717, 312))
        mouse_pos.append((3003, 313))
        mouse_pos.append((2962, 772))
        mouse_pos.append((2753, 785))


app = gp.GooeyPieApp("Multiautoclicker")

win2 = gp.Image(app, 'images/win2.png')

header_lbl = gp.StyleLabel(app, "Multiclicker by Jason")
header_lbl.font_size = 20

mon_sel_lbl = gp.Label(app, "Monitor selection:")
mon_sel_dd = gp.Dropdown(app, ["Monitor 1", "Monitor 2"])

interval_lbl = gp.Label(app, "Time interval in seconds:")
interval_inp = gp.Number(app, 5, 1200)

win_layout_lbl = gp.Label(app, "Windows layout:")
win_layout_dd = gp.Dropdown(app, ["1 window", "2 windows", "3 windows", "4 windows"])
win_layout_dd.selected_index = 3

runtime_lbl = gp.Label(app, "Runtime:")

start_btn = gp.Button(app, "Start macro", startmacro)
end_btn = gp.Button(app, "End macro", None)

#####################################

app.set_grid(7, 3)
app.add(header_lbl, 1, 1)

app.add(mon_sel_lbl, 2, 1)
app.add(mon_sel_dd, 2, 2)

app.add(interval_lbl, 3, 1)
app.add(interval_inp, 3, 2)

app.add(win_layout_lbl, 4, 1)
app.add(win_layout_dd, 4, 2)

app.add(start_btn, 5, 1, align="left")
app.add(end_btn, 5, 2, align="right")

app.add(runtime_lbl, 6, 1)

### windows visualizer, doesnt look good
# app.add(win2, 5, 1)

app.run()