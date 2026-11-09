import customtkinter
from main import app_main
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.grid_columnconfigure((0), weight=2)
        title_font = customtkinter.CTkFont(size=32, weight="bold")
        title = customtkinter.CTkLabel(master=self,height=50,width=50,pady=20, font=title_font, text="Chemical Balancer")
        btn = customtkinter.CTkButton(master=self,height=50,width=50,text="Balance Equation", command=self.get_text)

        self.chm_frame = CHM_Frame(self)
        self.chm_frame.configure(fg_color="transparent")
        

        title.grid(row=0,column=0,padx=20,sticky="ew")
        self.chm_frame.grid(row=1,column=0,padx=20, pady=(100,150), sticky="ew",columnspan=2)
        btn.grid(row=4,column=0,padx=20, columnspan=2, sticky="ew")
        btn.grid(row=6,column=0,pady=20)

    def get_text(self):
        text_left = self.chm_frame.get_text_left()
        text_right = self.chm_frame.get_text_right()
        full_equation = f"{text_left} -> {text_right}"
        print(full_equation)
        app_main(full_equation)


class CHM_Frame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        eqn_font = customtkinter.CTkFont(family="Eqn_font", size=24)
        
        self.text_left = customtkinter.CTkEntry(master=self,height=50,width=340, font=eqn_font)
        self.text_right = customtkinter.CTkEntry(master=self,height=50,width=340, font=eqn_font)
        arrow = customtkinter.CTkLabel(master=self, height=50, width=50, text="→",font=eqn_font)

        self.text_left.grid(row=0,column=0,padx=5,sticky="e")
        arrow.grid(row=0,column=1,padx=5)
        self.text_right.grid(row=0,column=2,padx=5,sticky="w")

    def get_text_left(self):
        return self.text_left.get()

    def get_text_right(self):
        return self.text_right.get()

if __name__ == "__main__":
    app = App()
    app.mainloop()
