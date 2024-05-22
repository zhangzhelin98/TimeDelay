import random
import matplotlib.pyplot as plt
import numpy as np

# 乱数のシード
random.seed(1111)
# 効用関数
def risk_aversion(x, alpha):
    try:
        assert alpha != 1
    except AssertionError:
        print("alpha should be < 1")
        return None

    if x >= 0:
        return x**(1-alpha) 
    else:
        return -((-x) ** (1-alpha))   # 損失回避ならalphaの値を変える
    
# risk_aversion の逆関数: 効用水準 u における certainty equivalent
def inverse_risk_aversion(u, alpha):
    if u >= 0:
        return ((1 - 0) * u) ** (1 / (1-alpha))
    else:
        return -(((1 - 0) * (-u)) ** (1 / (1-alpha)))    


def simulate_lottery(num_simulations, alpha, initial_endowment=20000):
    # くじの払戻金額とその確率
    profit_options = [1000, 800, 600, 400, 200, -10000]  # 払戻金額のオプション
    # profit_options = [500, 400, 300, 200, 100, -10000]  # 払戻金額のオプション
    profit_probabilities = [
        0.199,
        0.199,
        0.199,
        0.199,
        0.199,
        0.005,
    ]  # 各払戻金額の確率

    profits = []  # 各シミュレーションの利益を格納するリスト
    lottery_returns = []  # 各シミュレーションのくじの払戻金額を格納するリスト
    experience = []
    total_tail = 0

    for _ in range(num_simulations):  # 指定された回数だけシミュレーションを繰り返す
        investor_bid = (
            inverse_risk_aversion(
                sum(
                    [
                        risk_aversion(initial_endowment + x[0], alpha) * x[1]
                        for x in zip(profit_options, profit_probabilities)
                    ]
                ),
                alpha,
            )
            - initial_endowment
        )
        # print ("bid={}".format(investor_bid))

        # ランダムな整数を生成
        random_number = random.randint(0, 1000)  # 0から1000までのランダムな整数

        # くじの払戻金額を決定
        outcome = random.choices(profit_options, weights=profit_probabilities)[0]
        lottery_returns.append(outcome)  # くじの払戻金額を記録

        if outcome == -10000 and investor_bid >= random_number:
            tail = 1
        else:
            tail = 0
        total_tail += tail
        experience.append(total_tail)
        final_experience = experience [-1]
        # print("experience={}".format(final_experience))

        # くじを購入できるかどうかを決定し、利益を計算
        if investor_bid >= random_number:  # 入札額がランダムな数値以上であれば
            profit = outcome - random_number
        else:
            profit = 0

        profits.append(profit)  # 利益をリストに追加

    return profits, lottery_returns, investor_bid  # 利益、くじの払戻金額のリストを返す

num_simulations = 20000  # シミュレーションの回数





for v in [0,0.5, 0.75, 0.9, 0.95, 0.99,1.3,1.37]:
    alpha = v
    profits, lottery_returns, investor_bid = simulate_lottery(num_simulations, alpha)
    
    print(
        "alpha: {}: くじ1回あたりの平均利益 {} (SD = {}),bid:{}".format(
            alpha, np.mean(profits), np.std(profits), investor_bid, 
        )
    )



# # 最後の回の利得をプリントする
# final_profit = profits[-1]
# print(f"Final profit from the last simulation with risk preference alpha {alpha}: {final_profit} points")

# 利得の図
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_simulations + 1), profits)
plt.xlabel('Simulation Number')
plt.ylabel('Cumulative Profit')
plt.title('Investor Profit Over Simulations')
plt.grid(True)
plt.show()

# 投資価格の図
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_simulations + 1), investor_bid)
plt.xlabel('Simulation Number')
plt.ylabel('Investor Bid')
plt.title('Investor Bid Over Simulations')
plt.grid(True)
plt.show()

# くじの払戻金額の図
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_simulations + 1), lottery_returns)
plt.xlabel('Simulation Number')
plt.ylabel('Lottery Return')
plt.title('Lottery Return Over Simulations')
plt.grid(True)
plt.show()




import random
import matplotlib.pyplot as plt

def risk_aversion(x, alpha):
    return x**alpha / (1 - alpha)


