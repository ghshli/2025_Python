from tkinter import *
import random
import time

tk = Tk()
tk.title("Game 01")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = 0     
score_text = None  

def update_score():
    global score_text
    canvas.delete(score_text)
    score_text = canvas.create_text(450, 30, text=f"Score: {score}",
                                    fill="black", font=("Helvetica", 15, "bold"))

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global score
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if not self.hit_bottom:
            if self.hit_paddle(pos):
                self.y = -3
                score += 1       
                update_score()
                
                # 공 색깔 랜덤 변경(공이 패들에 닿을 때마다 공 색 바뀜) -> 아이디어 추가 부분
                colors = ["red", "blue", "green", "yellow", "purple", "orange"]
                new_color = random.choice(colors)
                self.canvas.itemconfig(self.id, fill=new_color)

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


def restart_game():
    global score
    canvas.delete("all")
    score = 0             
    start_game()

def start_game():
    global ball, paddle, score_text
    canvas.delete("all")

    score_text = canvas.create_text(450, 30, text="Score: 0",
                                    fill="black", font=("Helvetica", 15, "bold"))

    paddle = Paddle(canvas, "blue")
    ball = Ball(canvas, paddle, "red")

    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
        else:
            canvas.create_text(250, 200, text="GAME OVER", fill="red",
                               font=("Helvetica", 30, "bold"))

            btn = Button(tk, text="RESTART", command=restart_game)
            canvas.create_window(250, 250, window=btn)
            break

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

start_game()
tk.mainloop()