import os
import tkinter as tk
from tkinter import ttk, messagebox

from bot_commands import *
from get_client import stop_clients, create_bots
from settings import *

close_button_color = '#F35F41'
run_button_color = '#87B86F'
backgroundcolor = '#CFDEDF'
font = 'Helvetica 16 bold'
font_small = 'Helvetica 11'


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Bot Manager')
        self.configure(bg=backgroundcolor)
        window_height = 500
        window_width = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        title = tk.Label(self, text="Bot Manager", font=font, bg=backgroundcolor)
        title.pack(side='top', pady=10, padx=10)

        self.run_button()

        self.bar = ttk.Progressbar(self, orient='horizontal', length=400)

    def create_bots_animation(self, n=0):
        self.bar['value'] = n
        if n > 100:
            self.ms_creating_bots.pack_forget()
            self.bar.pack_forget()
            messagebox.showinfo(title='Info', message=txt_bots_are_created)
            self.commands()
        else:
            self.after(30, self.create_bots_animation, n + 1)

    def tki(self, txt_enter_number_of_bots):
        button_pressed = tk.StringVar()
        self.msg = tk.Label(self, text=txt_enter_number_of_bots, font=font, bg=backgroundcolor)
        self.data = tk.Entry(self)
        self.create_bots_button = tk.Button(self, text='Ok', command=lambda: button_pressed.set("button pressed"))
        self.msg.pack(pady=20)
        self.data.pack(pady=21)
        self.create_bots_button.pack(pady=22)
        self.create_bots_button.wait_variable(button_pressed)
        try:
            self.number_of_bots = int(self.data.get())
        except ValueError:
            self.number_of_bots = 0

    def hide_tki(self):
        self.msg.pack_forget()
        self.data.pack_forget()
        self.create_bots_button.pack_forget()

    def run(self):
        self.run.pack_forget()

        # get number of bots
        self.number_of_bots = 0
        while self.number_of_bots <= 0 or self.number_of_bots > max_amount_of_bots:
            self.tki(txt_enter_number_of_bots)
            self.hide_tki()
            if self.number_of_bots <= 0 or self.number_of_bots > max_amount_of_bots:
                print(txt_positive_number)
                messagebox.showinfo(title='Info', message=txt_positive_number)

        self.ms_creating_bots = tk.Label(self, text=txt_the_process_of_creating_bots, font=font, bg=backgroundcolor)
        self.ms_creating_bots.pack(pady=20)
        self.ms_creating_bots.update_idletasks()
        self.clients = create_bots(self.number_of_bots)
        self.bar.pack(pady=30)
        self.create_bots_animation()

    # def create_bots(self):
    #     urls = create_and_registaer_bots(self.number_of_bots, os.getenv('ROOM_ID'))
    #     pool = ThreadPool(10)
    #     self.clients = pool.map(get_client, urls)
    #     pool.close()
    #     pool.join()

    def run_button(self):
        self.run = tk.Button(self, text=txt_run_app_button, command=self.run)
        self.run.config(bg=run_button_color)
        self.run.pack(pady=50, padx='50', fill='x')

    def commands_window(self):
        button_pressed = tk.StringVar()
        self.ms_command = tk.Label(self, text=txt_start_commands, font=font, bg=backgroundcolor)
        self.command_data = tk.Entry(self)
        self.run_command_button = tk.Button(self, text=txt_run_app_button, command=lambda: button_pressed.set("button pressed"))
        self.ms_command.pack(pady=20)
        self.command_data.pack(pady=21)
        self.run_command_button.pack(pady=22)
        self.run_command_button.wait_variable(button_pressed)
        self.command = self.command_data.get()

    def hide_commands_window(self):
        self.ms_command.pack_forget()
        self.command_data.pack_forget()
        self.run_command_button.pack_forget()

    def commands(self):
        log_window = Log(self)
        log_window.geometry('500x500')
        self.ms_creating_bots.pack_forget()
        while self.command != 'exit':
            self.commands_window()
            available_commands = get_available_commands(way_to_receive_commands_and_messages)
            if self.command in available_commands.keys():
                try:
                    result = universal_command(self.clients, self.command, available_commands)
                    if result:
                        log_window.add_log(f'{txt_command_completed_successfully}: {self.command}')
                    else:
                        log_window.add_log(f'{txt_command_has_not_been_implemented}: {self.command}')

                    # for test
                    # print(universal_command_test(self.clients, self.command))
                except Exception as e:
                    print(e)
                    log_window.add_log(f'{txt_command_has_not_been_implemented}: {e}')
            elif self.command == 'exit':
                break
            else:
                print(txt_command_not_found)
                log_window.add_log(f'{txt_command_has_not_been_implemented}: {txt_command_not_found}')
            self.hide_commands_window()

        stop_clients(self.clients)

    def on_closing(self):
        if messagebox.askokcancel("Quit", txt_exit):
            try:
                stop_clients(self.clients)
            except Exception as e:
                print(e)
            finally:
                app.destroy()
                os._exit(0)


class Log(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def add_log(self, message):
        self.ms_last_command_fail = tk.Label(self, text=message, font=font_small, bg=backgroundcolor)
        self.ms_last_command_fail.pack()

    def create_widgets(self):
        tk.Label(self, text='Logs').pack(padx=20, pady=50)


if __name__ == '__main__':
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
