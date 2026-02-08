class animal:
    def __init__(self, name):
        self.name= name
        print(self.name, 'was adopted')

    def run(self):
        print('running')

class turtle(animal):
    def run(self):
        print('run slowly')

tim= turtle('tim')
tim.run()
