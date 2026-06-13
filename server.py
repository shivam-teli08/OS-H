from app import app,db
from redisConnection import redisConnection
redisConnection()

with app.app_context():
    db.create_all()
print("Tables created successfully")

if __name__ == '__main__':
    app.run(debug=True) 
    # server running in debug mode for development purposes. In production, set debug to False.
