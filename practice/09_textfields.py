#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
09_textfields.py - MDTextFieldを使ったテキスト入力

このサンプルでは、MDTextFieldの使い方を学びます。
- 通常のテキスト入力
- パスワード入力（password: True）
- ヘルパーテキスト、エラー表示
- バリデーション例（ログイン画面想定）

実行方法:
    python practice/09_textfields.py
"""

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.core.text import LabelBase
from kivy.core.window import Window


class TextFieldsApp(MDApp):
    """
    テキストフィールドのサンプルアプリケーション

    様々なスタイルのテキスト入力フィールドと、
    バリデーション（入力検証）の実装方法を学びます。
    """

    def build(self):
        """
        UIを構築するメソッド

        ログイン画面風のUIを作成します。

        Returns:
            MDBoxLayout: ルートウィジェット
        """
        # テーマ設定
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        # メインレイアウト
        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # タイトルラベル
        title_label = MDLabel(
            text="ログイン画面",
            halign="center",
            font_name="Roboto",
            font_size=24,
            size_hint_y=0.2
        )
        layout.add_widget(title_label)

        # ユーザー名入力フィールド
        # hint_text: プレースホルダー（入力がないときに表示されるヒント）
        # helper_text: 補助テキスト
        # helper_text_mode: 補助テキストの表示モード
        #   - "on_focus": フォーカス時に表示
        #   - "persistent": 常に表示
        #   - "on_error": エラー時に表示
        self.username_field = MDTextField(
            hint_text="ユーザー名",
            helper_text="学籍番号を入力してください",
            helper_text_mode="on_focus",
            font_name="Roboto",
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.username_field)

        # パスワード入力フィールド
        # password: True にするとパスワード入力（●で表示）
        self.password_field = MDTextField(
            hint_text="パスワード",
            helper_text="8文字以上で入力してください",
            helper_text_mode="on_focus",
            password=True,
            font_name="Roboto",
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.password_field)

        # メールアドレス入力フィールド（オプション）
        self.email_field = MDTextField(
            hint_text="メールアドレス（オプション）",
            helper_text="例: user@example.com",
            helper_text_mode="on_focus",
            font_name="Roboto",
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.email_field)

        # ログインボタン
        login_button = MDRaisedButton(
            text="ログイン",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            on_press=self.on_login_press
        )
        layout.add_widget(login_button)

        # クリアボタン
        clear_button = MDRaisedButton(
            text="クリア",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
            on_press=self.on_clear_press
        )
        layout.add_widget(clear_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.3
        )
        layout.add_widget(self.result_label)

        return layout

    def on_login_press(self, instance):
        """
        ログインボタンが押されたときの処理

        入力内容をバリデーション（検証）します。

        Args:
            instance: 押されたボタンのインスタンス
        """
        username = self.username_field.text
        password = self.password_field.text
        email = self.email_field.text

        # バリデーション
        errors = []

        # ユーザー名チェック
        if not username:
            self.username_field.error = True
            self.username_field.helper_text = "ユーザー名は必須です"
            errors.append("ユーザー名")
        else:
            self.username_field.error = False
            self.username_field.helper_text = "学籍番号を入力してください"

        # パスワードチェック
        if not password:
            self.password_field.error = True
            self.password_field.helper_text = "パスワードは必須です"
            errors.append("パスワード")
        elif len(password) < 8:
            self.password_field.error = True
            self.password_field.helper_text = "パスワードは8文字以上で入力してください"
            errors.append("パスワード（短すぎ）")
        else:
            self.password_field.error = False
            self.password_field.helper_text = "8文字以上で入力してください"

        # メールアドレスチェック（オプション）
        if email and "@" not in email:
            self.email_field.error = True
            self.email_field.helper_text = "正しいメールアドレスを入力してください"
            errors.append("メールアドレス")
        else:
            self.email_field.error = False
            self.email_field.helper_text = "例: user@example.com"

        # 結果表示
        if errors:
            self.result_label.text = f"エラー: {', '.join(errors)}"
        else:
            self.result_label.text = f"ログイン成功！\nユーザー名: {username}"

    def on_clear_press(self, instance):
        """
        クリアボタンが押されたときの処理

        すべての入力フィールドをクリアします。

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.username_field.text = ""
        self.password_field.text = ""
        self.email_field.text = ""
        self.result_label.text = ""

        # エラー状態もリセット
        self.username_field.error = False
        self.password_field.error = False
        self.email_field.error = False


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
    TextFieldsApp().run()


if __name__ == '__main__':
    main()
