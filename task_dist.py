import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname='/Users/ludaming/Downloads/msyh.ttf')


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

plt.bar([x[0] for x in sorted_list], [x[1] for x in sorted_list], width=0.4, facecolor='#9999ff', edgecolor='white')
plt.gca().axes.get_xaxis().set_visible(False)

for (x, y) in sorted_list:
    # import pdb;pdb.set_trace()
    plt.text(x, -0.07, '做 %s 次任务' % str(x), ha='center',
             va='bottom', fontproperties=myfont)
    plt.text(x, y + 0.05, '%s' % str(y), ha='center', va='bottom')

plt.ylim(0, 1)

plt.ylabel('概 率', fontproperties=myfont, fontsize=12)
plt.title('阿瓦隆抵抗组织做任务次数的分布', fontproperties=myfont, fontsize=12)
plt.show()


# import pdb;pdb.set_trace()
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

to_plot = []
for (idx, v) in enumerate(switches):
    to_plot.append((idx, v))
    print('The prob of Lancelot switches %d times is %.4f' % (idx, v))

plt.bar([x[0] for x in to_plot], [x[1] for x in to_plot], width=0.4, facecolor='#9999ff', edgecolor='white')
plt.gca().axes.get_xaxis().set_visible(False)

for (x, y) in to_plot:
    # import pdb;pdb.set_trace()
    plt.text(x, -0.07, '兰斯洛特互换%s次' % str(x), ha='center',
             va='bottom', fontproperties=myfont)
    plt.text(x, y + 0.05, '%s' % ('%.2f' % y), ha='center', va='bottom')

plt.ylim(0, 1)

plt.ylabel('概 率', fontproperties=myfont, fontsize=12)
plt.title('兰斯洛特互换次数分布', fontproperties=myfont, fontsize=12)
plt.show()
