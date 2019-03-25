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

lancelot_cards = [1,1,0,0,0,0,0]
def lancelot_switches(tasks_played):
    chosen_lancelot_cards = random.sample(lancelot_cards, k=tasks_played)
    times = sum(chosen_lancelot_cards)
    return times

task_num_dist = {}
total_games_played = 0

lancelot_dist = {}
for epoch in range(0, NUM_EPOCH):
    for i in range(0, NUM_TESTS):
        tasks_played = play_a_game()
        total_games_played += 1
        if tasks_played not in task_num_dist:
            task_num_dist[tasks_played] = 0
        task_num_dist[tasks_played] += 1
        num_of_lancelot_switches = lancelot_switches(tasks_played)

        if tasks_played not in lancelot_dist:
            lancelot_dist[tasks_played] = {}

        if num_of_lancelot_switches not in lancelot_dist[tasks_played]:
            lancelot_dist[tasks_played][num_of_lancelot_switches] = 0
        lancelot_dist[tasks_played][num_of_lancelot_switches] += 1

# print('AVG NUM_FAILURE : %.2f; AVG NUM_SUCCESS : %.2f' % (NUM_FAILURE/NUM_EPOCH, NUM_SUCCESS/NUM_EPOCH))
sorted_list = []
for k, v in task_num_dist.items():
    sorted_list.append((k, v/total_games_played))
    sorted_list = sorted(sorted_list, key=lambda x: x[0])

for t in sorted_list:
    print('Tasks of %d has %.4f probability' % (t[0], t[1]))


# print(lancelot_dist)
print('\nlancelot switches disttribution:\n')
for i in range(3,6):
    game_sum = 0
    for j in range(0, 3):
        game_sum += lancelot_dist[i][j]

    for j in range(0, 3):
        lancelot_dist[i][j] /= game_sum
        print('Play %d rounds, Lancelot switches %d, prob is %f' %
                (i, j, lancelot_dist[i][j]))
    print()

print('\nOverall Lancelot # of switch probability:\n')
switches = [0,0,0]

for t in sorted_list:
    tasks = t[0]
    prob = t[1]
    for j in range(0, 3):
        switches[j] += lancelot_dist[tasks][j] * prob

for (idx, v) in enumerate(switches):
    print('The prob of Lancelot switches %d times is %.4f' % (idx, v))
