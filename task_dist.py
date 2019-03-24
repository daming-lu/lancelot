import random

NUM_EPOCH = 100
NUM_TESTS = 10000

# failure 0; success 1

NUM_FAILURE = 0
NUM_SUCCESS = 0

choices = [0, 1]
for epoch in range(0, NUM_EPOCH):
    for i in range(0, NUM_TESTS):
        result = random.choice(choices)
        if result == 0:
            NUM_FAILURE += 1
        elif result == 1:
            NUM_SUCCESS += 1
        else:
            print("What ???")

print('AVG NUM_FAILURE : %.2f; AVG NUM_SUCCESS : %.2f' % (NUM_FAILURE/NUM_EPOCH, NUM_SUCCESS/NUM_EPOCH))
