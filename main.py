import yt_dlp
import customtkinter
from tkinter import DISABLED
import os

# Set the theme and color options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.title('YOUTUBE MP3 VIDEO DOWNLOADER')
        self.geometry('800x550')
        self.resizable(False, False)

        self.Title = customtkinter.CTkTextbox(
            self, 
            width = 400,
            height = 90,
            font = ("Ubuntu", 28),
            border_spacing = 15,
            text_color = "silver",
            corner_radius = 25,
            border_width = 3,
            activate_scrollbars = False,
            border_color = "silver")
        self.Title.pack(pady = 20)
        self.Title.insert('end', "Youtube MP3 Downloader")
        self.Title.configure(state = DISABLED)

        self.frame = customtkinter.CTkFrame(
            self,
            width = 400,
            height = 190,
            corner_radius = 25,
            border_width = 3,
            border_color = "silver")
        self.frame.pack(pady = 10)

        url_input_label = customtkinter.CTkLabel(
            self.frame,
            width = 130,
            height = 30,
            text_color = 'silver',
            text = "Enter youtube video url:",
            font = ("Ubuntu", 16),
            compound = "center")
        url_input_label.place(x = 120, y = 10)
        url_input_label.pack(pady = 20, padx = 120)
        
        self.url_input_entry = customtkinter.CTkEntry(
            self.frame,
            width = 380,
            height = 50,
            border_color = 'silver',
            font = ("Ubuntu", 14),
            text_color = "silver")
        self.url_input_entry.place(x = 20, y = 50)
        self.url_input_entry.pack(pady = 20, padx = 30)

        download_button = customtkinter.CTkButton(
            self.frame,
            text = "Download",
            font = ("Ubuntu", 16),
            width = 150,
            height = 50, 
            corner_radius = 25,
            command = self.download_audio)
        download_button.place(x = 100, y = 130)
        download_button.pack(pady = 30, padx = 30)

        self.status_label = customtkinter.CTkLabel(
            self, 
            text = "", 
            font = ("Ubuntu", 16),
            text_color = "green")
        self.status_label.pack(pady = 10)

    def download_audio(self):
        yt_url = self.url_input_entry.get()
        directory = os.path.expanduser("~/Downloads")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': '/snap/bin/ffmpeg', # adjust this path of where ffmpeg is on your computer
            'outtmpl': os.path.join(directory, '%(title)s.%(ext)s')}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(yt_url, download=True)
                file_path = ydl.prepare_filename(info_dict)
            self.status_label.configure(text = f"Download successful!\nFile saved to: {file_path}")

            open_folder_button = customtkinter.CTkButton(
            self, 
            text = "Open Folder",
            font = ("Ubuntu", 14),
            width = 120,
            height = 30,
            corner_radius = 25,
            command = self.open_downloads_folder)
            open_folder_button.pack(pady = 10)

        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}", text_color="silver")

    def open_downloads_folder(self):
        download_dir = os.path.expanduser("~/Downloads")
        os.system(f'xdg-open "{download_dir}"' if "linux" in os.uname().sysname.lower() else f'open "{download_dir}"')

if __name__ == "__main__": 
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")