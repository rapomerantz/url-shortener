import redis

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

try:
    redis_client.ping()
    print("connected to redis")
except redis.ConnectionError:
    print("redis not connected")