# 第一個程式。
# 變數 = 一個有名字嘅值。函數 = 一段可以重複用嘅步驟。

name = "CS 潘"


def greet(who):
    """用個名組一句問候。"""
    return f"你好，{who}！呢個係你嘅第一個程式。"


def add(a, b):
    """將兩個數加埋。"""
    return a + b


if __name__ == "__main__":
    print(greet(name))
    print("1 + 2 =", add(1, 2))
