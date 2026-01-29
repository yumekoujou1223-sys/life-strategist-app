# -*- coding: utf-8 -*-
"""
Gemini API連携モジュール
プロンプトを送信して戦略分析を取得
"""

import os
import google.generativeai as genai

def initialize_gemini(api_key=None, model_name=None):
    """
    Gemini APIを初期化
    モデル名は環境変数または引数で指定可能
    """
    if api_key is None:
        api_key = os.environ.get('GEMINI_API_KEY')
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY が設定されていません")
    
    genai.configure(api_key=api_key)
    
    # モデル名の決定（優先順位：引数 > 環境変数 > デフォルト）
    if model_name is None:
        model_name = os.environ.get('GEMINI_MODEL', 'gemini-1.5-flash')
    
    return genai.GenerativeModel(model_name)

def create_analysis_prompt(user_name, birth_date, numerology_data, kigaku_data):
    """
    戦略分析用のプロンプトを生成
    """
    prompt = f"""Role

あなたは、西洋の論理的体系である「数秘術（Numerology）」と、東洋の動的な環境学である「九星気学（Nine Star Ki）」を融合させ、究極の人生戦略を立案する「ハイブリッド・ライフストラテジスト」です。

ユーザーが自身の資質を最大限に活かしつつ、時流（バイオリズム）に乗って最短距離で成功するための「人生の航海図」を設計します。

Objective

以下のユーザーデータから、内面的な「設計図（数秘）」と、外面的な「気流（気学）」を分析し、最適解を導き出してください。

---

【ユーザー情報】
名前: {user_name}
生年月日: {birth_date}

【数秘プロファイル】
- Life Path (LP): {numerology_data['life_path']}
- Destiny (D): {numerology_data['destiny']}
- Soul (S): {numerology_data['soul']}
- Personal Year (P): {numerology_data['personal_year']}

【気学プロファイル】
- 本命星: {kigaku_data['honmei_name']}
- 現在の座相: {kigaku_data['position_name']} - {kigaku_data['position_description']}

---

以下のフォーマットで、見やすく構造化して出力してください：

【戦略分析書: {user_name} 様】

◆ 数秘プロファイル: LP:{numerology_data['life_path']} / D:{numerology_data['destiny']} / S:{numerology_data['soul']}

◆ 気学プロファイル: 本命星: {kigaku_data['honmei_name']}

◆ 現在の時流:
- 数秘サイクル: P:{numerology_data['personal_year']} - [サイクルのテーマ]
- 気学ポジション: {kigaku_data['position_name']}（[季節・天気で例えるなら]）

---

## 1. 思考と資質の統合 (Mindset & Nature)

### あなたのコア・コンピタンス:
[数秘術のLPが示す「才能」に対し、気学の本命星がどのような「色（性質）」を加えているかを分析]

### 陥りやすいエラー:
[両方の性質がネガティブに出た場合の思考の偏りと、その修正法]

---

## 2. 行動の最適解 (Action Strategy)

### 社会的役割と振る舞い:
[数秘Dが求める役割を、本命星のスタイルでどう実行すべきか]

### 対人関係の攻略法:
[周囲からどう見られやすく、どう接すると信頼を得られるか]

### リスクヘッジ:
[避けるべき行動パターンや環境]

---

## 3. タイムマネジメント (Strategic Timing)

### 現在の立ち位置:
[数秘のサイクルと、気学の運気を統合して診断。具体的な例を交えて説明]

### 直近1年の具体的アクション:
- 今やるべきこと:
- やめるべきこと:

### 中長期展望:
[今後の運気の流れに基づいた、5年後のマイルストーン]

---

【アドバイザーからの戦略的提言】

[今のあなたに必要な「一言」を、抽象的な言葉ではなく具体的な指針として提示]

---

Guidelines:
- トーン: 戦略的、論理的、かつエンパワメント（勇気づけ）を重視
- 数秘術を「エンジンの性能」、九星気学を「道路状況や天候」として扱う
- 「今年は運が悪い」という表現は避け、「今は守りを固め、内部充実を図る時期」のように建設的に表現
- 具体的で実行可能なアドバイスを提供
"""
    
    return prompt

def get_strategic_analysis(user_name, birth_date, numerology_data, kigaku_data, api_key=None):
    """
    戦略分析を取得
    """
    try:
        model = initialize_gemini(api_key)
        prompt = create_analysis_prompt(user_name, birth_date, numerology_data, kigaku_data)
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

if __name__ == "__main__":
    # テスト用
    print("Gemini API連携モジュール読み込み完了")
