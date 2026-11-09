import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.grid_columnconfigure((0), weight=2)

        title = customtkinter.CTkLabel(master=self,height=50,width=50,pady=20)
        btn = customtkinter.CTkButton(master=self,height=50,width=50,text="buttom")

        self.chm_frame = CHM_Frame(self)
        #self.chm_frame.configure(fg_color="transparent")
        

        title.grid(row=0,column=0,padx=20,sticky="ew")
        self.chm_frame.grid(row=1,column=0,padx=20, pady=(50,150), sticky="ew",columnspan=2)
        btn.grid(row=2,column=0,padx=20, columnspan=2, sticky="ew")

class CHM_Frame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        text_left = customtkinter.CTkEntry(master=self,height=50,width=100)
        text_right = customtkinter.CTkEntry(master=self,height=50,width=100)
        arrow = customtkinter.CTkLabel(master=self, height=50, width=50, text="->")

        text_left.grid(row=0,column=0,padx=5)
        arrow.grid(row=0,column=1,padx=5)
        text_right.grid(row=0,column=1,padx=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()
