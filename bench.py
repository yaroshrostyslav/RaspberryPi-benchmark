from decimal import *
from tkinter import *
import tkinter.ttk as ttk
import time
import shutil
import zipfile
# for get machine info
import sys, os, platform, subprocess
sys.path.append("packages/")
import cpuinfo
from cpuinfo import get_cpu_info
from threading import Thread

#config
RUN_TIME = 60;

default_b1 = 626;
default_b2 = 19550516;
default_b3 = 7214769;
default_b4 = 33477349;
default_b5 = 4867;

k_1 = Decimal(1) / Decimal(default_b1);
k_2 = Decimal(0.3) / Decimal(default_b2);
k_3 = Decimal(5) / Decimal(default_b3);
k_4 = Decimal(3) / Decimal(default_b4);
k_5 = Decimal(0.7) / Decimal(default_b5);

res_1 = 0;
res_2 = 0;
res_3 = 0;
res_4 = 0;
res_5 = 0;

sudo_password = '';

#1
def copy_files():
    time.sleep(1)
    start_time_left.place(relx=0.5, rely=0.60, anchor=CENTER);
    start_logs.insert(3.0, 'Running test 1 - Flash memory write\n')
    start_title.config(text='Test 1 of 5: Flash memory write');
    start_progress.stop();
    start_progress.start(RUN_TIME*10);
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        count += 1;
        shutil.copyfile(r'files/image.jpg', r'temp/image.jpg');
        if (time.time() >= time_end):
            global res_1
            res_1 = count;
            res = res_1 * k_1;
            start_logs.insert(4.0, "Result test 1 - "+'%f' % res + "\n");
            start_logs.see(END);
            start_progress.stop();
            Thread(target=find_hash).start();
            return count;

#2
def find_hash():
    file = 'files/PRO_WPA.txt';
    start_time_left.config(text='4 minutes left');
    start_logs.insert(5.0, 'Running test 2 - RAM speed\n')
    start_title.config(text='Test 2 of 5: RAM speed');
    start_progress.start(RUN_TIME*10);
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        with open(file, 'r') as read_file:
            for line in read_file:
                new_line = line.strip('\n')
                count += 1;
                if (time.time() >= time_end):
                    global res_2
                    res_2 = count;
                    res = res_2 * k_2;
                    start_logs.insert(6.0, "Result test 2 - "+'%f' % res + "\n");
                    start_logs.see(END);
                    start_progress.stop();
                    Thread(target=test_integer).start();
                    return count;

#3
def test_integer():
    start_time_left.config(text='3 minutes left');
    start_logs.insert(7.0, 'Running test 3 - Integer operations\n')
    start_title.config(text='Test 3 of 5: Integer operations');
    start_progress.start(RUN_TIME*10);
    time_end = time.time() + RUN_TIME;
    count = 0;
    b = 0;
    while True:
        count += 1;
        b += 22226545*22+26216*222+88**88*88;
        if (time.time() >= time_end):
            global res_3
            res_3 = count;
            res = res_3 * k_3;
            start_logs.insert(8.0, "Result test 3 - "+'%f' % res + "\n");
            start_logs.see(END);
            start_progress.stop();
            Thread(target=test_float).start();
            return count;

#4
def test_float():
    start_time_left.config(text='2 minutes left');
    start_logs.insert(9.0, 'Running test 4 - Floating point operations\n')
    start_title.config(text='Test 4 of 5: Floating point operations');
    start_progress.start(RUN_TIME*10);
    time_end = time.time() + RUN_TIME;
    count = 0;
    b = 0.1;
    while True:
        count += 1;
        b += 0.01;
        if (time.time() >= time_end):
            global res_4
            res_4 = count;
            res = res_4 * k_4;
            start_logs.insert(10.0, "Result test 4 - "+'%f' % res + "\n");
            start_logs.see(END);
            start_progress.stop();
            Thread(target=create_archive).start();
            return count;

