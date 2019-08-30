class Queue:

    def __init__(self):
        queue = []

    def get_in_line(self, name):
        self.queue.append(name)

    def get_out_of_line(self):
        self.queue.pop(0)
