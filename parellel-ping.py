link:http://blog.boa.nu/2012/10/python-threading-example-creating-pingerpy.html
#!/usr/bin/env python

import subprocess
import threading

class Pinger(object):
    status = {'alive': [], 'dead': []} # Populated while we are running
    hosts = [] # List of all hosts/ips in our input queue

    # How many ping process at the time.
    thread_count = 20

    # Lock object to keep track the threads in loops, where it can potentially be race conditions.
    lock = threading.Lock()

    def ping(self, ip):
        # Use the system ping command with count of 1 and wait time of 1.
        ret = subprocess.call(['ping', '-c', '1', '-W', '1', ip],
                              stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))

        return ret == 0 # Return True if our ping command succeeds

    def pop_queue(self):
        ip = None

        self.lock.acquire() # Grab or wait+grab the lock.

        if self.hosts:
            ip = self.hosts.pop()

        self.lock.release() # Release the lock, so another thread could grab it.

        return ip

    def dequeue(self):
        while True:
            ip = self.pop_queue()

            if not ip:
                return None

            result = 'alive' if self.ping(ip) else 'dead'
            self.status[result].append(ip)

    def start(self):
        threads = []

        for i in range(self.thread_count):
            # Create self.thread_count number of threads that together will
            # cooperate removing every ip in the list. Each thread will do the
            # job as fast as it can.
            t = threading.Thread(target=self.dequeue)
            t.start()
            threads.append(t)

        # Wait until all the threads are done. .join() is blocking.
        [ t.join() for t in threads ]

        return self.status

if __name__ == '__main__':
    ping = Pinger()
    ping.thread_count = 8
    ping.hosts = [
        '192.168.28.1', '192.168.28.2', '192.168.28.3', '192.168.28.4', '192.168.28.0', '192.168.28.255', '192.168.28.100',
        'google.com', 'github.com', 'nonexisting', '127.0.1.2', '*not able to ping!*', '8.8.8.8'
        ]

    print ping.start()
