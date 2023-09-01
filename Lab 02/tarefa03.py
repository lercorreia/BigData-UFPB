import redis

r = redis.Redis(
  host='redis-11614.c308.sa-east-1-1.ec2.cloud.redislabs.com',
  port=11614,
  password='kpTCvmSuK4TjXT3wf2CU384PMElVFpOA')



r.set('hello', 'world')
print(r.get('hello'))