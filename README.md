# KivyMD Practice

KivyMD学習用の練習プロジェクトです。final-assignment-teamsugata で使用するKivyMDコンポーネントの習得を目的としています。

## 概要

このプロジェクトは、KivyMDの主要コンポーネントを実践的に学ぶためのサンプル集です。各サンプルは独立して実行でき、日本語のコメント付きで理解しやすい構成になっています。

## 環境

- **Platform**: WSL2 Ubuntu 22.04
- **Framework**: Kivy 2.2.1 + KivyMD
- **Build Tool**: Buildozer
- **Target**: Android / Desktop
- **Language**: Python
- **Font**: NotoSansCJKjp-Regular.otf（日本語対応）

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

## サンプル一覧

| No | ファイル名 | 内容 | 学習ポイント |
|---|---|---|---|
| 01 | [01_basic_app.py](practice/01_basic_app.py) | 基本的なMDApp | MDAppクラス、build()、日本語フォント設定 |
| 02 | [02_buttons.py](practice/02_buttons.py) | ボタン各種 | MDRaisedButton、MDFlatButton、MDIconButton |
| 03 | [03_cards.py](practice/03_cards.py) | カード表示 | MDCard、ScrollView、リスト型レイアウト |
| 04 | [04_dialogs.py](practice/04_dialogs.py) | ダイアログ | MDDialog、open()、dismiss()、カスタムコンテンツ |
| 05 | [05_lists.py](practice/05_lists.py) | リスト表示 | MDList、OneLineListItem、TwoLineListItem |
| 06 | [06_navigation_drawer.py](practice/06_navigation_drawer.py) | ナビゲーションドロワー | MDNavigationDrawer、サイドメニュー |
| 07 | [07_bottom_navigation.py](practice/07_bottom_navigation.py) | ボトムナビゲーション | MDBottomNavigation、タブ画面切り替え |
| 08 | [08_tabs.py](practice/08_tabs.py) | タブ切り替え | MDTabs、MDTabsBase、タブ内コンテンツ |
| 09 | [09_textfields.py](practice/09_textfields.py) | テキスト入力 | MDTextField、バリデーション、パスワード入力 |
| 10 | [10_toolbar.py](practice/10_toolbar.py) | トップバー | MDTopAppBar、タイトル、アイコンボタン |
| 11 | [11_bottom_sheet.py](practice/11_bottom_sheet.py) | ボトムシート | MDBottomSheet、モーダル/スタンダード |
| 12 | [12_snackbar.py](practice/12_snackbar.py) | スナックバー | MDSnackbar、通知メッセージ、アクション付き |
| 13 | [13_spinner.py](practice/13_spinner.py) | スピナー/プログレスバー | MDSpinner、MDProgressBar、ローディング表示 |
| 14 | [14_switch_checkbox.py](practice/14_switch_checkbox.py) | スイッチ/チェックボックス | MDSwitch、MDCheckbox、on_active |

## 推奨学習順序

1. **基礎** (01-02): MDAppの基本構造とイベント処理
2. **UI部品** (03-05, 09): カード、ダイアログ、リスト、テキスト入力
3. **ナビゲーション** (06-08, 10): 画面遷移、タブ、ツールバー
4. **補助機能** (11-14): ボトムシート、スナックバー、ローディング、スイッチ

## 特徴

- ✅ 各サンプルは独立して実行可能
- ✅ 日本語コメント付き
- ✅ 段階的に難易度UP
- ✅ 実践的な内容（final-assignment で使える）
- ✅ 200行以下の簡潔なコード

## 参考リンク

- **KivyMD公式**: https://kivymd.readthedocs.io/
- **Kivy公式**: https://kivy.org/doc/stable/
- **KivyMD Components**: https://kivymd.readthedocs.io/en/latest/components/

## ライセンス

このプロジェクトは学習目的で作成されています。

---

詳細な情報は [CLAUDE.md](CLAUDE.md) を参照してください。
