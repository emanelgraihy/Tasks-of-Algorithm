def max_profit_linear(prices: list[int]):
    if not prices or len(prices) < 2:
        return 0, None, None

    min_price = prices[0]
    min_day = 0
    best_profit = 0
    buy_day = None
    sell_day = None

    for day in range(1, len(prices)):
        profit = prices[day] - min_price
        if profit > best_profit:
            best_profit = profit
            buy_day = min_day
            sell_day = day
        if prices[day] < min_price:
            min_price = prices[day]
            min_day = day

    return best_profit, buy_day, sell_day


def max_profit_dc(prices: list[int], left: int, right: int):
    if left >= right:
        return 0, None, None

    mid = (left + right) // 2

    left_profit, l_buy, l_sell = max_profit_dc(prices, left, mid)
    right_profit, r_buy, r_sell = max_profit_dc(prices, mid + 1, right)

    min_left_price = prices[left]
    min_left_idx = left
    for i in range(left, mid + 1):
        if prices[i] < min_left_price:
            min_left_price = prices[i]
            min_left_idx = i

    max_right_price = prices[mid + 1]
    max_right_idx = mid + 1
    for j in range(mid + 1, right + 1):
        if prices[j] > max_right_price:
            max_right_price = prices[j]
            max_right_idx = j

    cross_profit = max_right_price - min_left_price

    if cross_profit >= left_profit and cross_profit >= right_profit:
        return cross_profit, min_left_idx, max_right_idx
    if left_profit >= right_profit:
        return left_profit, l_buy, l_sell
    return right_profit, r_buy, r_sell


if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]

    dc_profit, dc_buy, dc_sell = max_profit_dc(prices, 0, len(prices) - 1)
    lin_profit, lin_buy, lin_sell = max_profit_linear(prices)

    print(f"[Divide & Conquer] Buy Day {dc_buy} -> Sell Day {dc_sell} | Max Profit: {dc_profit}")
    print(f"[Linear Scan] Buy Day {lin_buy} -> Sell Day {lin_sell} | Max Profit: {lin_profit}")