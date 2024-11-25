from tkinter import *
import speedtest
import threading

root = Tk()
root.title("Internet Speed Test")
root.resizable(False, False)
root.configure(bg="#141527")

w, h = 450, 700
ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = int((ws - w) / 2), int((hs - h) / 2)
root.geometry(f"{w}x{h}+{x}+{y}")


def run_speed_test():
    try:
        Download.config(text="loaing")
        test = speedtest.Speedtest()
        test.get_servers([])
        test.get_best_server()
        download_speed = round(test.download() / (1024 * 1024), 2)
        upload_speed = round(test.upload() / (1024 * 1024), 2)
        ping_result = round(test.results.ping, 2)
        isp = test.results.client["isp"]
        ip_address = test.results.client["ip"]
        root.after(0, update_results, ping_result, download_speed, upload_speed, isp, ip_address)
    except Exception as e:
        root.after(0, show_error, str(e))


def update_results(ping_result, download_speed, upload_speed, isp, ip_address):
    ping.config(text=f"{ping_result}")
    download.config(text=f"{download_speed}")
    upload.config(text=f"{upload_speed}")
    Download.config(text=f"{download_speed}")
    service.config(text=isp)
    ip.config(text=ip_address)


def show_error(error_message):
    Download.config(text="Error")
    print(f"Error: {error_message}")


def start_test():
    threading.Thread(target=run_speed_test, daemon=True).start()


def reset_results():
    ping.config(text="--")
    download.config(text="--")
    upload.config(text="--")
    Download.config(text="--")
    service.config(text="- - -")
    ip.config(text="- - - - - - - -")


image_icon = PhotoImage(file=r"C:\cit collage\internet speed test\Speed-Test-main\Speed-Test-main\images\logo.png")
root.iconphoto(False, image_icon)
Top = PhotoImage(file=r"C:\cit collage\internet speed test\Speed-Test-main\Speed-Test-main\images\background3.png")
Test_Image = PhotoImage(file=r"C:\cit collage\internet speed test\Speed-Test-main\Speed-Test-main\images\button.png")
Reset_Image = PhotoImage(file=r"C:\cit collage\internet speed test\Speed-Test-main\Speed-Test-main\images\reset.png")

Label(root, image=Top, bg="#141527").place(x=0, y=0)

Test_Button = Button(root, image=Test_Image, bg="#141527", bd=0,
                     activebackground="#141527", cursor="hand2", command=start_test)
Test_Button.place(x=125, y=510)

Reset_Button = Button(root, image=Reset_Image, bg="#141527", bd=0,
                      activebackground="#141527", cursor="hand2", command=reset_results)
Reset_Button.place(x=190, y=600)

ping = Label(root, text="--", font="arial 20", bg="#141527", fg="#e9b342")
ping.place(x=100, y=215, anchor="center")

download = Label(root, text="--", font="arial 20", bg="#141527", fg="#0cf107")
download.place(x=225, y=215, anchor="center")

upload = Label(root, text="--", font="arial 20", bg="#141527", fg="#e61c25")
upload.place(x=350, y=215, anchor="center")

Download = Label(root, text="--", font="arial 30", bg="#141527", fg="#00FFFF")
Download.place(x=225, y=430, anchor="center")

service = Label(root, text="- - -", font="arial 12", bg="#141527", fg="white")
service.place(x=55, y=590, anchor="center")

ip = Label(root, text="- - - - - - - -", font="arial 12", bg="#141527", fg="white")
ip.place(x=380, y=590, anchor="center")

root.mainloop()
