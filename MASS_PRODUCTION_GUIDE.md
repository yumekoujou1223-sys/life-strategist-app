# 🏭 アプリ量産化ガイド

このガイドでは、Hybrid Life Strategist アプリを雛形として、別の占いアプリを短時間で作成する方法を説明します。

---

## 📊 アーキテクチャの理解

### アプリの構造（3層モデル）

```
┌─────────────────────────────────────┐
│  フロントエンド（UI）               │ ← 見た目を変更
│  - templates/index.html             │
│  - static/css/style.css             │
│  - static/js/app.js                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  バックエンド（API）                │ ← 最小限の変更
│  - app.py                           │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  占いロジック（計算エンジン）        │ ← ここを差し替える
│  - numerology.py                    │
│  - kigaku.py                        │
│  - gemini_api.py                    │
└─────────────────────────────────────┘
```

---

## 🎯 量産のための3ステップ

### ステップ1: 占いロジックの差し替え

#### 例: タロット占いに変更する場合

**1-1. 新しい計算モジュールを作成**

`tarot.py` を作成：

```python
# -*- coding: utf-8 -*-
"""
タロット占い計算エンジン
"""

import random

MAJOR_ARCANA = {
    0: "愚者 (The Fool)",
    1: "魔術師 (The Magician)",
    2: "女教皇 (The High Priestess)",
    # ... 22枚のカード定義
}

def draw_cards(num_cards=3):
    """
    タロットカードを引く
    """
    cards = random.sample(list(MAJOR_ARCANA.keys()), num_cards)
    return {
        'past': MAJOR_ARCANA[cards[0]],
        'present': MAJOR_ARCANA[cards[1]],
        'future': MAJOR_ARCANA[cards[2]]
    }

def get_tarot_profile(seed=None):
    """
    タロットプロファイルを取得
    """
    if seed:
        random.seed(seed)
    
    cards = draw_cards(3)
    return cards
```

**1-2. `app.py` を修正**

```python
# 変更前
from numerology import get_numerology_profile
from kigaku import get_kigaku_profile

# 変更後
from tarot import get_tarot_profile
```

```python
# analyzeエンドポイントを修正
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    name = data.get('name', '')
    question = data.get('question', '')
    
    # タロット占い実行
    tarot_data = get_tarot_profile(seed=name)
    
    # Gemini APIで解釈を取得
    analysis = get_tarot_analysis(name, question, tarot_data, api_key)
    
    result = {
        'name': name,
        'tarot': tarot_data,
        'analysis': analysis
    }
    return jsonify(result)
```

**1-3. プロンプトを修正**

`gemini_api.py` の `create_analysis_prompt` 関数を変更：

```python
def create_tarot_prompt(user_name, question, tarot_data):
    prompt = f"""
あなたはプロのタロットリーダーです。

【ユーザー情報】
名前: {user_name}
質問: {question}

【引かれたカード】
過去: {tarot_data['past']}
現在: {tarot_data['present']}
未来: {tarot_data['future']}

このカードの組み合わせから、{user_name}様への具体的なアドバイスを提供してください。
"""
    return prompt
```

---

### ステップ2: UIの変更

#### テーマカラーの変更

`static/css/style.css` の `:root` セクションを編集：

```css
:root {
    /* タロット用のカラーパレット */
    --primary-color: #7c3aed;      /* 紫 */
    --primary-dark: #5b21b6;
    --primary-light: #a78bfa;
    /* ... */
}
```

#### タイトルとキャッチコピーの変更

`templates/index.html` を編集：

```html
<!-- 変更前 -->
<h1 class="logo">⚡ HYBRID LIFE STRATEGIST</h1>
<p class="tagline">数秘術 × 九星気学で導く、あなただけの人生戦略</p>

<!-- 変更後 -->
<h1 class="logo">🔮 MYSTIC TAROT READER</h1>
<p class="tagline">タロットが示す、あなたの過去・現在・未来</p>
```

#### 入力フォームの変更

