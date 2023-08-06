from tkadw import *

root = Adwite(wincaption=(53, 53, 53))
root.set_default_theme("metro", "dark")

frame = AdwTFrame(root)

label1 = AdwTLabel(frame.frame, text="GTkLabel")
label1.row(padx=5, pady=5)

button1 = AdwTButton(frame.frame, text="GTkButton")
button1.row(padx=5, pady=5)

separator1 = AdwTSeparator(frame.frame)
separator1.row(padx=5, pady=5)

entry1 = AdwTEntry(frame.frame, text="GTkEntry")
entry1.row(padx=5, pady=5)

textbox1 = AdwTText(frame.frame)
textbox1.tinsert("1.0", "GTkTextBox")
textbox1.row(padx=5, pady=5)

frame.pack(fill="both", expand="yes", padx=5, pady=5)

root.mainloop()