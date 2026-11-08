import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.grid_columnconfigure((0), weight=2)

        title = customtkinter.CTkLabel(master=self,height=50,width=50,pady=20)
        btn = customtkinter.CTkButton(master=self,height=50,width=50,text="buttom")

        title.grid(row=0,column=0,padx=20,sticky="ew")
        btn.grid(row=1,column=0,padx=20, columnspan=2, sticky="ew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
