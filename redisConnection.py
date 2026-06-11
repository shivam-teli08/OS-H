import redis

def redisConnection():    
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    return r