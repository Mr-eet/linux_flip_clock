#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import time
import datetime

class FlipClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Flip Clock")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")

        # Boş canvas tanımla
        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Fontlar
        self.time_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 180)
        self.date_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)

        # İlk görüntü
        self.image_on_canvas = None

        self.update_clock()

        self.root.bind("<Escape>", lambda e: root.destroy())  # ESC ile çık

    def draw_frame(self, time_str, date_str):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        img = Image.new("RGB", (width, height), color="black")
        draw = ImageDraw.Draw(img)

        # Saat
        bbox_time = draw.textbbox((0, 0), time_str, font=self.time_font)
        w_time = bbox_time[2] - bbox_time[0]
        h_time = bbox_time[3] - bbox_time[1]
        x_time = (width - w_time) // 2
        y_time = (height - h_time) // 2 - 100
        draw.text((x_time, y_time), time_str, font=self.time_font, fill="white")

        # Tarih
        bbox_date = draw.textbbox((0, 0), date_str, font=self.date_font)
        w_date = bbox_date[2] - bbox_date[0]
        h_date = bbox_date[3] - bbox_date[1]
        x_date = (width - w_date) // 2
        y_date = y_time + h_time + 40
        draw.text((x_date, y_date), date_str, font=self.date_font, fill="gray")

        return img

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        today = datetime.datetime.now().strftime("%A, %d %B %Y")

        img = self.draw_frame(now, today)
        tk_img = ImageTk.PhotoImage(img)

        if self.image_on_canvas is None:
            self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
        else:
            self.canvas.itemconfig(self.image_on_canvas, image=tk_img)

        self.canvas.image = tk_img
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = FlipClock(root)
    root.mainloop()
