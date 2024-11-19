import asyncio
import deps.aiorepl as aiorepl
from time import ticks_ms


class AIO_TASK():
    def __init__(self, update, delta_t):
        self.__update  = update
        self.__delta_t = delta_t

    def task(self):
        first  = ticks_ms()
        start  = first
        remain = 0 
        while True :
            log_msg = self.__update()
            # print(log_msg, ticks_ms() - first)
            
            remain = self.__delta_t - (ticks_ms() - start)
            start += self.__delta_t
            if remain < 0 :
                remain = 0
            await asyncio.sleep_ms(remain)


class AIO_MANAGER():
    def __init__(self):
        self.__task = {}
        self.__task_running = {}
    
    def add(self, name, update, delta_t):
        task = AIO_TASK(update, delta_t)
        self.__task[name] = task

    def run(self, time=0):
        print("aio : running")
        asyncio.run(self.__create_tasks(time))
        print("aio : stopping")
        
    def __create_tasks(self, time):
        self.__task_running = {}
        self.__task_running["repl"] = asyncio.create_task(aiorepl.task())
    
        for key, value in self.__task.items() :
            self.__task_running[key] = asyncio.create_task(value.task())

        if time :
            await asyncio.sleep_ms(time)
        else :
            await asyncio.gather(*tuple(self.__task_running.values()))
            

aio_manager = AIO_MANAGER()