```html
<!-- 質問項目を追加 -->
<div class="form-group">
    <label for="question">占いたい質問<span class="required">*</span></label>
    <textarea id="question" name="question" placeholder="例: 今年の仕事運について知りたい" required></textarea>
</div>
```

---

### ステップ3: デプロイ設定の変更

#### プロジェクト名の変更

1. **フォルダ名を変更**: `life-strategist-app` → `tarot-reader-app`
2. **README.mdを更新**: タイトルと説明を変更
3. **GitHubリポジトリ名**: 新しい名前で作成
4. **Renderサービス名**: 新しい名前で作成

---

## 🚀 量産のベストプラクティス

### 1. テンプレートリポジトリの作成

**最初のアプリをテンプレート化**：

1. GitHubで元のリポジトリを開く
2. Settings → Template repository にチェック
3. 2つ目以降は「Use this template」でクローン

### 2. 共通部分のモジュール化

**共通コンポーネントを別ファイルに**：

```
common/
├── ui_components.py    # 共通UI要素
├── api_handler.py      # API共通処理
└── deploy_config.py    # デプロイ設定
```

### 3. 環境変数管理の統一

`.env.example` に必要な変数を明記：

```
# 必須
GEMINI_API_KEY=your_api_key_here

# アプリ固有
APP_NAME=Tarot Reader
APP_THEME_COLOR=#7c3aed
```

---

## 📋 量産チェックリスト

新しいアプリを作る際の確認リスト：

- [ ] 占いロジックモジュールを作成（例: `tarot.py`）
- [ ] `app.py` のインポートとエンドポイントを修正
- [ ] `gemini_api.py` のプロンプトを変更
- [ ] `style.css` のカラーテーマを変更
- [ ] `index.html` のタイトル・説明を変更
- [ ] 入力フォームを占いに合わせて変更
- [ ] `README.md` を更新
- [ ] 新しいGitHubリポジトリを作成
- [ ] Renderで新しいサービスを作成
- [ ] 環境変数を設定
- [ ] デプロイして動作確認

---

## 💡 アプリアイデア例

### 1. 西洋占星術アプリ
- **ロジック**: ホロスコープ計算
- **入力**: 生年月日、出生時刻、出生地
- **出力**: 太陽星座、月星座、アセンダント、ハウス分析

### 2. 四柱推命アプリ
- **ロジック**: 天干地支の計算
- **入力**: 生年月日、出生時刻
- **出力**: 命式、大運、十二運星

### 3. ルーン占いアプリ
- **ロジック**: ルーン文字のランダム抽出
- **入力**: 名前、質問
- **出力**: 3つのルーン文字とその解釈

### 4. 六星占術アプリ
- **ロジック**: 運命星の計算
- **入力**: 生年月日
- **出力**: 運命星、霊合星、年運

### 5. 相性診断アプリ
- **ロジック**: 既存の占いロジック + 2人分の計算
- **入力**: 2人の生年月日と名前
- **出力**: 相性スコア、アドバイス

---

## 🎓 学習リソース

### プログラミング初心者向け

1. **Python基礎**
   - [Progate Python コース](https://prog-8.com/languages/python)
   - [Python公式チュートリアル](https://docs.python.org/ja/3/tutorial/)

2. **Flask入門**
   - [Flask公式ドキュメント](https://flask.palletsprojects.com/)
   - [Real Python Flask Tutorial](https://realpython.com/tutorials/flask/)

3. **Git/GitHub**
   - [GitHub公式ガイド](https://docs.github.com/ja)
   - [サルでもわかるGit入門](https://backlog.com/ja/git-tutorial/)

---

## 🤝 サポート

量産化で困ったことがあれば、以下を確認してください：

1. **エラーログの確認**: Renderの「Logs」タブ
2. **ブラウザコンソール**: F12キーで開発者ツール
3. **Pythonのエラー**: ターミナルのエラーメッセージ

---

**継続的な改善を続けて、素晴らしいアプリを量産しましょう！** 🚀

© 2026 Hybrid Life Strategist - Template Framework
