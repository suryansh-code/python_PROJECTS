from tkinter import *
from PIL import Image,ImageTk




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

        #================= HTE TOP IMAGE ================================
        img1=Image.open(r"C:\Users\tarag\git\mini_project\images\hotel1.png")
        img1=img1.resize((1550,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        label_img.place(x=0,y=0,width=1550,height=140)

        #========================title=====================================
        lb1_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=140,width=1550,height=50)


        #===========================MAIN FRAME ============================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        lb1_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_menu.place(x=0,y=0,width=230)

        #=============================BUTTON_FRAME================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)

        detail_btn=Button(btn_frame,text="DETAIL",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        detail_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="RERPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)

        #============================RIGHT SIDE IMAGE==================================
        img3=Image.open(r"C:\Users\tarag\git\mini_project\images\back2.png")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lb_img1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lb_img1.place(x=225,y=0,width=1310,height=590)

if __name__ == "__main__":
        root=Tk()
        obj=HotelManagementSystem(root)
        root.mainloop()