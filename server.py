from app import app
from dotenv import load_dotenv
from redisConnection import redisConnection
load_dotenv()
redisConnection()
if __name__ == '__main__':
    app.run(debug=True) 
    # server running in debug mode for development purposes. In production, set debug to False.