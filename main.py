import loginLapas, timer, lapas, time, json

def kill_wa():
    lapas.find_stop('WhatsApp.exe')

def close_kill(win):
    win.destroy()
    kill_wa()

def config(key):
    conf = json.loads(open('config.json').read())
    return conf[key]

def call_log(s0, s1):
    with open('call_logs', 'a+') as cl:
        cl.write(f'Nama Tahanan: {s0}\nNomor sel: {s1}\nWaktu mulai: {str(time.ctime())}\nDurasi: {config("jam")} jam {config("menit")} menit {config("detik")} detik\n\n')

kill_wa()

def pending_function(win):
    win.destroy()
    kill_wa()

def login(page, inputs):
    call_log(inputs['nama'], str(inputs['nomor_sel']))

    page.window.destroy()
    kill_wa()
    lapas.start_wa()
    time.sleep(5)
    timer.startTimer(config('jam'), config('menit'), config('detik'), pending_function, close_kill)

loginLapas.page(login, close_kill)