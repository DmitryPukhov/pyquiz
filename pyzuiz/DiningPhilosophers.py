import threading
import time


class DiningPhilosophers:
    """
    Dining Philosophers: In the famous dining philosophers problem, a bunch of philosophers are
    sitting around a circular table with one chopstick between each of them. A philosopher needs
    both chopsticks to eat, and always picks up the left chopstick before the right one. A deadlock
    could potentially occur if all the philosophers reached for the left chopstick at the same time. Using
    threads and locks, implement a simulation of the dining philosophers problem that prevents dead­
    locks.
    """

    def __init__(self, num):
        """
        :param num: count of people at the table
        """
        self.people_cnt = num
        self.sticks: [threading.Lock] = []
        for i in range(0, num):
            self.sticks.append(threading.Lock())

    class Philosopher:

        def __init__(self, num, sticks: [threading.Lock]):
            """
            :param num: number of this guy at the table
            """
            # Number of current philosopher
            self.num = num
            # Memorize left and right stick for this philosopher
            self.left_stick: threading.Lock = sticks[self.num % len(sticks)]
            self.right_stick: threading.Lock = sticks[(self.num + 1) % len(sticks)]

        def __call__(self, *args, **kwargs):
            print('Phil%s\n' % self.num)
            for i in range(0, 100000):
                self.eat_step()

        def eat_step(self):
            print('Eating%s\n' % self.num)
            self.left_stick.acquire(blocking=True)
            self.right_stick.acquire(blocking=True)
            time.sleep(5)

            self.left_stick.release()
            self.right_stick.release()
            print('Have eat%s\n' % self.num)

    def run(self):
        # Create threading philosophers
        people = []
        for i in range(0, self.people_cnt):
            thread = threading.Thread(target=self.Philosopher(i, self.sticks))
            people.append(thread)
            thread.start()

        # Wait
        for thread in people:
            if thread.is_alive():
                thread.join(60)

# Run the code to reproduce dead locks
DiningPhilosophers(5).run()
