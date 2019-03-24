import random

NUM_EPOCH = 10
# NUM_EPOCH = 100
NUM_TESTS = 10000

# failure 0; success 1

def play_a_game():
    choices = [0, 1]
    num_failure = 0
    num_success = 0
    tasks_played = 0
    for i in range(0, 5):  # 5 tasks
        result = random.choice(choices)
        tasks_played += 1
        if result == 0:
            num_failure += 1
            if num_failure == 3:
                return tasks_played
        elif result == 1:
            num_success += 1
            if num_success == 3:
                return tasks_played
        else:
            print("What ???")
    print('OMG')

task_num_dist = {}
total_games_played = 0
for epoch in range(0, NUM_EPOCH):
    for i in range(0, NUM_TESTS):
        tasks_played = play_a_game()
        total_games_played += 1
        if tasks_played not in task_num_dist:
            task_num_dist[tasks_played] = 0
        task_num_dist[tasks_played] += 1

# print('AVG NUM_FAILURE : %.2f; AVG NUM_SUCCESS : %.2f' % (NUM_FAILURE/NUM_EPOCH, NUM_SUCCESS/NUM_EPOCH))
sorted_list = []
for k, v in task_num_dist.items():
    sorted_list.append((k, v/total_games_played))
    sorted_list = sorted(sorted_list, key=lambda x: x[0])

for t in sorted_list:
    print('Tasks of %d has %.4f probability' % (t[0], t[1]))
