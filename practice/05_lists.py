#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
05_lists.py - MDListを使ったリスト表示

このサンプルでは、MDListの使い方を学びます。
- OneLineListItem（1行リスト）
- TwoLineListItem（2行リスト）
- ThreeLineListItem（3行リスト）
- リストアイテムクリックイベント
- ScrollView対応

実行方法:
    python practice/05_lists.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivy.core.window import Window


class ListsApp(MDApp):
    """
    リスト表示のサンプルアプリケーション

    様々なスタイルのリストアイテムの使い方を学びます。
    """

    def build(self):
        """
        UIを構築するメソッド

        ScrollView内にMDListを配置し、
        様々な種類のリストアイテムを追加します。

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        main_layout = MDBoxLayout(orientation="vertical")

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="リストアイテムをタップしてください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.15
        )
        main_layout.add_widget(self.result_label)

        # スクロールビュー
        scroll_view = MDScrollView()

        # MDList（リストコンテナ）
        list_widget = MDList()

        # 1行リストアイテム（OneLineListItem）
        list_widget.add_widget(
            OneLineListItem(
                text="1行リストアイテム",
                on_press=lambda x: self.on_item_press("1行リストアイテム")
            )
        )

        # 2行リストアイテム（TwoLineListItem）
        # text: 1行目のテキスト
        # secondary_text: 2行目のテキスト
        two_line_item = TwoLineListItem(
            text="2行リストアイテム",
            secondary_text="これは2行目のテキストです",
            on_press=lambda x: self.on_item_press("2行リストアイテム")
        )
        list_widget.add_widget(two_line_item)

        # 3行リストアイテム（ThreeLineListItem）
        three_line_item = ThreeLineListItem(
            text="3行リストアイテム",
            secondary_text="これは2行目のテキストです\nこれは3行目のテキストです",
            on_press=lambda x: self.on_item_press("3行リストアイテム")
        )
        list_widget.add_widget(three_line_item)

        # 通常の1行リストアイテム（アイコン無し版に変更）
        # KivyMD 1.2.0ではアイコン付きリストの実装が複雑なため、
        # シンプルなテキストのみのリストに変更
        simple_item = OneLineListItem(
            text="⭐ 絵文字付きリスト",
            on_press=lambda x: self.on_item_press("絵文字付きリスト")
        )
        list_widget.add_widget(simple_item)

        # 飲食店リストの例
        # アイコンの代わりに絵文字を使用（KivyMD 1.2.0の制限回避）
        restaurants = [
            ("🍜 ラーメン大将", "東京都渋谷区1-2-3"),
            ("☕ カフェモカ", "東京都渋谷区2-3-4"),
            ("🍛 カレーハウス", "東京都渋谷区3-4-5"),
            ("🍱 和食処 さくら", "東京都渋谷区4-5-6"),
            ("🍝 イタリアン トマト", "東京都渋谷区5-6-7"),
        ]

        for name, address in restaurants:
            item = TwoLineListItem(
                text=name,
                secondary_text=address,
                on_press=lambda x, n=name: self.on_restaurant_press(n)
            )
            list_widget.add_widget(item)

        scroll_view.add_widget(list_widget)
        main_layout.add_widget(scroll_view)

        return main_layout

    def on_item_press(self, item_name):
        """
        リストアイテムがタップされたときの処理

        Args:
            item_name (str): タップされたアイテムの名前
        """
        self.result_label.text = f"「{item_name}」がタップされました"

    def on_restaurant_press(self, restaurant_name):
        """
        飲食店リストアイテムがタップされたときの処理

        Args:
            restaurant_name (str): タップされた飲食店の名前
        """
        self.result_label.text = f"「{restaurant_name}」が選択されました"


# TwoLineIconListItemクラスを定義（カスタムクラス）
class TwoLineIconListItem(TwoLineListItem):
    """
    アイコン付き2行リストアイテム

    TwoLineListItemを継承して、アイコンを追加できるようにします。
    """
    pass


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
    ListsApp().run()


if __name__ == '__main__':
    main()