#5
def create_archive():
    start_time_left.config(text='1 minutes left');
    start_logs.insert(11.0, 'Running test 5 - Archiving data operations\n')
    start_title.config(text='Test 5 of 5: Archiving data operations');
    start_progress.start(RUN_TIME*10);
    time_end = time.time() + RUN_TIME;
    count = 0;
    while True:
        count += 1;
        newzip=zipfile.ZipFile(r'temp/images.zip','w');
        newzip.write(r'files/image.jpg');
        if (time.time() >= time_end):
            global res_5
            res_5 = count;
            res = res_5 * k_5;
            start_logs.insert(12.0, "Result test 5 - "+'%f' % res + "\n");
            start_logs.see(END);
            start_progress.stop();
            get_result();
            return count;

def get_result():
    calc_1 = res_1 * k_1;
    calc_2 = res_2 * k_2;
    calc_3 = res_3 * k_3;
    calc_4 = res_4 * k_4;
    calc_5 = res_5 * k_5;
    result = calc_1 + calc_2 + calc_3 + calc_4 + calc_5;
    start_title.config(text="Result\n"+'%.2f' % result, anchor=CENTER, fg='#053b66', font="Arial 20 bold");
    start_logs.insert(13.0, "Result All Tests - "+'%.2f' % result);
    start_progress.place_forget();
    start_time_left.place_forget();
    btn_end = Button(root, text="Ok", width=12, height=1, font="Arial 14");
    btn_end.place(relx=0.35, rely=0.69, anchor=CENTER);
    btn_other_result = Button(root, text="Other results", width=12, height=1, font="Arial 14");
    btn_other_result.place(relx=0.65, rely=0.69, anchor=CENTER);
    def click_btn_end(event):
        global start_progress
        start_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=350, mode='determinate', value=0);
        start_logs.place_forget();
        start_logs.delete('1.0', END);
        start_title.place_forget();
        btn_end.place_forget();
        btn_other_result.place_forget();
        btn_start_test.place(relx=0.5, rely=0.57, anchor=CENTER);
        body_info_proc.place(width=100, relx=0, rely=0.85);
        body_info_proc_value.place(relx=0.20, rely=0.85);
        body_info_os.place(width=100, relx=0, rely=0.71);
        body_info_os_value.place(relx=0.20, rely=0.71);
        body_info_user.place(width=100, relx=0, rely=0.78);
        body_info_user_value.place(relx=0.20, rely=0.78);
        body_info_temp.place(width=100, relx=0, rely=0.92);
        btn_get_tempature.place(relx=0.22, rely=0.92);
    def click_btn_other_result(event):
        b = Toplevel();
        b.title("Benchmark v1.0 - Other results");
        b.configure(bg='#fff');
        window__width = 600;
        window_height = 380;
        window_x = b.winfo_screenwidth() // 2 - (window__width//2);
        window_y = b.winfo_screenheight() // 2 - (window_height//2);
        b.geometry(str(window__width)+'x'+str(window_height)+'+'+str(window_x)+'+'+str(window_y-50));
        body_img_results = Label(b, image=img_results, bg='#fff');
        body_img_results.pack(expand=1);
        
    btn_end.bind("<ButtonRelease-1>", click_btn_end);
    btn_other_result.bind("<ButtonRelease-1>", click_btn_other_result);

def exit_program():
    root.destroy();

def about_program():
    a = Toplevel();
    a.title("Benchmark v1.0 - About");
    a.configure(bg='#fff');
    window__width = 300;
    window_height = 200;
    window_x = a.winfo_screenwidth() // 2 - (window__width//2);
    window_y = a.winfo_screenheight() // 2 - (window_height//2);
    a.geometry(str(window__width)+'x'+str(window_height)+'+'+str(window_x)+'+'+str(window_y-50));
    Label(a, text="Benchmark v1.0 for Raspberry pi \n\n Developer: Yarosh Rostyslav \n\n Copyright © 2020", bg='#fff', font="Arial 11").pack(expand=1);

def click_start(event=''):
    global alert_start
    alert_start = Toplevel();
    alert_start.title("Benchmark v1.0 - Start Tests");
    alert_start.configure(bg='#fff');
    window__width = 300;
    window_height = 200;
    window_x = alert_start.winfo_screenwidth() // 2 - (window__width//2);
    window_y = alert_start.winfo_screenheight() // 2 - (window_height//2);
    alert_start.geometry(str(window__width)+'x'+str(window_height)+'+'+str(window_x)+'+'+str(window_y));
    Label(alert_start, text="Please close all third-party applications \n to get an accurate result!", bg='#fff', fg='#f00', font="Arial 11").place(relx=0.5, rely=0.35, anchor=CENTER);
    btn_start = Button(alert_start, text="Start", width=15, height=1, font="Arial 12 bold");
    btn_start.place(relx=0.5, rely=0.70, anchor=CENTER);
    btn_start.bind("<ButtonRelease-1>", click_start_test);

