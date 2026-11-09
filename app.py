import customtkinter




app = customtkinter.CTk()
app.geometry("800x600")
app.grid_columnconfigure((0), weight=2)

title_font = customtkinter.CTkFont(size=32, weight="bold")
title = customtkinter.CTkLabel(master=app,height=50,width=50,pady=20,font=title_font, text="Chemical Equation Balancer")
btn = customtkinter.CTkButton(master=app,height=100,width=50,text="Balance Equation", command=balance_equation)
test_btn = customtkinter.CTkButton(master=app,height=60,width=60,text="Run all tests")

app.chm_frame = customtkinter.CTkFrame(master=app,height=50,width=700)
app.chm_frame.configure(fg_color="transparent")
#app.chm_frame.grid_columnconfigure(1, weight=1) use later
app.chm_frame.grid_anchor("center")
eqn_font = customtkinter.CTkFont(size=24)
        
text_left = customtkinter.CTkEntry(master=app.chm_frame,height=50,width=300, font=eqn_font)
text_right = customtkinter.CTkEntry(master=app.chm_frame,height=50,width=300, font=eqn_font)
arrow = customtkinter.CTkLabel(master=app.chm_frame, height=50, width=50, text="->",font=eqn_font)

text_left.grid(row=0,column=0,padx=5,sticky="w",columnspan=5)
arrow.grid(row=0,column=10,padx=5)
text_right.grid(row=0,column=20,padx=5,sticky="e",columnspan=5)

title.grid(row=0,column=0,padx=20,sticky="ew")
app.chm_frame.grid(row=1,column=0,padx=20, pady=(100,150), sticky="ew",columnspan=2)
btn.grid(row=4,column=0,padx=20, columnspan=2, sticky="ew")
test_btn.grid(row=7,column=0,pady=50, padx=20)




app.mainloop()
