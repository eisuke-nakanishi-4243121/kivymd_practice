#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
04_dialogs.py - MDDialogを使ったダイアログ

このサンプルでは、MDDialogの使い方を学びます。
- シンプルなアラートダイアログ
- ボタン付き確認ダイアログ
- カスタムコンテンツを含むダイアログ
- open() / dismiss()メソッド

実行方法:
    python examples/04_dialogs.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.core.text import LabelBase
from kivy.core.window import Window


class DialogsApp(MDApp):
    """
    ダイアログのサンプルアプリケーション

    様々な種類のダイアログの表示方法を学びます。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ダイアログオブジェクトを保持する変数
        self.dialog = None

    def build(self):
        """
        UIを構築するメソッド

        3種類のダイアログを表示するボタンを配置します。

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # 縦方向にボタンを並べるレイアウト
        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # タイトルラベル
        title_label = MDLabel(
            text="ダイアログサンプル",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.2
        )
        layout.add_widget(title_label)

        # シンプルなアラートダイアログを表示するボタン
        alert_button = MDRaisedButton(
            text="アラートダイアログ",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_alert_dialog
        )
        layout.add_widget(alert_button)

        # 確認ダイアログを表示するボタン
        confirm_button = MDRaisedButton(
            text="確認ダイアログ",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_confirm_dialog
        )
        layout.add_widget(confirm_button)

        # カスタムコンテンツダイアログを表示するボタン
        custom_button = MDRaisedButton(
            text="カスタムダイアログ",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_custom_dialog
        )
        layout.add_widget(custom_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="ダイアログのボタンを押してください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.3
        )
        layout.add_widget(self.result_label)

        return layout

    def show_alert_dialog(self, instance):
        """
        シンプルなアラートダイアログを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        # 既存のダイアログがあれば閉じる
        if self.dialog:
            self.dialog.dismiss()

        # MDDialog作成
        # title: ダイアログのタイトル
        # text: メッセージ本文
        # buttons: ダイアログ下部のボタンリスト
        self.dialog = MDDialog(
            title="お知らせ",
            text="これはシンプルなアラートダイアログです。",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_press=self.close_alert_dialog
                ),
            ],
        )
        self.dialog.open()

    def close_alert_dialog(self, instance):
        """
        アラートダイアログを閉じる

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.dialog.dismiss()
        self.result_label.text = "アラートダイアログが閉じられました"

    def show_confirm_dialog(self, instance):
        """
        確認ダイアログを表示（はい/いいえ）

        Args:
            instance: 押されたボタンのインスタンス
        """
        if self.dialog:
            self.dialog.dismiss()

        self.dialog = MDDialog(
            title="確認",
            text="この操作を実行してもよろしいですか？",
            buttons=[
                MDFlatButton(
                    text="キャンセル",
                    on_press=self.cancel_action
                ),
                MDRaisedButton(
                    text="OK",
                    on_press=self.confirm_action
                ),
            ],
        )
        self.dialog.open()

    def cancel_action(self, instance):
        """
        キャンセルボタンが押された

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.dialog.dismiss()
        self.result_label.text = "キャンセルされました"

    def confirm_action(self, instance):
        """
        OKボタンが押された

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.dialog.dismiss()
        self.result_label.text = "操作が実行されました"

    def show_custom_dialog(self, instance):
        """
        カスタムコンテンツを含むダイアログを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        if self.dialog:
            self.dialog.dismiss()

        # カスタムコンテンツ（テキストフィールド）
        content = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint_y=None,
            height=100
        )

        self.name_field = MDTextField(
            hint_text="名前を入力",
            font_name="Roboto"
        )
        content.add_widget(self.name_field)

        self.dialog = MDDialog(
            title="名前入力",
            type="custom",  # カスタムタイプ
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="キャンセル",
                    on_press=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="送信",
                    on_press=self.submit_name
                ),
            ],
        )
        self.dialog.open()

    def submit_name(self, instance):
        """
        名前を送信

        Args:
            instance: 押されたボタンのインスタンス
        """
        name = self.name_field.text
        self.dialog.dismiss()

        if name:
            self.result_label.text = f"こんにちは、{name}さん！"
        else:
            self.result_label.text = "名前が入力されませんでした"


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
    DialogsApp().run()


if __name__ == '__main__':
    main()
