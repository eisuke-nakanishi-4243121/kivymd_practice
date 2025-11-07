#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py - KivyMD練習プロジェクトのメインアプリケーション

このアプリケーションは、practice/ ディレクトリ内の
各サンプルファイルの説明を表示するランチャーです。

実行方法:
    python main.py

各サンプルを実際に実行するには:
    python practice/01_basic_app.py
    python practice/02_buttons.py
    ... etc
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class KivyMDPracticeApp(MDApp):
    """
    KivyMD練習プロジェクトのメインアプリケーション

    各サンプルファイルの説明を表示するランチャーアプリです。
    """

    def build(self):
        """
        UIを構築するメソッド

        サンプルファイル一覧を表示します。

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        main_layout = MDBoxLayout(orientation="vertical")

        # ツールバー
        toolbar = MDTopAppBar(
            title="KivyMD Practice"
        )
        main_layout.add_widget(toolbar)

        # スクロールビュー
        scroll_view = MDScrollView()

        # コンテンツレイアウト
        content_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            padding=dp(10),
            spacing=dp(10)
        )

        # 説明カード
        info_card = MDCard(
            elevation=2,
            padding=dp(15),
            size_hint_y=None,
            height=dp(150),
            radius=[dp(10)]
        )
        info_label = MDLabel(
            text="KivyMD練習プロジェクトへようこそ！\n\n以下のサンプルは practice/ ディレクトリにあります。\n各サンプルを実行するには:\n\npython practice/XX_xxxx.py\n\nの形式で実行してください。",
            size_hint_y=None,
            height=dp(140)
        )
        info_card.add_widget(info_label)
        content_layout.add_widget(info_card)

        # サンプル一覧
        samples = [
            ("01_basic_app.py", "基本的なMDApp", "MDAppクラスの基本構造、日本語フォント設定"),
            ("02_buttons.py", "ボタン各種", "Raised、Flat、Iconボタンとイベント処理"),
            ("03_cards.py", "カード表示", "MDCard、飲食店リスト風UI、ScrollView"),
            ("04_dialogs.py", "ダイアログ", "アラート、確認、カスタムダイアログ"),
            ("05_lists.py", "リスト表示", "OneLineListItem、TwoLineListItem等"),
            ("06_navigation_drawer.py", "ナビゲーションドロワー", "サイドメニューの基本（簡略版）"),
            ("07_bottom_navigation.py", "ボトムナビゲーション", "下部タブナビゲーション、画面切り替え"),
            ("08_tabs.py", "タブUI", "MDTabs、タブ切り替え"),
            ("09_textfields.py", "テキスト入力", "MDTextField、バリデーション、ログイン画面"),
            ("10_toolbar.py", "ツールバー", "MDTopAppBar、アイコンボタン"),
            ("11_bottom_sheet.py", "ボトムシート", "画面下部から表示されるシート、ドラッグ操作"),
            ("12_snackbar.py", "スナックバー", "通知メッセージ、アクション付き通知"),
            ("13_spinner.py", "スピナー/プログレスバー", "ローディング表示、進行状況表示"),
            ("14_switch_checkbox.py", "スイッチ/チェックボックス", "ON/OFF切り替え、複数選択"),
            ("15_chip.py", "チップ/タグ", "タグ風UI、削除可能、チェック可能"),
            ("16_menu.py", "ドロップダウンメニュー", "メニュー選択、コンテキストメニュー"),
        ]

        # サンプルリスト
        list_widget = MDList()

        for filename, title, description in samples:
            item = TwoLineListItem(
                text=f"{filename} - {title}",
                secondary_text=description
            )
            list_widget.add_widget(item)

        content_layout.add_widget(list_widget)

        # フッター情報カード
        footer_card = MDCard(
            elevation=2,
            padding=dp(15),
            size_hint_y=None,
            height=dp(100),
            radius=[dp(10)]
        )
        footer_label = MDLabel(
            text="詳細情報:\n- CLAUDE.md を参照\n- KivyMD公式: https://kivymd.readthedocs.io/",
            size_hint_y=None,
            height=dp(90)
        )
        footer_card.add_widget(footer_label)
        content_layout.add_widget(footer_card)

        scroll_view.add_widget(content_layout)
        main_layout.add_widget(scroll_view)

        return main_layout


def main():
    """
    アプリケーションのエントリーポイント
    """
    # デスクトップ実行時のウィンドウサイズ設定
    Window.size = (360, 640)

    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )

    # アプリケーションの起動
    KivyMDPracticeApp().run()


if __name__ == '__main__':
    main()
