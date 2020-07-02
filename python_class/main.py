import package.list_ops as lo
import package.dict_ops as do
import numeric.prime_number as pn

num = [341, 12, 523, 59, 1, 2, 3, 4]
num_bool = []
for n in num:
    num_bool.append((pn.check_prime_number(n)))
print(num_bool)

# weights = [65, 90, 42, 76]
# heights = [1.65, 1.78, 1.59, 1.80]
# heights_sq = lo.multiply(heights, heights)
# BMI = lo.divide(weights, heights_sq)
# print("BMI:", BMI)
#
# w_names = ["RM", "Suga", "Jin", "V"]
# h_names = ["Jimin", "RM", "Suga", "Jin"]
# weights = dict(zip(w_names, weights))
# heights = dict(zip(h_names, heights))
# print("weights:", weights)
# print("heights:", heights)
#
# heights_sq = do.multiply(heights, heights)
# BMI = do.divide(weights, heights_sq)
# print(f"height^2: {heights_sq} \nBMI: {BMI}")