def simulate_lottery(num_simulations, num_repeats, alpha):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple', 'orange', 'pink']  # 手动指定颜色
    plt.figure(figsize=(30, 30))

    for repeat in range(num_repeats):
        profits = []
        bids = []  # 记录每次模拟中的投资者出价
        lottery_returns = []  # 记录每次模拟中的彩票回报（与是否购入无关）
        total_profit = 0
        experience = []
        total_tail = 0
        for _ in range(num_simulations):
            # 彩票的收益选项和对应的概率
            profit_options = [1000, 800, 600, 400, 200, -10000]
            profit_probabilities = [0.199, 0.199, 0.199, 0.199, 0.199, 0.005]

            # 随机生成电脑的随机数字
            random_number = random.randint(0, 1000)



            # 映射风险规避程度到0-523范围内
            investor_bid = 547
            bids.append(investor_bid)  # 记录投资者出价

            # 随机生成彩票的收益（与是否购入无关的）
            outcome = random.choices(profit_options, weights=profit_probabilities)[0]
            lottery_returns.append(outcome)  # 记录彩票回报
            if outcome == -10000 and investor_bid >= random_number:
                tail = 1
            else:
                tail = 0
            total_tail += tail
            experience.append(total_tail)
            final_experience = experience [-1]
            print("experience={}".format(final_experience))
            
    
            

            # 判断是否购买彩票并计算收益
            if investor_bid >= random_number:
                # 计算投资者的收益
                if outcome == -10000:
                    profit = -10000 - random_number  # 收益为-10000时，减去电脑给出的随机数字
                else:
                    profit = outcome - random_number
                total_profit += profit

            profits.append(total_profit)
  
        # # 绘制总收益折线图
        # plt.subplot(2, 1, 1)
        # plt.plot(range(1, num_simulations + 1), profits, color=colors[repeat])


        # 绘制彩票回报折线图
        # plt.subplot(2, 1, 2)
    plt.plot(range(1, num_simulations + 1), lottery_returns, color=colors[repeat])

    plt.xlabel('Simulation Number')
    plt.grid(True)


num_simulations = 200  # 设置每次模拟的次数
num_repeats = 10  # 设置重复模拟的次数


simulate_lottery(num_simulations, num_repeats, alpha)
print("experiment_mean={}".format(np.mean(final_experience)))






import random
import matplotlib.pyplot as plt
import numpy as np

def risk_aversion(x, alpha):
    return x**alpha / (1 - alpha)

def simulate_lottery(num_simulations, num_repeats, alpha):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple', 'orange', 'pink']  # 手动指定颜色
    plt.figure(figsize=(30, 30))

    all_final_experiences = []

    for repeat in range(num_repeats):
        profits = []
        bids = []  # 记录每次模拟中的投资者出价
        lottery_returns = []  # 记录每次模拟中的彩票回报（与是否购入无关）
        total_profit = 0
        experience = []
        total_tail = 0
        for _ in range(num_simulations):
            # 彩票的收益选项和对应的概率
            profit_options = [1000, 800, 600, 400, 200, -10000]
            profit_probabilities = [0.199, 0.199, 0.199, 0.199, 0.199, 0.005]

            # 随机生成电脑的随机数字
            random_number = random.randint(0, 1000)

            # 映射风险规避程度到0-523范围内
            investor_bid = 512
            bids.append(investor_bid)  # 记录投资者出价

            # 随机生成彩票的收益（与是否购入无关的）
            outcome = random.choices(profit_options, weights=profit_probabilities)[0]
            lottery_returns.append(outcome)  # 记录彩票回报
            if outcome == -10000 and investor_bid >= random_number:
                tail = 1
            else:
                tail = 0
            total_tail += tail
            experience.append(total_tail)

            # 判断是否购买彩票并计算收益
            if investor_bid >= random_number:
                # 计算投资者的收益
                if outcome == -10000:
                    profit = -10000 - random_number  # 收益为-10000时，减去电脑给出的随机数字
                else:
                    profit = outcome - random_number
                total_profit += profit

            profits.append(total_profit)

        final_experience = experience[-1]
        all_final_experiences.append(final_experience)
        print("Repeat {}: final_experience={}".format(repeat + 1, final_experience))

        # 绘制彩票回报折线图
        plt.plot(range(1, num_simulations + 1), lottery_returns)

    plt.xlabel('Simulation Number')
    plt.grid(True)
    plt.show()

    return all_final_experiences

num_simulations = 200  # 设置每次模拟的次数
num_repeats = 100  # 设置重复模拟的次数
alpha = 0.5  # 示例alpha值

all_final_experiences = simulate_lottery(num_simulations, num_repeats, alpha)
print("Mean of final_experiences={}".format(np.mean(all_final_experiences)))
