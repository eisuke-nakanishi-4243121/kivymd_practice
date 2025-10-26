#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
02_buttons.py - KivyMDの各種ボタンコンポーネント

このサンプルでは、KivyMDで使用できる様々なボタンを学びます。
- MDRaisedButton（立体ボタン）
- MDFlatButton（フラットボタン）
- MDIconButton（アイコンボタン）
- on_pressイベント処理
- ボタン押下でラベルのテキスト変更

実行方法:
    python practice/02_buttons.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton
from kivy.core.text import LabelBase
from kivy.core.window import Window


class ButtonsApp(MDApp):
    """
    ボタンのサンプルアプリケーション

    3種類のボタン（Raised、Flat、Icon）の使い方と、
    ボタン押下時のイベント処理方法を学びます。
    """

    def build(self):
        """
        UIを構築するメソッド

        縦に並べたレイアウト（MDBoxLayout）の中に、
        ラベルと3種類のボタンを配置します。

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # 縦方向にウィジェットを並べるレイアウト
        # orientation="vertical": 縦方向に配置
        # padding: 外側の余白（20ピクセル）
        # spacing: ウィジェット間の間隔（20ピクセル）
        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # 結果を表示するラベル
        # halign="center": 中央揃え
        # font_name: 日本語フォント
        self.result_label = MDLabel(
            text="ボタンを押してください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.3  # 高さを30%に設定
        )
        layout.add_widget(self.result_label)

        # MDRaisedButton（立体的なボタン）
        # text: ボタンに表示されるテキスト
        # pos_hint: 位置のヒント（中央に配置）
        # size_hint_x: 幅を80%に設定
        # on_press: ボタンが押されたときに呼ばれる関数
        raised_button = MDRaisedButton(
            text="立体ボタン（Raised）",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.on_raised_button_press
        )
        layout.add_widget(raised_button)

        # MDFlatButton（フラットなボタン）
        # テキストのみのシンプルなボタン
        flat_button = MDFlatButton(
            text="フラットボタン（Flat）",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.on_flat_button_press
        )
        layout.add_widget(flat_button)

        # MDIconButton（アイコンボタン）
        # icon: Material Design Iconsのアイコン名
        # アイコン一覧: https://materialdesignicons.com/
        icon_button = MDIconButton(
            icon="heart",  # ハートアイコン
            pos_hint={"center_x": 0.5},
            on_press=self.on_icon_button_press
        )
        layout.add_widget(icon_button)

        # カウンター用の変数を初期化
        self.button_count = 0

        return layout

    def on_raised_button_press(self, instance):
        """
        立体ボタンが押されたときの処理

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.button_count += 1
        self.result_label.text = f"立体ボタンが押されました！\n（{self.button_count}回目）"

    def on_flat_button_press(self, instance):
        """
        フラットボタンが押されたときの処理

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.button_count += 1
        self.result_label.text = f"フラットボタンが押されました！\n（{self.button_count}回目）"

    def on_icon_button_press(self, instance):
        """
        アイコンボタンが押されたときの処理

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.button_count += 1
        self.result_label.text = f"アイコンボタンが押されました！\n（{self.button_count}回目）"


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
    ButtonsApp().run()


if __name__ == '__main__':
    main()
