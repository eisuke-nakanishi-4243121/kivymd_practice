# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリで作業する際のガイダンスを提供します。

## プロジェクト概要

**プロジェクト名**: kivymd_practice
**目的**: KivyMD学習用練習プロジェクト
**対象**: final-assignment-teamsugata で使用するKivyMDコンポーネントの習得

## 環境

- **Platform**: WSL2 Ubuntu 22.04
- **Location**: `/home/user/buildozer-venv/projects/kivymd_practice`
- **Framework**: Kivy 2.2.1 + KivyMD
- **Build Tool**: Buildozer
- **Target Platform**: Android / Desktop
- **Language**: Python
- **Font**: NotoSansCJK-Regular.ttc（日本語対応）

## ディレクトリ構成

```
kivymd_practice/
├── main.py                          # メインエントリーポイント（サンプル選択メニュー）
├── buildozer.spec                   # Buildozer設定ファイル
├── requirements.txt                 # 依存関係
├── CLAUDE.md                        # このファイル
├── .gitignore                       # Git無視ファイル
├── assets/                          # アセット
│   └── fonts/
│       └── NotoSansCJK-Regular.ttc  # 日本語フォント
└── practice/                        # KivyMDコンポーネント別サンプル
    ├── 01_basic_app.py              # 基本的なMDAppの構造
    ├── 02_buttons.py                # ボタン各種（MDRaisedButton, MDFlatButton等）
    ├── 03_cards.py                  # MDCard（カード表示）
    ├── 04_dialogs.py                # MDDialog（ダイアログ）
    ├── 05_lists.py                  # MDList（リスト表示）
    ├── 06_navigation_drawer.py      # ナビゲーションドロワー
    ├── 07_bottom_navigation.py      # ボトムナビゲーション
    ├── 08_tabs.py                   # MDTabs（タブ）
    ├── 09_textfields.py             # MDTextField（入力フィールド）
    ├── 10_toolbar.py                # MDTopAppBar（ツールバー）
    ├── 11_bottom_sheet.py           # MDBottomSheet（ボトムシート）
    ├── 12_snackbar.py               # MDSnackbar（通知メッセージ）
    ├── 13_spinner.py                # MDSpinner/プログレスバー（ローディング）
    └── 14_switch_checkbox.py        # MDSwitch/MDCheckbox（スイッチ/チェックボックス）
```

## サンプル一覧

### 01_basic_app.py - 基本的なMDApp
- **内容**: MDAppクラスの基本構造
- **学習ポイント**:
  - `MDApp`クラスの継承
  - `build()`メソッドの実装
  - `MDLabel`を使った中央テキスト表示
  - ウィンドウサイズ設定
  - 日本語フォント設定（NotoSansCJK）

### 02_buttons.py - ボタン各種
- **内容**: KivyMDの各種ボタンコンポーネント
- **学習ポイント**:
  - `MDRaisedButton`（立体ボタン）
  - `MDFlatButton`（フラットボタン）
  - `MDIconButton`（アイコンボタン）
  - `on_press` / `on_release`イベント処理
  - ボタン押下でラベルのテキスト変更

### 03_cards.py - カード表示
- **内容**: MDCardを使ったカード型UI
- **学習ポイント**:
  - `MDCard`の基本的な使い方
  - `ScrollView` + `MDBoxLayout`でスクロール対応
  - 飲食店リスト風のカードデザイン（店名、住所、評価）
  - 画像 + テキストのレイアウト

### 04_dialogs.py - ダイアログ
- **内容**: ダイアログ（アラート、確認）の実装
- **学習ポイント**:
  - `MDDialog`の基本的な使い方
  - ボタン付きダイアログ
  - カスタムコンテンツを含むダイアログ
  - `open()` / `dismiss()`メソッド

### 05_lists.py - リスト表示
- **内容**: リストアイテムの表示と操作
- **学習ポイント**:
  - `MDList` + `OneLineListItem`
  - `TwoLineListItem`（2行リスト）
  - `ThreeLineListItem`（3行リスト）
  - リストアイテムクリックイベント
  - `ScrollView`対応

### 06_navigation_drawer.py - ナビゲーションドロワー
- **内容**: サイドメニュー（ドロワー）の実装
- **学習ポイント**:
  - `MDNavigationDrawer`の基本構造
  - `MDNavigationLayout`の使い方
  - メニューアイテムの作成
  - 画面切り替え

### 07_bottom_navigation.py - ボトムナビゲーション
- **内容**: 下部タブナビゲーション
- **学習ポイント**:
  - `MDBottomNavigation`の使い方
  - `MDBottomNavigationItem`で画面追加
  - 複数画面（ホーム、検索、お気に入り等）
  - アイコン付きタブ

### 08_tabs.py - タブ切り替え
- **内容**: タブUIの実装
- **学習ポイント**:
  - `MDTabs` + `MDTabsBase`
  - タブ内コンテンツの配置
  - タブ切り替えイベント

### 09_textfields.py - テキスト入力
- **内容**: テキストフィールドと入力バリデーション
- **学習ポイント**:
  - `MDTextField`の基本的な使い方
  - パスワード入力（`password: True`）
  - ヘルパーテキスト、エラー表示
  - バリデーション例（ログイン画面想定）

### 10_toolbar.py - トップバー
- **内容**: アプリ上部のツールバー
- **学習ポイント**:
  - `MDTopAppBar`の基本的な使い方
  - タイトル表示
  - 左右アイコンボタンの配置
  - ナビゲーションドロワーとの連携

