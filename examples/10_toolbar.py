#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
10_toolbar.py - MDTopAppBarを使ったツールバー

このサンプルでは、MDTopAppBarの使い方を学びます。
- MDTopAppBar（ツールバー）
- タイトル表示
- 左右アイコンボタンの配置

実行方法:
    python examples/10_toolbar.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.text import LabelBase
from kivy.core.window import Window


class ToolbarApp(MDApp):
    """
    ツールバーのサンプルアプリケーション

    MDTopAppBarの基本的な使い方を学びます。
    """

    def build(self):
        """
        UIを構築するメソッド

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        layout = MDBoxLayout(orientation="vertical")

        # MDTopAppBar（ツールバー）
        # title: タイトル
        # left_action_items: 左側のアイコンボタン
        # right_action_items: 右側のアイコンボタン
        # [["アイコン名", lambda x: 関数()], ...]の形式
        toolbar = MDTopAppBar(
            title="KivyMD Practice",
            left_action_items=[["menu", lambda x: self.on_menu_press()]],
            right_action_items=[
                ["magnify", lambda x: self.on_search_press()],
                ["dots-vertical", lambda x: self.on_more_press()],
            ]
        )
        layout.add_widget(toolbar)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="ツールバーのアイコンをタップしてください",
            halign="center",
            font_name="Roboto"
        )
        layout.add_widget(self.result_label)

        return layout

    def on_menu_press(self):
        """メニューボタンが押されたときの処理"""
        self.result_label.text = "メニューボタンが押されました"

    def on_search_press(self):
        """検索ボタンが押されたときの処理"""
        self.result_label.text = "検索ボタンが押されました"

    def on_more_press(self):
        """その他ボタンが押されたときの処理"""
        self.result_label.text = "その他ボタンが押されました"


def main():
    """アプリケーションのエントリーポイント"""
    Window.size = (360, 640)
    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )
    ToolbarApp().run()


if __name__ == '__main__':
    main()
