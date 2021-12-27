from locust import HttpUser, task, constant_throughput

class TestUser(HttpUser):

    host='https://yopass.dermai.com.tw'
    
    wait_time = constant_throughput(20)
    @task
    def yopass(self):
        self.client.post('/secret', json={"expiration":3600,"message":"-----BEGIN PGP MESSAGE-----\n\nwy4ECQMIB760ELUSLdDgOQUzWmn740+mPNwaSBhfL8Pv8CNpM8IsJUrGy5HI\naWWs0jMBhHNDbK29y7tJV127JeGT+S0VR0l37ltGsmfLT/foixh69M9eltia\nIm5Zj7jZrdegR9Y=\n=cmK3\n-----END PGP MESSAGE-----\n","one_time":True})



