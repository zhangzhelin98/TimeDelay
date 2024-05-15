import random
import matplotlib.pyplot as plt

# 効用関数
def risk_aversion(x, alpha):
    return x**alpha / (1 - alpha)


def simulate_lottery(num_simulations, alpha):
    profits = []
    bids = []  # 投資者の最大購入希望価格
    lottery_returns = []  # くじの払戻金額
    total_profit = 0
    for _ in range(num_simulations):
        # くじの払戻金額と確率
        profit_options = [1000, 800, 600, 400, 200, -10000]
        profit_probabilities = [0.199, 0.199, 0.199, 0.199, 0.199, 0.005]

        # コンピューターが選択した整数
        random_number = random.randint(0, 1000)

        # くじの払戻金額
        outcome = random.choices(profit_options, weights=profit_probabilities)[0]
        lottery_returns.append(outcome)  # くじの払戻金額を記録する

        # くじを購入できるかどうかを決定されます
        # 利得を計算します
        if investor_bid >= random_number:
            profit = outcome - random_number
        else:
            profit = 0
        total_profit += profit    

        profits.append(total_profit)

    return profits, bids, lottery_returns

num_simulations = 200  # シミュレーションの回数
alpha = 0.9  

profits, bids, lottery_returns = simulate_lottery(num_simulations, alpha)


# 最後の回の利得をプリントする
final_profit = profits[-1]
print(f"Final profit from the last simulation with risk preference alpha {alpha}: {final_profit} points")

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
plt.plot(range(1, num_simulations + 1), bids)
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
        for _ in range(num_simulations):
            # 彩票的收益选项和对应的概率
            profit_options = [1000, 800, 600, 400, 200, -10000]
            profit_probabilities = [0.199, 0.199, 0.199, 0.199, 0.199, 0.005]

            # 随机生成电脑的随机数字
            random_number = random.randint(0, 1000)

            # 计算投资者的风险规避程度
            risk_score = risk_aversion(random_number, alpha)

            # 映射风险规避程度到0-523范围内
            investor_bid = 400
            bids.append(investor_bid)  # 记录投资者出价

            # 随机生成彩票的收益（与是否购入无关的）
            outcome = random.choices(profit_options, weights=profit_probabilities)[0]
            lottery_returns.append(outcome)  # 记录彩票回报

            # 判断是否购买彩票并计算收益
            if investor_bid >= random_number:
                # 计算投资者的收益
                if outcome == -10000:
                    profit = -10000 - random_number  # 收益为-10000时，减去电脑给出的随机数字
                else:
                    profit = outcome - random_number
                total_profit += profit

            profits.append(total_profit)

        # 绘制总收益折线图
        plt.subplot(2, 1, 1)
        plt.plot(range(1, num_simulations + 1), profits, color=colors[repeat])


        # 绘制彩票回报折线图
        plt.subplot(2, 1, 2)
        plt.plot(range(1, num_simulations + 1), lottery_returns, color=colors[repeat])

    plt.xlabel('Simulation Number')
    plt.grid(True)


num_simulations = 200  # 设置每次模拟的次数
num_repeats = 10  # 设置重复模拟的次数
alpha = 0.9  # 设置风险偏好参数

simulate_lottery(num_simulations, num_repeats, alpha)