# after click start
def click_start_test(event):
    alert_start.destroy();
    start_title.config(text='Loading...', fg='#000', font="Arial 15");
    btn_start_test.place_forget();
    body_info_proc.place_forget();
    body_info_proc_value.place_forget();
    body_info_os.place_forget();
    body_info_os_value.place_forget();
    body_info_user.place_forget();
    body_info_user_value.place_forget();
    body_info_temp.place_forget();
    btn_get_tempature.place_forget();
    body_info_temp_value.place_forget();

    start_title.place(relx=0.5, rely=0.54, anchor=CENTER);
    start_progress.place(relx=0.5, rely=0.66, anchor=CENTER);
    start_progress.start(10);
    start_logs.place(relx=0.5, rely=0.90, anchor=CENTER);
    start_logs.insert(1.0, 'Loading...\n')
    start_logs.insert(2.0, 'Starting tests...\n')
    
    # Thread(copy_files())
    Thread(target=copy_files).start();


def get_tempature(event):
    os_name = platform.system();
    temp = 0;
    def save_password(event):
        global sudo_password;
        if (sudo_password == ''):
            sudo_password = body_input.get()
            root2.destroy();
        command = 'powermetrics -n 1 -i 1 --samplers smc'.split();
        cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE);
        cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE);
        output = cmd2.stdout.read().decode();
        lst = output.split('CPU die temperature');
        lst2 = lst[1].split('CPU Plimit:');
        lst3 = lst2[0].replace(':', '').replace('\n', '');
        temp = lst3[1:];
        global body_info_temp_value
        btn_get_tempature.place_forget();
        body_info_temp_value.config(text=temp);
        body_info_temp_value.place(relx=0.21, rely=0.92);
        
    if (os_name == "Darwin"):
        global sudo_password;
        if (sudo_password == ''):
            root2 = Toplevel(root)
            root2.title("Benchmark v1.0");
            window__width = 250;
            window_height = 200;
            window_x = root2.winfo_screenwidth() // 2 - (window__width//2);
            window_y = root2.winfo_screenheight() // 2 - (window_height//2);
            root2.geometry(str(window__width)+'x'+str(window_height)+'+'+str(window_x)+'+'+str(window_y-50));
            # root2.overrideredirect(True)

            body_title = Label(root2, text='Please enter admin password:', width=window__width, fg='#000', font="Arial 15");
            body_input = Entry(root2, width=50);
            btn_ok = Button(root2, text="OK", width=6, height=1, font="Arial 14")

            body_title.place(x=0, y=50, width=window__width, height=20);
            body_input.place(x=15, y=88, width=window__width-30, height=25);
            btn_ok.place(x=70, y=120, width=window__width-140, height=25);

            btn_ok.bind("<ButtonRelease-1>", save_password);
        else:
            save_password(0)

    elif (os_name == "Linux"):
        get_temp = os.popen('vcgencmd measure_temp').readline();
        temp = get_temp.replace("temp=", "").replace('\n', '');
        btn_get_tempature.place_forget();
        body_info_temp_value.config(text=temp);
        body_info_temp_value.place(relx=0.21, rely=0.92);
    elif (os_name == "Windows"):
        btn_get_tempature.place_forget();
        body_info_temp_value.place(relx=0.22, rely=0.92);


def get_osPlatform():
    os_name = platform.system();
    if (os_name == "Darwin"):
        return "Mac OS";
    else:
        return os_name;

name_cpu = get_cpu_info()['brand_raw'].replace('  ', '');
name_os_platform = get_osPlatform();

#user name computer
pc_username = platform.uname()[1]