### 11_bottom_sheet.py - ボトムシート
- **内容**: 画面下部から表示されるシート
- **学習ポイント**:
  - `MDBottomSheet`の基本的な使い方
  - モーダルボトムシート（画面を覆うタイプ）
  - スタンダードボトムシート（背景操作可能タイプ）
  - `MDBottomSheetDragHandle`でのドラッグ操作
  - `open()` / `dismiss()`メソッド
  - カスタムコンテンツの配置（リスト、ボタン等）

### 12_snackbar.py - スナックバー
- **内容**: 通知メッセージの表示
- **学習ポイント**:
  - `MDSnackbar`の基本的な使い方
  - シンプルな通知メッセージ
  - アクション付きスナックバー
  - 閉じるボタン付きスナックバー
  - カラーカスタマイズ（成功/エラーメッセージ）
  - 自動消去と手動消去

### 13_spinner.py - スピナー/プログレスバー
- **内容**: ローディング表示・進行状況の表示
- **学習ポイント**:
  - `MDSpinner`（円形スピナー）
  - `MDProgressBar`（線形プログレスバー）
  - `MDCircularProgressIndicator`（円形プログレス）
  - 確定/不確定プログレス
  - プログレスの更新とアニメーション
  - 非同期処理中の表示

### 14_switch_checkbox.py - スイッチ/チェックボックス
- **内容**: ON/OFF切り替えとチェックボックス
- **学習ポイント**:
  - `MDSwitch`の基本的な使い方
  - `MDCheckbox`の基本的な使い方
  - 状態の取得と設定
  - イベント処理（`on_active`）
  - 設定画面の実装例
  - 複数選択の管理

## 実行方法

### デスクトップ実行
```bash
# メインアプリ（サンプル選択メニュー）
cd /home/user/buildozer-venv/projects/kivymd_practice
python main.py

# 個別サンプルの実行
python practice/01_basic_app.py
python practice/02_buttons.py
# ... 以下同様
```

### Android実行
```bash
cd /home/user/buildozer-venv/projects/kivymd_practice

# デバッグビルド
buildozer android debug

# デバッグビルド + デプロイ + 実行
buildozer android debug deploy run
```

## 学習の進め方

### 推奨学習順序

1. **01_basic_app.py** から開始
   - KivyMDの基本構造を理解
   - MDAppクラスの使い方を把握

2. **02_buttons.py** → **09_textfields.py**
   - 基本的なUIコンポーネントを学習
   - イベント処理に慣れる

3. **06_navigation_drawer.py** / **07_bottom_navigation.py**
   - 画面遷移の実装方法を学習
   - アプリ全体の構造を理解

4. **実践**: final-assignment-teamsugata での応用
   - 学んだコンポーネントを組み合わせる
   - 地図画面、ログイン画面、口コミ画面の実装

### 学習のポイント

- ✅ **各サンプルは独立して実行可能** - 1つずつ試せる
- ✅ **日本語コメント付き** - コードの理解が容易
- ✅ **段階的に難易度UP** - 無理なく学習できる
- ✅ **実践的な内容** - final-assignment で使えるコンポーネント優先
- ✅ **200行以下** - 簡潔で理解しやすい

### コード確認のコツ

1. **まず実行してみる** - 動作を確認
2. **コメントを読む** - 各部分の役割を理解
3. **コードを変更してみる** - 試行錯誤で理解を深める
4. **他のサンプルと比較** - 共通パターンを見つける

## 参考リンク

### 公式ドキュメント
- **KivyMD公式**: https://kivymd.readthedocs.io/
- **Kivy公式**: https://kivy.org/doc/stable/
- **KivyMD Components**: https://kivymd.readthedocs.io/en/latest/components/

### よく使うコンポーネント
- **MDApp**: https://kivymd.readthedocs.io/en/latest/components/app/
- **MDButton**: https://kivymd.readthedocs.io/en/latest/components/button/
- **MDCard**: https://kivymd.readthedocs.io/en/latest/components/card/
- **MDDialog**: https://kivymd.readthedocs.io/en/latest/components/dialog/
- **MDList**: https://kivymd.readthedocs.io/en/latest/components/list/
- **MDNavigationDrawer**: https://kivymd.readthedocs.io/en/latest/components/navigationdrawer/
- **MDBottomNavigation**: https://kivymd.readthedocs.io/en/latest/components/bottomnavigation/
- **MDTextField**: https://kivymd.readthedocs.io/en/latest/components/textfield/

## コーディング規約

このプロジェクトは final-assignment-teamsugata と同じ規約に従います：

- **命名規則**: スネークケース（snake_case）
- **コメント**: すべて日本語で記述
- **ファイル名**: 小文字スネークケース
- **インデント**: スペース4つ

## メモ・Tips

### KivyMD の基本パターン

```python
from kivymd.app import MDApp
from kivymd.ufl import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, KivyMD!")

if __name__ == '__main__':
    MyApp().run()
```

### 日本語フォント設定

```python
from kivy.core.text import LabelBase

LabelBase.register(
    name='NotoSansCJK',
    fn_regular='assets/fonts/NotoSansCJK-Regular.ttc'
)
```

### よく使うレイアウト

- **MDBoxLayout**: 縦・横に並べる
- **MDFloatLayout**: 自由配置
- **MDGridLayout**: グリッド配置
- **ScrollView**: スクロール可能領域

### カラーテーマ

```python
class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"  # or "Dark"
        return ...
```

## 学習メモ欄

ここに学習中の気づきや、つまずいたポイント、解決方法などを自由に記録してください。

---

**更新履歴**
- 2025-10-24: プロジェクト作成、基本構成確立
