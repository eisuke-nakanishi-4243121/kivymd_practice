#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
16_menu.py - MDDropdownMenu（ドロップダウンメニュー）

このサンプルでは、KivyMDのMDDropdownMenuコンポーネントを学びます。
ドロップダウンメニューは、オプション選択やコンテキストメニューに使用されます。

主な機能:
- 基本的なドロップダウンメニュー
- アイコン付きメニューアイテム
- メニューアイテムの選択処理
- ボタンからメニューを開く
- 複数のメニュー（異なる用途）

実行方法:
    python practice/16_menu.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class MenuApp(MDApp):
    """
    MDDropdownMenuの使い方を示すアプリケーション

    さまざまなスタイルのドロップダウンメニューを表示し、
    メニューアイテムの選択処理を実演します。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_simple = None
        self.menu_icons = None
        self.menu_sort = None
        self.menu_context = None

    def build(self):
        """
        UIを構築するメソッド

        Returns:
            MDScreen: ルートスクリーン
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインスクリーン
        screen = MDScreen()

        # メインレイアウト（縦方向）
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20)
        )

        # タイトル
        title = MDLabel(
            text="MDDropdownMenu サンプル",
            font_size=dp(24),
            halign="center",
            size_hint_y=None,
            height=dp(50)
        )
        main_layout.add_widget(title)

        # セクション1: シンプルなメニュー
        main_layout.add_widget(self.create_section_label("1. シンプルなメニュー"))
        self.simple_button = MDRaisedButton(
            text="言語を選択",
            pos_hint={'center_x': 0.5},
            size_hint_x=0.8
        )
        self.simple_button.bind(on_release=self.open_simple_menu)
        main_layout.add_widget(self.simple_button)

        # セクション2: アイコン付きメニュー
        main_layout.add_widget(self.create_section_label("2. アイコン付きメニュー"))
        self.icon_button = MDRaisedButton(
            text="アクションを選択",
            pos_hint={'center_x': 0.5},
            size_hint_x=0.8
        )
        self.icon_button.bind(on_release=self.open_icon_menu)
        main_layout.add_widget(self.icon_button)

        # セクション3: ソートメニュー
        main_layout.add_widget(self.create_section_label("3. ソートメニュー"))
        sort_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(50),
            spacing=dp(10)
        )
        sort_label = MDLabel(
            text="並び替え:",
            size_hint_x=0.3
        )
        self.sort_button = MDRaisedButton(
            text="新着順",
            size_hint_x=0.7
        )
        self.sort_button.bind(on_release=self.open_sort_menu)
        sort_layout.add_widget(sort_label)
        sort_layout.add_widget(self.sort_button)
        main_layout.add_widget(sort_layout)

        # セクション4: コンテキストメニュー（カード右上の...ボタン）
        main_layout.add_widget(self.create_section_label("4. コンテキストメニュー"))
        main_layout.add_widget(self.create_card_with_menu())

        # ステータス表示用ラベル
        self.status_label = MDLabel(
            text="メニューボタンをタップしてください",
            halign="center",
            size_hint_y=None,
            height=dp(60),
            theme_text_color="Secondary"
        )
        main_layout.add_widget(self.status_label)

        screen.add_widget(main_layout)

        # メニューの初期化
        self.create_menus()

        return screen

    def create_section_label(self, text):
        """
        セクションラベルを作成

        Args:
            text (str): セクションのタイトル

        Returns:
            MDLabel: セクションラベル
        """
        return MDLabel(
            text=text,
            font_size=dp(18),
            size_hint_y=None,
            height=dp(40),
            theme_text_color="Primary"
        )

    def create_card_with_menu(self):
        """
        コンテキストメニュー付きカードを作成

        Returns:
            MDCard: メニューボタン付きカード
        """
        card = MDCard(
            orientation='horizontal',
            size_hint=(None, None),
            size=(dp(320), dp(80)),
            pos_hint={'center_x': 0.5},
            padding=dp(10)
        )

        # カード内容
        content_layout = MDBoxLayout(
            orientation='vertical',
            size_hint_x=0.8
        )
        title = MDLabel(
            text="投稿タイトル",
            font_size=dp(16),
            size_hint_y=None,
            height=dp(30)
        )
        subtitle = MDLabel(
            text="2025年11月7日",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(20)
        )
        content_layout.add_widget(title)
        content_layout.add_widget(subtitle)

        # メニューボタン（右上の...）
        self.context_menu_button = MDIconButton(
            icon="dots-vertical",
            pos_hint={'center_y': 0.5},
            size_hint_x=0.2
        )
        self.context_menu_button.bind(on_release=self.open_context_menu)

        card.add_widget(content_layout)
        card.add_widget(self.context_menu_button)

        return card

    def create_menus(self):
        """
        各種メニューを作成
        """
        # 1. シンプルなメニュー（言語選択）
        menu_items_simple = [
            {
                "text": "日本語",
                "on_release": lambda: self.menu_callback("日本語", self.menu_simple)
            },
            {
                "text": "English",
                "on_release": lambda: self.menu_callback("English", self.menu_simple)
            },
            {
                "text": "中文",
                "on_release": lambda: self.menu_callback("中文", self.menu_simple)
            },
            {
                "text": "한국어",
                "on_release": lambda: self.menu_callback("한국어", self.menu_simple)
            }
        ]
        self.menu_simple = MDDropdownMenu(
            caller=self.simple_button,
            items=menu_items_simple,
            width_mult=4
        )

        # 2. アイコン付きメニュー
        menu_items_icons = [
            {
                "text": "共有",
                "leading_icon": "share-variant",
                "on_release": lambda: self.menu_callback("共有", self.menu_icons)
            },
            {
                "text": "コピー",
                "leading_icon": "content-copy",
                "on_release": lambda: self.menu_callback("コピー", self.menu_icons)
            },
            {
                "text": "削除",
                "leading_icon": "delete",
                "on_release": lambda: self.menu_callback("削除", self.menu_icons)
            },
            {
                "text": "お気に入り",
                "leading_icon": "heart",
                "on_release": lambda: self.menu_callback("お気に入り", self.menu_icons)
            },
            {
                "text": "設定",
                "leading_icon": "cog",
                "on_release": lambda: self.menu_callback("設定", self.menu_icons)
            }
        ]
        self.menu_icons = MDDropdownMenu(
            caller=self.icon_button,
            items=menu_items_icons,
            width_mult=4
        )

        # 3. ソートメニュー
        menu_items_sort = [
            {
                "text": "新着順",
                "on_release": lambda: self.sort_callback("新着順")
            },
            {
                "text": "古い順",
                "on_release": lambda: self.sort_callback("古い順")
            },
            {
                "text": "人気順",
                "on_release": lambda: self.sort_callback("人気順")
            },
            {
                "text": "評価順",
                "on_release": lambda: self.sort_callback("評価順")
            }
        ]
        self.menu_sort = MDDropdownMenu(
            caller=self.sort_button,
            items=menu_items_sort,
            width_mult=3
        )

        # 4. コンテキストメニュー
        menu_items_context = [
            {
                "text": "編集",
                "leading_icon": "pencil",
                "on_release": lambda: self.menu_callback("編集", self.menu_context)
            },
            {
                "text": "共有",
                "leading_icon": "share-variant",
                "on_release": lambda: self.menu_callback("共有", self.menu_context)
            },
            {
                "text": "報告",
                "leading_icon": "flag",
                "on_release": lambda: self.menu_callback("報告", self.menu_context)
            },
            {
                "text": "削除",
                "leading_icon": "delete",
                "on_release": lambda: self.menu_callback("削除", self.menu_context)
            }
        ]
        self.menu_context = MDDropdownMenu(
            caller=self.context_menu_button,
            items=menu_items_context,
            width_mult=3
        )

    def open_simple_menu(self, button):
        """
        シンプルなメニューを開く

        Args:
            button: ボタンインスタンス
        """
        self.menu_simple.open()

    def open_icon_menu(self, button):
        """
        アイコン付きメニューを開く

        Args:
            button: ボタンインスタンス
        """
        self.menu_icons.open()

    def open_sort_menu(self, button):
        """
        ソートメニューを開く

        Args:
            button: ボタンインスタンス
        """
        self.menu_sort.open()

    def open_context_menu(self, button):
        """
        コンテキストメニューを開く

        Args:
            button: ボタンインスタンス
        """
        self.menu_context.open()

    def menu_callback(self, item_text, menu_instance):
        """
        メニューアイテム選択時のコールバック

        Args:
            item_text (str): 選択されたアイテムのテキスト
            menu_instance: メニューインスタンス
        """
        self.status_label.text = f"「{item_text}」が選択されました"
        menu_instance.dismiss()

    def sort_callback(self, sort_type):
        """
        ソートメニュー選択時のコールバック

        Args:
            sort_type (str): 選択されたソート種類
        """
        self.sort_button.text = sort_type
        self.status_label.text = f"並び替え: {sort_type}"
        self.menu_sort.dismiss()


def main():
    """
    アプリケーションのエントリーポイント
    """
    # ウィンドウサイズ設定（スマートフォン縦画面）
    Window.size = (360, 640)

    # 日本語フォント登録
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )

    # アプリケーション実行
    MenuApp().run()


if __name__ == '__main__':
    main()
