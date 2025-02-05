import tkinter as tk
import time
import math


WIDTH, HEIGHT = 400, 400
CENTER = WIDTH // 2, HEIGHT // 2
RADIUS = 150


tk_root = tk.Tk()
tk_root.title("Analog Clock")
canvas = tk.Canvas(tk_root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

def draw_circle():
    canvas.create_oval(CENTER[0] - RADIUS, CENTER[1] - RADIUS,
                        CENTER[0] + RADIUS, CENTER[1] + RADIUS, outline="black", width=3)
    
    for i in range(1, 13):
        angle = math.radians(90 - i * 30)
        x = CENTER[0] + (RADIUS - 20) * math.cos(angle)
        y = CENTER[1] - (RADIUS - 20) * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"), fill="black")

def draw_hand(angle, length, color, width):
    x = CENTER[0] + length * math.cos(math.radians(angle))
    y = CENTER[1] - length * math.sin(math.radians(angle))
    canvas.create_line(CENTER[0], CENTER[1], x, y, fill=color, width=width)

def update_clock():
    canvas.delete("all")
    draw_circle()
    
    current_time = time.localtime()
    hours, minutes, seconds = current_time.tm_hour % 12, current_time.tm_min, current_time.tm_sec
    
    second_angle = 90 - seconds * 6
    minute_angle = 90 - minutes * 6
    hour_angle = 90 - (hours * 30 + minutes * 0.5)
    
    draw_hand(second_angle, RADIUS - 20, "red", 1)
    draw_hand(minute_angle, RADIUS - 40, "blue", 3)
    draw_hand(hour_angle, RADIUS - 60, "black", 5)
    
    tk_root.after(1000, update_clock)

update_clock()
tk_root.mainloop()
