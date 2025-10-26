#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
03_cards.py - MDCardを使ったカード型UI

このサンプルでは、MDCardを使ったカード型UIの作り方を学びます。
- MDCardの基本的な使い方
- ScrollViewでスクロール対応
- 飲食店リスト風のカードデザイン
- 画像 + テキストのレイアウト

実行方法:
    python practice/03_cards.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDIconButton
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class CardsApp(MDApp):
    """
    カード型UIのサンプルアプリケーション

    飲食店リスト風のカードを複数表示するアプリです。
    ScrollViewを使って、画面に収まらない場合はスクロールできます。
    """

    def build(self):
        """
        UIを構築するメソッド

        ScrollViewの中にMDBoxLayoutを配置し、
        その中に複数のカードを追加します。

        Returns:
            MDScrollView: ルートウィジェット（スクロール可能なビュー）
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # スクロール可能なビュー
        # do_scroll_x=False: 横スクロール無効
        # do_scroll_y=True: 縦スクロール有効（デフォルト）
        scroll_view = MDScrollView()

        # カードを縦に並べるレイアウト
        # adaptive_height=True: 子ウィジェットの高さに応じて自動調整
        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            padding=dp(10),
            spacing=dp(10)
        )

        # サンプル飲食店データ
        restaurants = [
            {
                "name": "ラーメン大将",
                "category": "ラーメン",
                "address": "東京都渋谷区1-2-3",
                "rating": 4.5,
                "distance": "150m"
            },
            {
                "name": "カフェモカ",
                "category": "カフェ",
                "address": "東京都渋谷区2-3-4",
                "rating": 4.2,
                "distance": "200m"
            },
            {
                "name": "カレーハウス",
                "category": "カレー",
                "address": "東京都渋谷区3-4-5",
                "rating": 4.7,
                "distance": "300m"
            },
            {
                "name": "和食処 さくら",
                "category": "和食",
                "address": "東京都渋谷区4-5-6",
                "rating": 4.3,
                "distance": "400m"
            },
            {
                "name": "イタリアン トマト",
                "category": "イタリアン",
                "address": "東京都渋谷区5-6-7",
                "rating": 4.6,
                "distance": "500m"
            },
        ]

        # 各飲食店のカードを作成
        for restaurant in restaurants:
            card = self.create_restaurant_card(restaurant)
            layout.add_widget(card)

        scroll_view.add_widget(layout)
        return scroll_view

    def create_restaurant_card(self, restaurant):
        """
        飲食店カードを作成するメソッド

        Args:
            restaurant (dict): 飲食店情報（name, category, address, rating, distance）

        Returns:
            MDCard: 飲食店情報を表示するカード
        """
        # MDCard（角丸のカード）
        # elevation: 影の高さ（大きいほど浮いて見える）
        # padding: 内側の余白
        # size_hint_y: 高さを自動調整しない（Noneに設定）
        # height: 固定の高さ
        # radius: 角の丸み
        card = MDCard(
            elevation=2,
            padding=dp(10),
            size_hint_y=None,
            height=dp(120),
            radius=[dp(10)]
        )

        # カード内のレイアウト
        card_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=dp(10)
        )

        # 左側：アイコン（店舗画像の代わり）
        icon_button = MDIconButton(
            icon="store",  # 店舗アイコン
            icon_size=dp(48),
            pos_hint={"center_y": 0.5}
        )

        # 右側：店舗情報（縦に並べる）
        info_layout = MDBoxLayout(
            orientation="vertical",
            spacing=dp(5)
        )

        # 店名ラベル
        name_label = MDLabel(
            text=f"[b]{restaurant['name']}[/b]",
            markup=True,  # マークアップ（太字など）を有効化
            font_name="Roboto",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(25)
        )

        # カテゴリ・距離ラベル
        category_label = MDLabel(
            text=f"{restaurant['category']} • {restaurant['distance']}",
            font_name="Roboto",
            font_size=dp(14),
            size_hint_y=None,
            height=dp(20)
        )

        # 住所ラベル
        address_label = MDLabel(
            text=restaurant['address'],
            font_name="Roboto",
            font_size=dp(12),
            size_hint_y=None,
            height=dp(20)
        )

        # 評価ラベル（星マーク）
        rating_label = MDLabel(
            text=f"★ {restaurant['rating']}",
            font_name="Roboto",
            font_size=dp(14),
            size_hint_y=None,
            height=dp(20)
        )

        # 情報レイアウトにラベルを追加
        info_layout.add_widget(name_label)
        info_layout.add_widget(category_label)
        info_layout.add_widget(address_label)
        info_layout.add_widget(rating_label)

        # カードレイアウトにアイコンと情報を追加
        card_layout.add_widget(icon_button)
        card_layout.add_widget(info_layout)

        # カードにカードレイアウトを追加
        card.add_widget(card_layout)

        return card


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
    CardsApp().run()


if __name__ == '__main__':
    main()
