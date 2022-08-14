
import loginLapas, timer, lapas, time, json, os
from datetime import date, datetime
from tkinter import messagebox
from threading import Thread

MAGIC_EXIT = 'polsek123'

running = True
loginned = False
keep_kill = True

def config(key):
    conf = json.loads(open('config.json').read())
    return conf[key]

def valid_json(json_file):
    try:
        json.loads(open(json_file, 'r').read())
        return True
    except (json.JSONDecodeError, FileNotFoundError) as error:    
        return False

def quota_names(name):

    quota_file = 'quotas.json'
    if (not os.path.isfile(quota_file)) or (not valid_json(quota_file)):
        with open(quota_file, 'w+') as qw:
            qw.write(json.dumps({
                'id_last': dict()
            }))
        print('wrote new quotas file')
    
    quotas = None
    with (open(quota_file, 'r') as qr):
        quotas = json.loads(qr.read())
    print('quotas:', quotas)

    toreturn = None

    now = datetime.now()
    id_last = quotas['id_last']
    if name in id_last:
        last = id_last[name]
        last_login = datetime.strptime(last, '%Y-%m-%d %H:%M:%S.%f')
        seconds_from_last = (now-last_login).total_seconds()
        delay_seconds = int(config('delay_jam'))*3600 + int(config('delay_menit'))*60 + int(config('delay_detik'))
        if seconds_from_last > delay_seconds:
            quotas['id_last'][name] = str(datetime.now())
            # qw.write(json.dumps(quotas))
            print('login again')
            toreturn = True, 0
        else:
            toreturn = False, delay_seconds-seconds_from_last
    else:
        quotas['id_last'][name] = str(now)
        # qw.write(json.dumps(quotas))
        toreturn = True, 0
        print('new')

    with open(quota_file, 'w+') as qw:
        qw.write(json.dumps(quotas))
    return toreturn

           

def kill_wa():
    lapas.find_stop('WhatsApp.exe')

def close_kill(win):
    global running, loginned, keep_kill
    running = False
    loginned = False
    keep_kill = False
    win.destroy()
    kill_wa()
    time.sleep(3)
    



def call_log(s0, s1):
    with open('call_logs', 'a+') as cl:
        cl.write(f'Nama Tahanan: {s0}\nNomor sel: {s1}\nWaktu mulai: {str(time.ctime())}\nDurasi: {config("timer_jam")} jam {config("timer_menit")} menit {config("timer_detik")} detik\n\n')

def pending_function(win):
    win.destroy()
    kill_wa()

def login(page, inputs):
    global loginned 
    loginned = True
    if inputs['nama']==MAGIC_EXIT and inputs['nomor_sel']==MAGIC_EXIT:
        close_kill(page.window)

    allowed, remining_seconds = quota_names(inputs['nomor_sel'])
    if not allowed:
        messagebox.showwarning(f"Jatah anda sudah habis", f'bisa dicoba kembali setelah {int(remining_seconds)} detik')
        return 

    call_log(inputs['nama'], str(inputs['nomor_sel']))

    page.window.destroy()
    kill_wa()
    lapas.start_wa()
    time.sleep(5)
    timer.startTimer(config('timer_jam'), config('timer_menit'), config('timer_detik'), pending_function, lambda *x: None)

def keep_kill():
    global keep_kill
    while keep_kill:
        kill_wa()
        time.sleep(3)
    

if __name__=='__main__':
    while running:
        kill_wa()
        Thread(target=keep_kill).start()
        loginLapas.page(login, close_kill)
        messagebox.showinfo('Sesi anda sudah berakhir', 'Jatah anda hari ini sudah habis')
        loginned = False