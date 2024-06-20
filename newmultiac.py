import gooeypie as gp

app = gp.GooeyPieApp("Multiautoclicker")

test_btn = gp.Button(app, "Test", None)
test_lbl = gp.Label(app, "")

app.set_grid(2, 1)
app.add(test_btn, 1, 1)
app.add(test_lbl, 2, 1)

app.run()