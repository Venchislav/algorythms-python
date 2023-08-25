def productExceptSelf(nums):
    n = len(nums)
    l_product = [1] * n
    r_product = [1] * n

    for i in range(1, n):
        l_product[i] = l_product[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        r_product[i] = r_product[i + 1] * nums[i + 1]

    return [r_product[i] * l_product[i] for i in range(n)]


# GPT объяснялкин
"""

n = len(nums)
l_product = [1] * n
r_product = [1] * n

for i in range(1, n):
    l_product[i] = l_product[i - 1] * nums[i - 1]

for i in range(n - 2, -1, -1):
    r_product[i] = r_product[i + 1] * nums[i + 1]

return [r_product[i] * l_product[i] for i in range(n)]


Этот код решает задачу, где требуется создать новый список, содержащий произведение всех элементов списка nums, исключая текущий элемент. Он использует два дополнительных списка (l_product и r_product) для хранения произведений элементов слева и справа от каждого элемента из nums.

Разберемся, как работает этот код:

- n = len(nums): Мы определяем переменную n и присваиваем ей длину списка nums.

- l_product = [1] * n и r_product = [1] * n: Мы создаем два новых списка, l_product и r_product, каждый из которых содержит n элементов, и каждый элемент инициализируется значением 1. Эти списки будут использоваться для хранения произведений элементов слева и справа от каждого элемента в nums. На этом этапе они содержат единицы, потому что пока мы не учитываем ни слева, ни справа ни одного элемента.

- Начало вычисления произведения слева (l_product):
  - for i in range(1, n): Мы проходим по индексам i от 1 до n-1.
  - l_product[i] = l_product[i - 1] * nums[i - 1]: Мы устанавливаем l_product[i] равным произведению предыдущего элемента (левого) l_product[i - 1] и соответствующего элемента из nums. Таким образом, l_product[i] будет содержать произведение всех элементов слева от nums[i].

- Начало вычисления произведения справа (r_product):
  - for i in range(n - 2, -1, -1): Мы проходим по индексам i в обратном порядке от n-2 до 0.
  - r_product[i] = r_product[i + 1] * nums[i + 1]: Мы устанавливаем r_product[i] равным произведению следующего элемента (правого) r_product[i + 1] и соответствующего элемента из nums. Таким образом, r_product[i] будет содержать произведение всех элементов справа от nums[i].

- return [r_product[i] * l_product[i] for i in range(n)]: Возвращается новый список, в котором каждый элемент равен произведению соответствующих элементов из r_product и l_product для каждого индекса i.

Итак, функция создает два дополнительных списка - l_product и r_product, которые хранят произведения элементов слева и справа от каждого элемента в nums. Затем она возвращает новый список, содержащий произведения r_product[i] * l_product[i] для каждого индекса i.

"""