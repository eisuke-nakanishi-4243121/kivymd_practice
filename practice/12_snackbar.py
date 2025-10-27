#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
12_snackbar.py - MDSnackbarを使った通知メッセージ

このサンプルでは、MDSnackbarの使い方を学びます。
- シンプルなスナックバー
- アクション付きスナックバー
- 位置とスタイルのカスタマイズ
- 自動消去と手動消去

実行方法:
    python practice/12_snackbar.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.snackbar import MDSnackbarSupportingText, MDSnackbarButtonContainer
from kivymd.uix.snackbar import MDSnackbarCloseButton, MDSnackbarActionButton
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class SnackbarApp(MDApp):
    """
    スナックバーのサンプルアプリケーション

    様々なスタイルのスナックバー（通知メッセージ）を実装します。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 現在表示中のスナックバーを保持
        self.current_snackbar = None

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
            spacing=dp(15)
        )

        # タイトルラベル
        title_label = MDLabel(
            text="スナックバーサンプル",
            halign="center",
            font_name="Roboto",
            font_style="H5",
            size_hint_y=0.15
        )
        main_layout.add_widget(title_label)

        # 説明ラベル
        desc_label = MDLabel(
            text="各種通知メッセージを表示できます",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.1
        )
        main_layout.add_widget(desc_label)

        # シンプルなスナックバーボタン
        simple_button = MDRaisedButton(
            text="シンプルな通知",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_simple_snackbar
        )
        main_layout.add_widget(simple_button)

        # 長いメッセージのスナックバーボタン
        long_button = MDRaisedButton(
            text="長いメッセージ通知",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_long_snackbar
        )
        main_layout.add_widget(long_button)

        # アクション付きスナックバーボタン
        action_button = MDRaisedButton(
            text="アクション付き通知",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_action_snackbar
        )
        main_layout.add_widget(action_button)

        # 閉じるボタン付きスナックバーボタン
        close_button = MDRaisedButton(
            text="閉じるボタン付き通知",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_close_snackbar
        )
        main_layout.add_widget(close_button)

        # 成功メッセージボタン
        success_button = MDRaisedButton(
            text="成功メッセージ",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_success_snackbar
        )
        main_layout.add_widget(success_button)

        # エラーメッセージボタン
        error_button = MDRaisedButton(
            text="エラーメッセージ",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            on_press=self.show_error_snackbar
        )
        main_layout.add_widget(error_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="ボタンを押して通知を表示してください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.2
        )
        main_layout.add_widget(self.result_label)

        screen.add_widget(main_layout)

        return screen

    def close_current_snackbar(self):
        """現在表示中のスナックバーを閉じる"""
        if self.current_snackbar:
            self.current_snackbar.dismiss()
            self.current_snackbar = None

    def show_simple_snackbar(self, instance):
        """
        シンプルなスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # シンプルなスナックバー
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="これはシンプルな通知です",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=3,  # 3秒後に自動で消える
        )
        self.current_snackbar.open()
        self.result_label.text = "シンプルな通知を表示しました"

    def show_long_snackbar(self, instance):
        """
        長いメッセージのスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # 長いメッセージのスナックバー
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="データの保存が完了しました",
            ),
            MDSnackbarSupportingText(
                text="変更内容はすべて正常に保存されました。次回起動時に反映されます。",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=4,
        )
        self.current_snackbar.open()
        self.result_label.text = "長いメッセージの通知を表示しました"

    def show_action_snackbar(self, instance):
        """
        アクション付きスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # アクションボタンのコンテナ
        button_container = MDSnackbarButtonContainer()
        action_btn = MDSnackbarActionButton(
            text="元に戻す",
            on_release=self.on_snackbar_action
        )
        button_container.add_widget(action_btn)

        # アクション付きスナックバー
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="アイテムを削除しました",
            ),
            button_container,
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=5,
        )
        self.current_snackbar.open()
        self.result_label.text = "アクション付き通知を表示しました"

    def show_close_snackbar(self, instance):
        """
        閉じるボタン付きスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # 閉じるボタンのコンテナ
        button_container = MDSnackbarButtonContainer()
        close_btn = MDSnackbarCloseButton(
            icon="close",
            on_release=lambda x: self.current_snackbar.dismiss()
        )
        button_container.add_widget(close_btn)

        # 閉じるボタン付きスナックバー
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="この通知は手動で閉じることができます",
            ),
            button_container,
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=0,  # 0 = 自動で消えない
        )
        self.current_snackbar.open()
        self.result_label.text = "閉じるボタン付き通知を表示しました"

    def show_success_snackbar(self, instance):
        """
        成功メッセージのスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # 成功メッセージ（緑色）
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="✓ 操作が正常に完了しました",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=3,
            md_bg_color=(0.2, 0.7, 0.3, 1),  # 緑色の背景
        )
        self.current_snackbar.open()
        self.result_label.text = "成功メッセージを表示しました"

    def show_error_snackbar(self, instance):
        """
        エラーメッセージのスナックバーを表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.close_current_snackbar()

        # エラーメッセージ（赤色）
        self.current_snackbar = MDSnackbar(
            MDSnackbarText(
                text="✗ エラーが発生しました",
            ),
            MDSnackbarSupportingText(
                text="もう一度お試しください。",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            duration=4,
            md_bg_color=(0.8, 0.2, 0.2, 1),  # 赤色の背景
        )
        self.current_snackbar.open()
        self.result_label.text = "エラーメッセージを表示しました"

    def on_snackbar_action(self, instance):
        """
        スナックバーのアクションボタンが押された

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.result_label.text = "「元に戻す」アクションが実行されました"
        if self.current_snackbar:
            self.current_snackbar.dismiss()


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
    SnackbarApp().run()


if __name__ == '__main__':
    main()
