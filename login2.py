from tkinter import*
import os

def register():
	global register_screen
	register_screen=Toplevel(main_screen)
	register_screen.title=("register")
	register_screen.geometry("700x500")
	
	global username
	global password
	global password_entry
	global username_entry
	username=StringVar()
	password=StringVar()
	
	Label(register_screen,text="Please enter details below",bg="blue").pack()
	Label(register_screen,text="").pack()
	username_label=Label(register_screen,text="Username *",bg="red")
	username_label.pack()
	username_entry=Entry(register_screen,textvariable=username)
	username_entry.pack()
	
	password_label=Label(register_screen,text="Password *",bg='yellow')
	password_label.pack()
	password_entry=Entry(register_screen,textvariable=password,show="*")
	password_entry.pack()
	Label(register_screen,text="").pack()
	Button(register_screen,text="Register",width=30,height=3,bg="blue",command=register_user).pack()
	
def login():
	global login_screen
	login_screen=Toplevel(main_screen)
	login_screen.title("Login")
	login_screen.geometry("700x5005")
	Label(login_screen,text="Please enter deteils below to login", bg='yellow').pack()
	Label(login_screen,text="",bg='red').pack()
	
	global username_verify
	global password_verify
	
	username_verify=StringVar()
	password_verify=StringVar()
	
	global username_login_entry
	global password_login_entry
	
	Label(login_screen,text="Username *").pack()
	username_login_entry=Entry(login_screen,textvariable=username_verify)
	username_login_entry.pack()
	Label(login_screen,text="",bg='green').pack()
	Label(login_screen,text="Password *",bg='yellow').pack()
	password_login_entry=Entry(login_screen,textvariable=password_verify,show="*")
	password_login_entry.pack()
	Label(login_screen,text="").pack()
	Button(login_screen,text="Login",width=30,height=3,command=login_verify,bg='green').pack()
	
def register_user():
	username_info=username.get()
	password_info=password.get()
	
	file=open(username_info,"w")
	file.write(username_info + "\n")
	file.close()
	
	username_entry.delete(0,END)
	password_entry.delete(0,END)
	
	Label(register_screen,text="Registeration Success",fg="green",font=("calibri",30)).pack()
	
def login_verify():
	username1=username_verify.get()
	password1=password_verify.get()
	username_login_entry.delete(0,END)
	password_login_entry.delete(0,END)
	
	list_of_files=os.listdir()
	if username1 in list_of_files:
		file1=open(username1,"r")
		verify=file1.read().splitlines()
		if password1 in verify:
			login_success()
		else:
			password_not_recognized()
	else:
		user_not_found()
		
def login_success():
	global login_success_screen
	login_success_screen=Toplevel(login_screen)
	login_success_screen.title("success")
	login_success_screen.geometry("700x500")
	Label(login_success_screen,text="Login Success",bg='green').pack()
	Button(login_success_screen,text="OK",command=delete_login_success).pack()
	
def password_not_recognized():
	global password_not_recog_screen
	password_not_recog_screen=Toplevel(login_screen)
	password_not_recog_screen.title("success")
	password_not_recog_screen.geometry("700x500")
	Label(password_not_recog_screen,text="invalid password",bg='red').pack()
	Button(password_not_recog_screen,text="OK",command=delete_password_not_recog_screen).pack()
	
def user_not_found():
	global user_not_found_screen
	user_not_found_screen=Toplevel(login_screen)
	user_not_found_screen.title("success")
	user_not_found_screen.geometry("700x500")
	Label(user_not_found_screen,text="user not found",bg='red').pack()
	Button(user_not_found_screen,text="OK",command=delete_user_not_found_screen).pack()
	
def delete_login_success():
	login_success_screen_destroy()
	
def delete_password_not_recog_screen():
	password_not_recog_screen.destroy()
	
def delete_user_not_found_screen():
	user_not_found_destroy()
	
def main_account_screen():
	global main_screen
	main_screen=Tk()
	main_screen.geometry("700x500")
	main_screen.title("Account Login")
	Label(text="Select your choice",bg="blue",width="500",height="5",font=("Calibri",30))
	Label(text="").pack()
	Button(text="Login",height="5",width="50",command=login,bg='red').pack()
	Label(text="").pack()
	Button(text="Register",height="5",width="50",command=register,bg='green').pack()
	
	main_screen.mainloop()

main_account_screen()
	
	
	

	
