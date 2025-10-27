#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
11_bottom_sheet.py - MDBottomSheetを使ったボトムシート

このサンプルでは、MDBottomSheetの使い方を学びます。
- モーダルボトムシート（画面を覆うタイプ）
- スタンダードボトムシート（背景操作可能タイプ）
- ドラッグハンドルでの開閉
- カスタムコンテンツの配置

実行方法:
    python practice/11_bottom_sheet.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.bottomsheet import MDBottomSheetDragHandle
from kivymd.uix.bottomsheet import MDBottomSheetDragHandleTitle
from kivymd.uix.bottomsheet import MDBottomSheetDragHandleButton
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class BottomSheetApp(MDApp):
    """
    ボトムシートのサンプルアプリケーション

    モーダルとスタンダードの2種類のボトムシートを実装します。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ボトムシートのインスタンスを保持
        self.modal_sheet = None
        self.standard_sheet = None

    def build(self):
        """UIを構築するメソッド"""
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メイン画面の作成
        screen = MDScreen()

        # メインコンテンツのレイアウト
        main_layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20)
        )

        # タイトルラベル
        title_label = MDLabel(
            text="ボトムシートサンプル",
            halign="center",
            font_name="Roboto",
            font_style="H5",
            size_hint_y=0.2
        )
        main_layout.add_widget(title_label)

        # 説明ラベル
        desc_label = MDLabel(
            text="2種類のボトムシートを試すことができます",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.1
        )
        main_layout.add_widget(desc_label)

        # モーダルボトムシートを開くボタン
        modal_button = MDRaisedButton(
            text="モーダルボトムシート",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.open_modal_sheet
        )
        main_layout.add_widget(modal_button)

        # スタンダードボトムシートを開くボタン
        standard_button = MDRaisedButton(
            text="スタンダードボトムシート",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.open_standard_sheet
        )
        main_layout.add_widget(standard_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="ボトムシートを開いてください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.3
        )
        main_layout.add_widget(self.result_label)

        # メインレイアウトを画面に追加
        screen.add_widget(main_layout)

        # モーダルボトムシートの作成
        self.modal_sheet = self.create_modal_sheet()
        screen.add_widget(self.modal_sheet)

        # スタンダードボトムシートの作成
        self.standard_sheet = self.create_standard_sheet()
        screen.add_widget(self.standard_sheet)

        return screen

    def create_modal_sheet(self):
        """
        モーダルボトムシートを作成

        Returns:
            MDBottomSheet: モーダルボトムシート
        """
        # MDBottomSheet作成（デフォルトはモーダルタイプ）
        sheet = MDBottomSheet(
            size_hint_y=None,
            height=dp(400),
            type="modal",  # モーダルタイプ（背景を覆う）
            radius=[dp(16), dp(16), 0, 0],  # 上部の角を丸める
        )

        # ドラッグハンドル（ヘッダー部分）
        drag_handle = MDBottomSheetDragHandle()

        # タイトル
        handle_title = MDBottomSheetDragHandleTitle(
            text="モーダルボトムシート",
            pos_hint={"center_y": 0.5}
        )
        drag_handle.add_widget(handle_title)

        # 閉じるボタン
        close_button = MDBottomSheetDragHandleButton(
            icon="close",
            on_release=lambda x: sheet.dismiss()
        )
        drag_handle.add_widget(close_button)

        sheet.add_widget(drag_handle)

        # コンテンツ部分
        content = MDBoxLayout(
            orientation="vertical",
            padding=[dp(16), 0, dp(16), dp(16)],
            spacing=dp(10)
        )

        # 説明テキスト
        info_label = MDLabel(
            text="これはモーダルボトムシートです。\n背景のUIは操作できません。",
            halign="center",
            font_name="Roboto",
            size_hint_y=None,
            height=dp(60)
        )
        content.add_widget(info_label)

        # アクションリスト
        scroll = MDScrollView(size_hint=(1, 1))
        list_widget = MDList()

        actions = [
            ("共有", "share-variant"),
            ("リンクをコピー", "link"),
            ("お気に入りに追加", "star"),
            ("削除", "delete"),
        ]

        for action_text, icon in actions:
            item = TwoLineListItem(
                text=action_text,
                secondary_text="タップしてアクションを実行",
                on_release=lambda x, txt=action_text: self.on_action_selected(txt)
            )
            list_widget.add_widget(item)

        scroll.add_widget(list_widget)
        content.add_widget(scroll)

        sheet.add_widget(content)

        return sheet

    def create_standard_sheet(self):
        """
        スタンダードボトムシートを作成

        Returns:
            MDBottomSheet: スタンダードボトムシート
        """
        # MDBottomSheet作成（スタンダードタイプ）
        sheet = MDBottomSheet(
            size_hint_y=None,
            height=dp(320),
            type="standard",  # スタンダードタイプ（背景操作可能）
            radius=[dp(16), dp(16), 0, 0],
        )

        # ドラッグハンドル
        drag_handle = MDBottomSheetDragHandle()

        # タイトル
        handle_title = MDBottomSheetDragHandleTitle(
            text="スタンダードボトムシート",
            pos_hint={"center_y": 0.5}
        )
        drag_handle.add_widget(handle_title)

        # 閉じるボタン
        close_button = MDBottomSheetDragHandleButton(
            icon="close",
            on_release=lambda x: sheet.dismiss()
        )
        drag_handle.add_widget(close_button)

        sheet.add_widget(drag_handle)

        # コンテンツ部分
        content = MDBoxLayout(
            orientation="vertical",
            padding=[dp(16), 0, dp(16), dp(16)],
            spacing=dp(10)
        )

        # 説明テキスト
        info_label = MDLabel(
            text="これはスタンダードボトムシートです。\n背景のUIも操作できます。",
            halign="center",
            font_name="Roboto",
            size_hint_y=None,
            height=dp(60)
        )
        content.add_widget(info_label)

        # 情報リスト
        scroll = MDScrollView(size_hint=(1, 1))
        list_widget = MDList()

        info_items = [
            "補助情報1: ここに詳細情報を表示",
            "補助情報2: フィルター設定など",
            "補助情報3: 追加オプション",
        ]

        for info_text in info_items:
            item = OneLineListItem(
                text=info_text,
                on_release=lambda x, txt=info_text: self.on_info_selected(txt)
            )
            list_widget.add_widget(item)

        scroll.add_widget(list_widget)
        content.add_widget(scroll)

        sheet.add_widget(content)

        return sheet

    def open_modal_sheet(self, instance):
        """
        モーダルボトムシートを開く

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.result_label.text = "モーダルボトムシートを開きました"
        self.modal_sheet.open()

    def open_standard_sheet(self, instance):
        """
        スタンダードボトムシートを開く

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.result_label.text = "スタンダードボトムシートを開きました"
        self.standard_sheet.open()

    def on_action_selected(self, action_text):
        """
        モーダルシートのアクションが選択された

        Args:
            action_text: 選択されたアクション名
        """
        self.result_label.text = f"アクション「{action_text}」が選択されました"
        self.modal_sheet.dismiss()

    def on_info_selected(self, info_text):
        """
        スタンダードシートの情報が選択された

        Args:
            info_text: 選択された情報
        """
        self.result_label.text = f"「{info_text}」が選択されました"


def main():
    """アプリケーションのエントリーポイント"""
    # デスクトップ実行時のウィンドウサイズ設定
    Window.size = (360, 640)

    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )

    # アプリケーションの起動
    BottomSheetApp().run()


if __name__ == '__main__':
    main()
