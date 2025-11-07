#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
15_chip.py - MDChip（チップ/タグ）

このサンプルでは、KivyMDのMDChipコンポーネントを学びます。
チップは小さなタグ風のUI要素で、カテゴリやフィルターの表示に使われます。

主な機能:
- 基本的なチップ（テキストのみ）
- アイコン付きチップ
- 削除可能なチップ（removable）
- チェック可能なチップ（check）
- チップのクリックイベント処理

実行方法:
    python practice/15_chip.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class ChipApp(MDApp):
    """
    MDChipの使い方を示すアプリケーション

    さまざまなスタイルのチップを表示し、クリックや削除などの
    インタラクション機能を実演します。
    """

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

        # スクロール可能なレイアウト
        scroll = MDScrollView()

        # メインレイアウト（縦方向）
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20),
            size_hint_y=None
        )
        main_layout.bind(minimum_height=main_layout.setter('height'))

        # タイトル
        title = MDLabel(
            text="MDChip サンプル",
            font_size=dp(24),
            halign="center",
            size_hint_y=None,
            height=dp(50)
        )
        main_layout.add_widget(title)

        # セクション1: 基本的なチップ
        main_layout.add_widget(self.create_section_label("1. 基本的なチップ"))
        main_layout.add_widget(self.create_basic_chips())

        # セクション2: アイコン付きチップ
        main_layout.add_widget(self.create_section_label("2. アイコン付きチップ"))
        main_layout.add_widget(self.create_icon_chips())

        # セクション3: 削除可能なチップ
        main_layout.add_widget(self.create_section_label("3. 削除可能なチップ"))
        main_layout.add_widget(self.create_removable_chips())

        # セクション4: チェック可能なチップ（選択型）
        main_layout.add_widget(self.create_section_label("4. チェック可能なチップ"))
        main_layout.add_widget(self.create_checkable_chips())

        # セクション5: 実用例（カテゴリフィルター）
        main_layout.add_widget(self.create_section_label("5. カテゴリフィルター例"))
        main_layout.add_widget(self.create_category_filter())

        # ステータス表示用ラベル
        self.status_label = MDLabel(
            text="チップをタップしてみてください",
            halign="center",
            size_hint_y=None,
            height=dp(40),
            theme_text_color="Secondary"
        )
        main_layout.add_widget(self.status_label)

        scroll.add_widget(main_layout)
        screen.add_widget(scroll)

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

    def create_basic_chips(self):
        """
        基本的なチップのレイアウトを作成

        Returns:
            MDBoxLayout: チップを含むレイアウト
        """
        layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40),
            adaptive_width=True
        )

        # シンプルなチップ
        chips_data = ["Python", "Kivy", "KivyMD", "Android"]

        for chip_text in chips_data:
            chip = MDChip(
                MDChipText(
                    text=chip_text,
                ),
                pos_hint={'center_y': 0.5}
            )
            chip.bind(on_release=lambda x, t=chip_text: self.on_chip_click(t))
            layout.add_widget(chip)

        return layout

    def create_icon_chips(self):
        """
        アイコン付きチップのレイアウトを作成

        Returns:
            MDBoxLayout: チップを含むレイアウト
        """
        layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40),
            adaptive_width=True
        )

        # アイコン付きチップ
        chips_data = [
            ("ホーム", "home"),
            ("検索", "magnify"),
            ("設定", "cog"),
            ("お気に入り", "heart")
        ]

        for chip_text, icon in chips_data:
            chip = MDChip(
                MDChipText(
                    text=chip_text,
                ),
                icon_left=icon,
                pos_hint={'center_y': 0.5}
            )
            chip.bind(on_release=lambda x, t=chip_text: self.on_chip_click(t))
            layout.add_widget(chip)

        return layout

    def create_removable_chips(self):
        """
        削除可能なチップのレイアウトを作成

        Returns:
            MDBoxLayout: チップを含むレイアウト
        """
        layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40),
            adaptive_width=True
        )

        # 削除可能なチップ（タグ風）
        tags = ["旅行", "グルメ", "写真", "音楽"]

        for tag in tags:
            chip = MDChip(
                MDChipText(
                    text=tag,
                ),
                icon_left="tag",
                icon_right="close",
                pos_hint={'center_y': 0.5}
            )
            chip.bind(
                on_release=lambda x, t=tag: self.on_chip_click(t)
            )
            # 右アイコン（×ボタン）をクリックすると削除
            chip.bind(
                on_remove=lambda x, t=tag: self.on_chip_remove(x, t)
            )
            layout.add_widget(chip)

        return layout

    def create_checkable_chips(self):
        """
        チェック可能なチップのレイアウトを作成

        Returns:
            MDBoxLayout: チップを含むレイアウト
        """
        layout = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40),
            adaptive_width=True
        )

        # チェック可能なチップ（選択型）
        options = ["全て", "未読", "重要", "スター付き"]

        for option in options:
            chip = MDChip(
                MDChipText(
                    text=option,
                ),
                type="filter",  # filterタイプでチェックマーク表示
                pos_hint={'center_y': 0.5}
            )
            chip.bind(on_release=lambda x, t=option: self.on_chip_toggle(x, t))
            layout.add_widget(chip)

        return layout

    def create_category_filter(self):
        """
        実用例: カテゴリフィルターのレイアウトを作成

        Returns:
            MDBoxLayout: チップを含むレイアウト
        """
        layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(100)
        )

        # カテゴリ行1
        row1 = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40)
        )

        categories1 = ["和食", "洋食", "中華", "イタリアン"]
        for category in categories1:
            chip = MDChip(
                MDChipText(
                    text=category,
                ),
                icon_left="silverware-fork-knife",
                type="filter",
                pos_hint={'center_y': 0.5}
            )
            chip.bind(on_release=lambda x, c=category: self.on_category_select(x, c))
            row1.add_widget(chip)

        # カテゴリ行2
        row2 = MDBoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40)
        )

        categories2 = ["カフェ", "居酒屋", "ラーメン", "スイーツ"]
        for category in categories2:
            chip = MDChip(
                MDChipText(
                    text=category,
                ),
                icon_left="coffee",
                type="filter",
                pos_hint={'center_y': 0.5}
            )
            chip.bind(on_release=lambda x, c=category: self.on_category_select(x, c))
            row2.add_widget(chip)

        layout.add_widget(row1)
        layout.add_widget(row2)

        return layout

    def on_chip_click(self, chip_text):
        """
        チップクリック時のイベントハンドラー

        Args:
            chip_text (str): クリックされたチップのテキスト
        """
        self.status_label.text = f"「{chip_text}」がクリックされました"

    def on_chip_remove(self, chip_instance, chip_text):
        """
        チップ削除時のイベントハンドラー

        Args:
            chip_instance: チップインスタンス
            chip_text (str): 削除されたチップのテキスト
        """
        self.status_label.text = f"「{chip_text}」が削除されました"
        # チップを親レイアウトから削除
        if chip_instance.parent:
            chip_instance.parent.remove_widget(chip_instance)

    def on_chip_toggle(self, chip_instance, chip_text):
        """
        チェック可能なチップの切り替えイベントハンドラー

        Args:
            chip_instance: チップインスタンス
            chip_text (str): チップのテキスト
        """
        # active属性でチェック状態を取得（filterタイプの場合）
        state = "選択" if chip_instance.active else "解除"
        self.status_label.text = f"「{chip_text}」が{state}されました"

    def on_category_select(self, chip_instance, category):
        """
        カテゴリフィルター選択時のイベントハンドラー

        Args:
            chip_instance: チップインスタンス
            category (str): 選択されたカテゴリ
        """
        state = "選択" if chip_instance.active else "解除"
        self.status_label.text = f"カテゴリ「{category}」が{state}されました"


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
    ChipApp().run()


if __name__ == '__main__':
    main()
