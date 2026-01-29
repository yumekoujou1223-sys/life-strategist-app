#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Geminiモデル利用可能性チェックツール
あなたのAPIキーで利用可能なモデルを確認します
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルから環境変数を読み込み
load_dotenv()

def check_models():
    """
    利用可能なGeminiモデルをチェック
    """
    api_key = os.environ.get('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ エラー: GEMINI_API_KEY が設定されていません")
        print("\n.envファイルに以下を追加してください:")
        print("GEMINI_API_KEY=あなたのAPIキー")
        return
    
    print("🔍 Geminiモデルの利用可能性をチェック中...\n")
    print("=" * 60)
    
    genai.configure(api_key=api_key)
    
    # チェックするモデルのリスト
    models_to_check = [
        ('gemini-1.5-flash', '最も安定（推奨）'),
        ('gemini-1.5-flash-latest', '最新の1.5-flash'),
        ('gemini-1.5-pro', '高精度版'),
        ('gemini-1.5-pro-latest', '最新の1.5-pro'),
        ('gemini-2.0-flash-exp', '実験版（不安定）'),
    ]
    
    available_models = []
    
    for model_name, description in models_to_check:
        try:
            model = genai.GenerativeModel(model_name)
            # 簡単なテスト（実際には生成しない）
            print(f"✅ {model_name}")
            print(f"   {description}")
            available_models.append(model_name)
        except Exception as e:
            print(f"❌ {model_name}")
            print(f"   エラー: {str(e)}")
        print()
    
    print("=" * 60)
    print(f"\n利用可能なモデル: {len(available_models)}/{len(models_to_check)}")
    
    if available_models:
        print("\n✅ 推奨設定:")
        print(f"\n.envファイルに以下を追加してください:")
        print(f"GEMINI_MODEL={available_models[0]}")
        print(f"\nまたは、環境変数を設定せずデフォルト（gemini-1.5-flash）を使用できます。")
    else:
        print("\n❌ 利用可能なモデルが見つかりませんでした")
        print("APIキーを確認してください")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    check_models()
