from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  my_label.config(text="Timer", fg=GREEN)
  check_label.config(text=" ", fg=GREEN)
  global rep
  rep=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def show_time():
  global rep 
  rep+=1
  work_sec=WORK_MIN*60
  short_break_sec=SHORT_BREAK_MIN*60
  long_break_sec=LONG_BREAK_MIN*60
  if rep%8==0:
    count_down(long_break_sec)
    my_label.config(text="Break", fg=RED)


    
  elif rep%2==0:
    count_down(short_break_sec)
    my_label.config(text="Break", fg=PINK)
    
  else: 
    count_down(work_sec)
    my_label.config(text="Work", fg=GREEN)
  


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min=math.floor(count/60)
  count_sec=count%60

  if count_sec<10:
    count_sec=f"0{count_sec}"


  
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

  if count>0:
    global timer
    timer=window.after(1000, count_down, count-1)

  else:
    show_time()
    if rep%2==0:
      check="✔"
      check_number=int(rep/2)
      check_label.config(text=check*check_number, fg=GREEN)
 



  
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

my_label=Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Ariel", 35, "bold"))
my_label.grid(row=1, column=2)
canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
canvas.grid(row=2, column=2)


timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button=Button(text="Start", highlightthickness=0, command=show_time)
start_button.grid(row=3, column=1)
reset_button=Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=3, column=3)

check_label=Label(bg=YELLOW, fg=GREEN, font=("Ariel", 25, "bold"))
check_label.grid(row=4, column=2)

window.mainloop()