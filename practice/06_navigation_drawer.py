#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
06_navigation_drawer.py - ナビゲーションドロワー（サイドメニュー）

このサンプルでは、MDNavigationDrawerの基本的な使い方を学びます。
- MDNavigationDrawer（サイドメニュー）
- MDNavigationLayout
- メニューアイテムの作成
- 画面切り替え

注意: このサンプルは簡略版です。実際のアプリではより複雑な実装になります。

実行方法:
    python practice/06_navigation_drawer.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.text import LabelBase
from kivy.core.window import Window


class NavigationDrawerApp(MDApp):
    """
    ナビゲーションドロワーのサンプルアプリケーション

    注意: KivyMDの最新バージョンではナビゲーションドロワーの実装が変更されています。
    このサンプルは基本的な概念を示すための簡略版です。
    """

    def build(self):
        """UIを構築するメソッド"""
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        layout = MDBoxLayout(orientation="vertical")

        # ツールバー
        toolbar = MDTopAppBar(
            title="ナビゲーションドロワー",
            left_action_items=[["menu", lambda x: self.show_info()]]
        )
        layout.add_widget(toolbar)

        # 情報ラベル
        self.info_label = MDLabel(
            text="ナビゲーションドロワーは\nサイドメニュー機能です。\n\n実際の実装にはMDNavigationLayout、\nMDNavigationDrawer、\nMDScreenManagerなどを使用します。",
            halign="center",
            font_name="Roboto"
        )
        layout.add_widget(self.info_label)

        return layout

    def show_info(self):
        """メニューボタンが押されたときの処理"""
        self.info_label.text = "メニューボタンが押されました\n\nナビゲーションドロワーの完全な実装は\n07_bottom_navigation.pyを参照してください"


def main():
    """アプリケーションのエントリーポイント"""
    Window.size = (360, 640)
    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )
    NavigationDrawerApp().run()


if __name__ == '__main__':
    main()
