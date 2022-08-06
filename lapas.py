# %%
from audioop import mul
from re import sub
import psutil, time, os, subprocess, traceback, multiprocessing
from threading import Thread

# %%
WHATSAPP_EXE_PATHS = [
    'C:\\Users\\kevin\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
]

CURRENT_WA_EXE = None

for exe in WHATSAPP_EXE_PATHS:
    if os.path.isfile(exe):
        CURRENT_WA_EXE = exe
        break

if CURRENT_WA_EXE is None:
    print('Has Whatsapp been installed?')



# %%

def get_process_info(p):
    try:
        cmdline = p.cmdline()
    except:
        cmdline = None
    return p.name(), cmdline

def find_processes(name_to_find):
    processes = []
    output = open('output.txt', 'w+')
    for p in psutil.process_iter():
        name, cmdline = get_process_info(p)
        if name==name_to_find:
            processes.append(p)
        output.write(name+str(cmdline)+'\n')
    output.close()
    return processes

def stop_process(p):
    try:
        p.terminate()
        p.wait()        
        p.kill()
    except psutil.NoSuchProcess:
        pass

def find_stop(name):
    ps = find_processes(name)
    for p in ps:
        stop_process(p)
    return 0

def _start_process(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()
    for line in process.stdout:
        print(line)

def start_in_new_process(command):
        
    # thread = Thread(target=_start, args=[command])
    # thread.start()
    # return thread

    # pid = os.fork()
    # if pid==0:
    #     _start(command)
    # else:
    #     return pid
    process = multiprocessing.Process(target=_start_process, args=[command])
    process.start()
    return process

def pending_function(seconds, function):
    for i in range(seconds):
        time.sleep(1)
        print(i)
    function()

def start_wa():
    def _start():
        process = subprocess.run(args=[CURRENT_WA_EXE], stdout=subprocess.PIPE)
        
    th = Thread(target=_start)
    th.start()
    return th


        
# %%

if __name__=='__main__':
    # find_stop('WhatsApp.exe')
    # process = start_in_new_process(CURRENT_WA_EXE)
    # try:

    #     # for i in range(7):
    #     #     time.sleep(1)
    #     #     print(i)
    #     input('stop now?')
    #     find_stop('WhatsApp.exe')
    #     process.terminate()
    #     process.kill()
    # except:
    #     print('Exception!')
    #     traceback.print_exc()
    #     find_stop('WhatsApp.exe')
    #     process.terminate()
    #     process.kill()    
    # finally:
    #     find_stop('WhatsApp.exe')
    #     process.terminate()
    #     process.kill()    

    find_stop('WhatsApp.exe')
    # process = subprocess.Popen(CURRENT_WA_EXE, stdout=subprocess.PIPE)
    # subprocess.run(args=[CURRENT_WA_EXE], stdout=subprocess.PIPE)
    start_wa()
    def kill_wa():
        # process.terminate()
        # process.kill()
        # try:
        #     process.terminate()
        #     process.kill()
        # except:
        #     pass
        find_stop('WhatsApp.exe')        
    try:
        
        # Thread(target=pending_function, args=[25, kill_wa]).start()
        pending_function(25, kill_wa)
        
        # process.wait()
        # for line in process.stdout:
        #     print(line)    
        
    except:
        kill_wa()
        
    finally:
        kill_wa()

# %%


# %%



