# ⚡ Hybrid Life Strategist

**数秘術 × 九星気学**で導く、あなただけの人生戦略診断アプリ

## 概要

西洋の論理的体系「数秘術（Numerology）」と東洋の動的環境学「九星気学（Nine Star Ki）」を融合させ、ユーザーの本質的資質、行動戦略、時流とタイミングを分析する戦略診断Webアプリケーションです。

## 主な機能

- 📊 **数秘術プロファイル計算**
  - Life Path Number（ライフパス）
  - Destiny Number（デスティニー）
  - Soul Number（ソウル）
  - Personal Year Number（パーソナルイヤー）

- 🌟 **九星気学分析**
  - 本命星の自動計算
  - 現在の座相（宮）の判定
  - 運気の時流分析

- 🤖 **AI戦略分析**
  - Google Gemini APIによる統合分析
  - 具体的な行動指針の提示
  - 中長期的な展望の策定

- 🎨 **ユーザー体験**
  - ステップバイステップのUI（3画面構成）
  - ビジネス的で論理的なデザイン
  - レスポンシブ対応

## 技術スタック

- **バックエンド**: Python 3.x, Flask
- **フロントエンド**: HTML5, CSS3, JavaScript (Vanilla)
- **AI**: Google Gemini API (gemini-2.0-flash-exp)
- **デプロイ**: Render (推奨)

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone <your-repository-url>
cd life-strategist-app
```

### 2. 仮想環境の作成（推奨）

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

`.env.example`を`.env`にコピーして、APIキーを設定します：

```bash
cp .env.example .env
```

`.env`ファイルを編集：

```
GEMINI_API_KEY=あなたのGemini APIキー
PORT=5000
```

### 5. ローカルでの起動

```bash
python app.py
```

ブラウザで `http://localhost:5000` にアクセス

## Renderへのデプロイ手順

### 1. GitHubリポジトリの作成

1. GitHubで新しいリポジトリを作成
2. ローカルのコードをプッシュ：

```bash
git init
git add .
git commit -m "Initial commit: Hybrid Life Strategist App"
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

### 2. Renderでの設定

1. [Render](https://render.com/)にログイン
2. 「New +」→「Web Service」をクリック
3. GitHubリポジトリを接続
4. 以下の設定を入力：

   - **Name**: `life-strategist-app`（任意）
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

5. **Environment Variables**を追加：
   - Key: `GEMINI_API_KEY`
   - Value: あなたのGemini APIキー

6. 「Create Web Service」をクリック

### 3. デプロイ完了

数分後、アプリが公開されます。RenderのダッシュボードでURLを確認できます。

## プロジェクト構造

```
life-strategist-app/
├── app.py                 # Flaskアプリケーション本体
├── numerology.py          # 数秘術計算エンジン
├── kigaku.py              # 九星気学計算エンジン
├── gemini_api.py          # Gemini API連携モジュール
├── requirements.txt       # Python依存パッケージ
├── Procfile               # Render用起動設定
├── .env.example           # 環境変数のサンプル
├── .gitignore             # Git除外設定
├── README.md              # このファイル
├── templates/
│   └── index.html         # HTMLテンプレート
└── static/
    ├── css/
    │   └── style.css      # スタイルシート
    └── js/
        └── app.js         # フロントエンドロジック
```

## 使い方

1. トップページで名前（ローマ字）と生年月日を入力
2. 「戦略分析を開始」ボタンをクリック
3. 数秒待つと、詳細な戦略分析レポートが表示されます

## 今後の拡張予定

- 🔐 会員登録機能（詳細診断へのアクセス）
- 📅 週間・月間の行動指針
- 💑 相性診断機能
- 📊 過去の診断履歴保存
- 💳 有料プランの追加

## ライセンス

© 2026 Hybrid Life Strategist. All rights reserved.

## 作成者

開発者: ワッシィ
コンセプト: 統計学に基づいた人生行動指針の提供

---

**注意**: このアプリケーションは占いツールですが、統計学的なデータに基づいた分析を提供しています。結果はあくまで参考情報としてご活用ください。
