#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
08_tabs.py - MDTabsを使ったタブUI

このサンプルでは、MDTabsの使い方を学びます。
- MDTabs + MDTabsBase
- タブ内コンテンツ
- タブ切り替え

実行方法:
    python examples/08_tabs.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.core.text import LabelBase
from kivy.core.window import Window


class Tab(MDBoxLayout, MDTabsBase):
    """
    タブのベースクラス

    MDTabsBaseを継承してタブのコンテンツを定義します。
    """
    pass


class TabsApp(MDApp):
    """
    タブUIのサンプルアプリケーション

    3つのタブ（情報、設定、ヘルプ）を切り替えられる
    タブUIを実装します。
    """

    def build(self):
        """UIを構築するメソッド"""
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        layout = MDBoxLayout(orientation="vertical")

        # MDTabs（タブバー）
        tabs = MDTabs()

        # タブ1: 情報
        tab1 = Tab(title="情報")
        tab1_label = MDLabel(
            text="情報タブ\n\nアプリの情報を表示します",
            halign="center",
            font_name="Roboto"
        )
        tab1.add_widget(tab1_label)
        tabs.add_widget(tab1)

        # タブ2: 設定
        tab2 = Tab(title="設定")
        tab2_label = MDLabel(
            text="設定タブ\n\nアプリの設定を変更できます",
            halign="center",
            font_name="Roboto"
        )
        tab2.add_widget(tab2_label)
        tabs.add_widget(tab2)

        # タブ3: ヘルプ
        tab3 = Tab(title="ヘルプ")
        tab3_label = MDLabel(
            text="ヘルプタブ\n\n使い方の説明を表示します",
            halign="center",
            font_name="Roboto"
        )
        tab3.add_widget(tab3_label)
        tabs.add_widget(tab3)

        layout.add_widget(tabs)
        return layout


def main():
    """アプリケーションのエントリーポイント"""
    Window.size = (360, 640)
    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )
    TabsApp().run()


if __name__ == '__main__':
    main()
