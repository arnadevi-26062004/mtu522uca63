#3.1 write a function called linear_search_product that takes the lot of product and the target product name as input the function should perform a linear search to find the target product in the list and return a list of integers of all occurrences of product is found ,or an empty list if the product is not foundDef linearSearchProduct (productList, targetProduct):
def linearSearchProduct (productList, targetProduct):
  indices = []

  for index, product in enumerate(productList): 
    if product == targetProduct:
     indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal","shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