# GUI
root = Tk();
root.title("Benchmark v1.0");
# root.iconbitmap('files/pi.ico');
root.configure(bg='#fff');
window__width = 550;
window_height = 450;
window_x = root.winfo_screenwidth() // 2 - (window__width//2);
window_y = root.winfo_screenheight() // 2 - (window_height//2);
root.geometry(str(window__width)+'x'+str(window_height)+'+'+str(window_x)+'+'+str(window_y-50));

# Menu
mainmenu = Menu(root);
root.config(menu=mainmenu);

actionmenu = Menu(mainmenu, tearoff=0);
actionmenu.add_command(label="Start tests", command=click_start);
actionmenu.add_command(label="Exit", command=exit_program);

helpmenu = Menu(mainmenu, tearoff=0);
helpmenu.add_command(label="About", command=about_program);

mainmenu.add_cascade(label="Action", menu=actionmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)


body_top = Label(root, text='Benchmark for Raspberry Pi', anchor='w', justify='left', padx=10, height=2, width=window__width, fg='#fff', bg='#053b66', font="Arial 15");

img_logo = PhotoImage(file='files/logo150.gif');
body_logo = Label(root, image=img_logo, bg='#fff');

img_results = PhotoImage(file='files/other_results.gif');

btn_start_test = Button(root, text="Start Tests", width=15, height=1, font="Arial 15 bold")

body_info_os = Label(root, height=1, text='OS', width=window__width, anchor='w', padx=10, font='Arial 15', bg='#fff');
body_info_os_value = Label(root, height=1, text=name_os_platform, anchor='w', padx=10, font='Arial 15', bg='#fff');

body_info_user = Label(root, height=1, text='User', width=window__width, anchor='w', padx=10, font='Arial 15', bg='#fff');
body_info_user_value = Label(root, height=1, text=pc_username, anchor='w', padx=10, font='Arial 15', bg='#fff');

body_info_proc = Label(root, height=1, text='Processor', anchor='w', padx=10, font='Arial 15', bg='#fff');
body_info_proc_value = Label(root, height=1, text=name_cpu, anchor='w', padx=10, font='Arial 15', bg='#fff');

body_info_temp = Label(root, height=1, text='Tempature', width=window__width, anchor='w', padx=10, font='Arial 15', bg='#fff');
body_info_temp_value = Label(root, height=1, text='Not supported', anchor='w', padx=6, font='Arial 15', bg='#fff');
btn_get_tempature = Button(root, text="Get", width=6, height=1, font="Arial 14");

# for windows os
if (name_os_platform == 'Windows'):
    btn_start_test.config(font='Arial 13 bold');
    body_info_os.config(font='Arial 13');
    body_info_os_value.config(font='Arial 13');
    body_info_user.config(font='Arial 13');
    body_info_user_value.config(font='Arial 13');
    body_info_proc.config(font='Arial 13');
    body_info_proc_value.config(font='Arial 13');
    body_info_temp.config(font='Arial 13');
    body_info_temp_value.config(font='Arial 13');
    btn_get_tempature.config(font='Arial 10');


#click start
start_title = Label(root, text='Loading...', anchor=CENTER, height=2, width=window__width, bg='#fff', fg='#000', font="Arial 15");
start_time_left = Label(root, text='5 minutes left', anchor=CENTER, height=1, width=window__width, bg='#fff', fg='#000', font="Arial 11");
start_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=350, mode='determinate', value=0)
start_logs = Text(width=61, height=5, bg="#eff0f1", fg='#333', wrap=WORD)

body_top.place(x=0, y=0);
body_logo.place(width=140, height=140, relx=0.5, rely=0.32, anchor=CENTER);
btn_start_test.place(relx=0.5, rely=0.57, anchor=CENTER);

body_info_os.place(width=110, relx=0, rely=0.71);
body_info_os_value.place(relx=0.21, rely=0.71);

body_info_user.place(width=110, relx=0, rely=0.78);
body_info_user_value.place(relx=0.21, rely=0.78);

body_info_proc.place(width=110, relx=0, rely=0.85);
body_info_proc_value.place(relx=0.21, rely=0.85);

body_info_temp.place(width=110, relx=0, rely=0.92);

btn_get_tempature.place(relx=0.23, rely=0.92);




btn_start_test.bind("<ButtonRelease-1>", click_start);
btn_get_tempature.bind("<ButtonRelease-1>", get_tempature);


root.mainloop();










