# -*- coding: utf-8 -*-
"""
Flaskアプリケーション本体
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

# 自作モジュールのインポート
from numerology import get_numerology_profile
from kigaku import get_kigaku_profile
from gemini_api import get_strategic_analysis

app = Flask(__name__)

@app.route('/')
def index():
    """
    トップページ（入力フォーム）
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    分析APIエンドポイント
    """
    try:
        # リクエストデータの取得
        data = request.json
        name = data.get('name', '')
        birth_date = data.get('birth_date', '')
        
        # 入力検証
        if not name or not birth_date:
            return jsonify({'error': '名前と生年月日を入力してください'}), 400
        
        # 生年月日をパース
        date_obj = datetime.strptime(birth_date, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        
        # 現在の年
        current_year = datetime.now().year
        
        # 数秘術プロファイルを計算
        numerology_data = get_numerology_profile(year, month, day, name, current_year)
        
        # 九星気学プロファイルを計算
        kigaku_data = get_kigaku_profile(year, month, day, current_year)
        
        # Gemini APIで戦略分析を取得
        api_key = os.environ.get('GEMINI_API_KEY')
        analysis = get_strategic_analysis(
            name, 
            birth_date, 
            numerology_data, 
            kigaku_data,
            api_key
        )
        
        # 結果を返す
        result = {
            'name': name,
            'birth_date': birth_date,
            'numerology': numerology_data,
            'kigaku': kigaku_data,
            'analysis': analysis
        }
        
        return jsonify(result)
    
    except ValueError as e:
        return jsonify({'error': f'日付の形式が正しくありません: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'エラーが発生しました: {str(e)}'}), 500

@app.route('/health')
def health():
    """
    ヘルスチェック用エンドポイント
    """
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # 開発環境用
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
