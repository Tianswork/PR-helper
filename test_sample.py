import sys
import os

print("這是測試檔案")

def bad_function( a,b,c ):
    result=a+b*c
    print(f"計算結果: {result}")
    return result

class TestClass:
    def __init__(self,name):
        self.name=name
        print(f"建立了 {name}")
    
    def process(self,data):
        for item in data:
            print(item)
        return len(data)