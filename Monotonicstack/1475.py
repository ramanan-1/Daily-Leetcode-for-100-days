def finalPrices(prices):
    
        discount = 0
        stack = []
        result = [0] * len(prices)

        for idx in range(len(prices)-1,-1,-1) :
            price = prices[idx]
            
            while stack and stack[-1] > price :
                stack.pop()

            if stack :
                discount = price - stack[-1]
                result[idx] = discount
            else:
                result[idx] = price
            stack.append(price)
        return result 
