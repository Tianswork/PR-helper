#!/usr/bin/env python3
"""
Test script for auto_mod_tool.py
測試自動修改工具的功能
"""
import os
import tempfile
import json
from auto_mod_tool import get_ai_fix_file_content

def test_get_ai_fix_file_content():
    """測試 AI 修改檔案內容的功能"""
    
    # 模擬一個有問題的 Python 檔案
    test_file_content = '''import sys
print("這是 debug 訊息")
def test_function( a,b ):
    result=a+b
    print(f"結果是: {result}")
    return result
'''
    
    # 模擬 PR 評論
    test_comment = [
        {
            "body": "請移除 print() 語句，並修正格式問題：函數參數間距、運算子空格等",
            "created_at": "2025-01-30T12:00:00Z",
            "user": {"login": "reviewer"}
        }
    ]
    
    print("🧪 測試開始...")
    print("原始檔案內容:")
    print("=" * 50)
    print(test_file_content)
    print("=" * 50)
    print(f"PR 評論: {test_comment[0]['body']}")
    print("=" * 50)
    
    try:
        # 呼叫修改函數
        modified_content = get_ai_fix_file_content(test_comment, test_file_content)
        
        print("修改後的檔案內容:")
        print("=" * 50)
        print(modified_content)
        print("=" * 50)
        
        # 簡單檢查
        if "print(" not in modified_content:
            print("✅ 成功移除 print() 語句")
        else:
            print("❌ 仍然包含 print() 語句")
            
        if "def test_function(a, b):" in modified_content:
            print("✅ 函數參數格式修正成功")
        else:
            print("❌ 函數參數格式未修正")
            
        if "result = a + b" in modified_content:
            print("✅ 運算子空格修正成功")
        else:
            print("❌ 運算子空格未修正")
            
    except Exception as e:
        print(f"❌ 測試失敗: {e}")

def test_prompt_loading():
    """測試 prompt.md 檔案讀取"""
    print("\n📄 測試 prompt.md 讀取...")
    
    prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.md')
    if os.path.exists(prompt_path):
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✅ prompt.md 讀取成功，檔案長度: {len(content)} 字元")
        print(f"📋 包含規範: {'Copyright' in content}")
    else:
        print("❌ prompt.md 檔案不存在")

if __name__ == "__main__":
    # 檢查環境變數
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  請設定 OPENAI_API_KEY 環境變數")
        print("export OPENAI_API_KEY='your_api_key'")
        exit(1)
    
    if not os.getenv("OPENAI_ENDPOINT_URL"):
        print("⚠️  請設定 OPENAI_ENDPOINT_URL 環境變數")
        print("export OPENAI_ENDPOINT_URL='https://api.openai.com/v1'")
        exit(1)
    
    print("🚀 開始測試 Auto Mod Tool...")
    test_prompt_loading()
    test_get_ai_fix_file_content()
    print("\n✨ 測試完成！")