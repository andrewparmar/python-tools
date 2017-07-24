import random
from pythonds.basic.queue import Queue

counter = 0

class Printer:

	def __init__(self, ppm):
		self.pagerate = ppm
		self.current_task = None
		self.time_remaining = 0

	# internal countdown timer
	def tick(self):
		if self.current_task != None:
			self.time_remaining = self.time_remaining -1
			if self.time_remaining <= 0:
				self.current_task = None

	# is printer busy
	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	# start next task
	def startNext(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.getPages() * 60/self.pagerate


class Task:

	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1,20)

	def gerStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self,current_time):
		return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):

	labprinter = Printer(pages_per_minute)
	print_queue = Queue()
	waiting_times = []

	for current_second in range(num_seconds):

		# check if new task is generated
		if new_print_task():
			task = Task(current_second)
			print_queue.enqueue(task)

		# feed queue to printer
		if (not labprinter.busy()) and (not print_queue.isEmpty()):
			nexttask = print_queue.dequeue()
			labprinter.startNext(nexttask)
			waiting_times.append(nexttask.waitTime(current_second)+labprinter.time_remaining)
			# waiting_times.append(nexttask.waitTime(current_second))

		labprinter.tick()

	average_wait = sum(waiting_times)/len(waiting_times)
	print("The average wait time is %.2f and tasks pending is %i" % (average_wait,print_queue.size()	)	)


def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        # global counter
        # counter = counter +1
        # print(counter)
        return True
    else:
        return False

for i in range(0,10):
	simulation(3600,10)