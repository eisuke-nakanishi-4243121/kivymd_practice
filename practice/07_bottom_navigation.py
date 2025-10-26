#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
07_bottom_navigation.py - ボトムナビゲーション（下部タブ）

このサンプルでは、MDBottomNavigationの使い方を学びます。
- MDBottomNavigation
- MDBottomNavigationItem（画面）
- アイコン付きタブ
- 画面切り替え

実行方法:
    python practice/07_bottom_navigation.py
"""

from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.core.text import LabelBase
from kivy.core.window import Window


class BottomNavigationApp(MDApp):
    """
    ボトムナビゲーションのサンプルアプリケーション

    3つの画面（ホーム、検索、お気に入り）を切り替えられる
    ボトムナビゲーションバーを実装します。
    """

    def build(self):
        """UIを構築するメソッド"""
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # MDBottomNavigation（ボトムナビゲーションバー）
        bottom_nav = MDBottomNavigation()

        # ホーム画面
        home_screen = MDBottomNavigationItem(
            name="home",
            text="ホーム",
            icon="home"
        )
        home_layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )
        home_label = MDLabel(
            text="ホーム画面\n\nここにホーム画面のコンテンツを配置します",
            halign="center",
            font_name="Roboto"
        )
        home_layout.add_widget(home_label)
        home_screen.add_widget(home_layout)
        bottom_nav.add_widget(home_screen)

        # 検索画面
        search_screen = MDBottomNavigationItem(
            name="search",
            text="検索",
            icon="magnify"
        )
        search_layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )
        search_label = MDLabel(
            text="検索画面\n\nここに検索機能を配置します",
            halign="center",
            font_name="Roboto"
        )
        search_layout.add_widget(search_label)
        search_screen.add_widget(search_layout)
        bottom_nav.add_widget(search_screen)

        # お気に入り画面
        favorite_screen = MDBottomNavigationItem(
            name="favorite",
            text="お気に入り",
            icon="star"
        )
        favorite_layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )
        favorite_label = MDLabel(
            text="お気に入り画面\n\nここにお気に入りリストを表示します",
            halign="center",
            font_name="Roboto"
        )
        favorite_layout.add_widget(favorite_label)
        favorite_screen.add_widget(favorite_layout)
        bottom_nav.add_widget(favorite_screen)

        return bottom_nav


def main():
    """アプリケーションのエントリーポイント"""
    Window.size = (360, 640)
    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )
    BottomNavigationApp().run()


if __name__ == '__main__':
    main()
