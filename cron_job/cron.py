from apschedular.schedulars.background import BackgroundSchedular


schedular=BackgroundSchedular()

def start_schedular():
    schedular.add_job(
        func=,
        trigger=,
        id=,
        replace_existing=True
    )
    schedular.start()

def stop_schedular():
    schedular.shutdown()
    