import random

def run():
     doors = []
     for i in range(1,50):
         randdoor = random.randrange(1,50)
         while randdoor in doors:
                 randdoor = random.randrange(1,50)
         doors.append(randdoor)
     print(doors)
