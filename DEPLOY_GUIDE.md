# 🚀 Renderへのデプロイ完全ガイド

このガイドでは、Hybrid Life Strategist アプリをRenderで公開する手順を詳しく説明します。

---

## 📋 事前準備

### 必要なもの
1. ✅ GitHubアカウント
2. ✅ Renderアカウント（無料で作成可能）
3. ✅ Google Gemini APIキー

### Gemini APIキーの取得方法

1. [Google AI Studio](https://makersuite.google.com/app/apikey) にアクセス
2. Googleアカウントでログイン
3. 「Create API Key」をクリック
4. 「Create API key in new project」を選択
5. 生成されたAPIキーをコピー（後で使います）

---

## ステップ1: GitHubリポジトリの作成

### 1-1. GitHubで新規リポジトリを作成

1. [GitHub](https://github.com/) にログイン
2. 右上の「+」→「New repository」をクリック
3. 以下を入力：
   - **Repository name**: `life-strategist-app`（任意の名前でOK）
   - **Description**: `数秘術×九星気学による人生戦略診断アプリ`
   - **Public** または **Private**（どちらでもOK）
   - ❌ **Initialize this repository with a README** はチェックしない
4. 「Create repository」をクリック

### 1-2. ローカルからGitHubへアップロード

ダウンロードしたZIPファイルを解凍後、ターミナル（またはコマンドプロンプト）で以下を実行：

```bash
# 解凍したフォルダに移動
cd life-strategist-app

# Gitリポジトリを初期化
git init

# すべてのファイルをステージング
git add .

# 最初のコミット
git commit -m "Initial commit: Hybrid Life Strategist App"

# GitHubリポジトリと接続（URLは自分のリポジトリのものに変更）
git remote add origin https://github.com/あなたのユーザー名/life-strategist-app.git

# メインブランチに変更
git branch -M main

# GitHubにプッシュ
git push -u origin main
```

**※ 初めてGitを使う場合**は、事前に以下を実行：

```bash
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメールアドレス"
```

---

## ステップ2: Renderでのデプロイ

### 2-1. Renderにログイン

1. [Render](https://render.com/) にアクセス
2. 「Get Started」または「Sign Up」をクリック
3. GitHubアカウントで認証（推奨）

### 2-2. 新しいWebサービスを作成

1. ダッシュボードで「New +」をクリック
2. 「Web Service」を選択
3. 「Connect a repository」でGitHubを選択
4. 先ほど作成した`life-strategist-app`リポジトリを選択
5. 「Connect」をクリック

### 2-3. サービス設定

以下の項目を入力：

| 項目 | 設定値 |
|------|--------|
| **Name** | `life-strategist-app`（任意） |
| **Region** | `Singapore (Southeast Asia)` または `Oregon (US West)` |
| **Branch** | `main` |
| **Root Directory** | 空欄のまま |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free`（無料プラン） |

### 2-4. 環境変数の設定

**重要！** APIキーを設定しないとアプリが動きません。

1. 「Advanced」セクションを展開
2. 「Add Environment Variable」をクリック
3. 以下を入力：

   - **Key**: `GEMINI_API_KEY`
   - **Value**: 事前準備で取得したGemini APIキーを貼り付け

4. 「Add Environment Variable」をもう一度クリックして追加（オプション）：

   - **Key**: `PORT`
   - **Value**: `10000`

### 2-5. デプロイを開始

1. すべての設定を確認
2. 「Create Web Service」をクリック
3. デプロイが開始されます（5〜10分程度）

---

## ステップ3: デプロイの確認

### 3-1. ビルドログの確認

- Renderのダッシュボードで「Logs」タブを開く
- `Build successful` と表示されればOK
- エラーが出た場合は、ログを確認してトラブルシューティング

### 3-2. アプリにアクセス

1. デプロイ完了後、Renderが自動でURLを生成
2. URL形式: `https://life-strategist-app-xxxx.onrender.com`
3. URLをクリックしてアプリを開く
4. フォームに名前と生年月日を入力してテスト！

---

## 🎉 完了！

おめでとうございます！アプリが公開されました。

### 公開URLの確認方法

- Renderダッシュボードの上部に表示されているURL
- または「Settings」→「Domains」で確認

### URLを共有する

- このURLを友人やブログで共有できます
- 独自ドメインを設定することも可能（Renderの設定で対応）

---

## 🔧 トラブルシューティング

### ケース1: ビルドに失敗する

**症状**: `Build failed` エラー

**解決方法**:
1. `requirements.txt` が正しくアップロードされているか確認
2. Python バージョンが3.8以上であることを確認
3. Renderの「Environment」で`Python 3`が選択されているか確認

### ケース2: アプリが起動しない

**症状**: `Application error` が表示される

**解決方法**:
1. 環境変数 `GEMINI_API_KEY` が正しく設定されているか確認
2. RenderのLogsで詳細なエラーメッセージを確認
3. `Procfile` の内容が `web: gunicorn app:app` になっているか確認

### ケース3: APIエラーが発生する

**症状**: 分析ボタンを押すとエラーが出る

**解決方法**:
1. Gemini APIキーが有効か確認（Google AI Studioで確認）
2. APIの使用制限に達していないか確認
3. ブラウザのコンソール（F12）でエラーメッセージを確認

---

## 📚 参考情報

### Renderの無料プランの制限

- ✅ 月750時間の稼働時間（1つのアプリなら十分）
- ✅ 512MBメモリ
- ✅ カスタムドメイン対応
- ⚠️ 15分間アクセスがないとスリープ（次回アクセス時に起動）

### アプリの更新方法

コードを修正した後：

```bash
git add .
git commit -m "更新内容の説明"
git push origin main
```

GitHubにプッシュすると、Renderが自動で再デプロイします！

---

## 💡 次のステップ

1. **カスタムドメインの設定**
   - お名前.comやGoogle Domainsで独自ドメインを取得
   - RenderのSettings → Domains で設定

2. **アクセス解析の追加**
   - Google Analyticsのコードを`index.html`に追加

3. **会員登録機能の開発**
   - データベース（PostgreSQL）の追加
   - 認証システムの実装

---

**質問があれば、いつでもサポートします！**

© 2026 Hybrid Life Strategist
