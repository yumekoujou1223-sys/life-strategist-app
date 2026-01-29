# Geminiモデル利用可能性チェックツール

このツールは、あなたのAPIキーでどのGeminiモデルが利用可能かを確認します。

## 使い方

```bash
python check_gemini_models.py
```

## 利用可能なモデル一覧（2026年1月時点）

### 推奨モデル

1. **gemini-1.5-flash** ✅ 最も安定（デフォルト）
   - 速度: 高速
   - 精度: 良好
   - 安定性: 高い
   - コスト: 低い

2. **gemini-1.5-flash-latest**
   - 最新の1.5-flashバージョン
   - 定期的に更新される

3. **gemini-1.5-pro**
   - 速度: 中速
   - 精度: 最高
   - 安定性: 高い
   - コスト: 中程度

4. **gemini-1.5-pro-latest**
   - 最新の1.5-proバージョン

### 実験版モデル

5. **gemini-2.0-flash-exp**
   - Gemini 2.0の実験版
   - 利用可能な場合もあるが、不安定
   - 予告なく変更・削除される可能性

## エラーが出た場合の対処法

### エラー: "models/gemini-X.X-XXX is not found"

**原因**: 指定したモデル名が存在しない、またはAPIキーで利用できない

**解決策**:
1. `.env` ファイルに `GEMINI_MODEL=gemini-1.5-flash` を追加
2. または、アプリのコード内で直接指定

### 設定方法

#### 方法1: 環境変数で設定（推奨）

`.env` ファイルに追加：

```
GEMINI_API_KEY=あなたのAPIキー
GEMINI_MODEL=gemini-1.5-flash
```

#### 方法2: コード内で指定

`gemini_api.py` の25行目を直接編集：

```python
model_name = os.environ.get('GEMINI_MODEL', 'gemini-1.5-flash')
```

デフォルトのモデル名を変更できます。

## トラブルシューティング

### Q: どのモデルを使えばいい?

A: **gemini-1.5-flash** が最も安定しています。速度と精度のバランスが良く、コストも安いです。

### Q: gemini-2.0は使える?

A: 2026年1月時点では実験版（exp）のみで、安定性が保証されていません。本番環境では **gemini-1.5-flash** を推奨します。

### Q: エラーが続く場合は?

A: 
1. APIキーが正しいか確認
2. Google AI Studioでモデル一覧を確認
3. `gemini-1.5-flash` を使用（最も確実）

## 参考リンク

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API ドキュメント](https://ai.google.dev/docs)
