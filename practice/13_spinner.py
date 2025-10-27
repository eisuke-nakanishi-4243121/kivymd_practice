#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
13_spinner.py - MDSpinner/MDProgressBarを使ったローディング表示

このサンプルでは、スピナーとプログレスバーの使い方を学びます。
- MDSpinner（円形スピナー）
- MDLinearProgressIndicator（線形プログレスバー）
- MDCircularProgressIndicator（円形プログレスインジケーター）
- 確定/不確定プログレス
- プログレスの更新

実行方法:
    python practice/13_spinner.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.progressindicator import MDCircularProgressIndicator
from kivymd.uix.progressbar import MDProgressBar
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.animation import Animation


class SpinnerApp(MDApp):
    """
    スピナー/プログレスバーのサンプルアプリケーション

    ローディング表示の様々なパターンを実装します。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.progress_event = None
        self.current_progress = 0

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
            text="スピナー/プログレスバー",
            halign="center",
            font_name="Roboto",
            font_style="H5",
            size_hint_y=0.1
        )
        main_layout.add_widget(title_label)

        # 説明ラベル
        desc_label = MDLabel(
            text="ローディング表示のサンプル",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.08
        )
        main_layout.add_widget(desc_label)

        # === 円形スピナー（MDSpinner） ===
        spinner_label = MDLabel(
            text="円形スピナー（MDSpinner）",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.06
        )
        main_layout.add_widget(spinner_label)

        self.spinner = MDSpinner(
            size_hint=(None, None),
            size=(dp(46), dp(46)),
            pos_hint={'center_x': 0.5},
            active=False,  # 初期状態は非表示
        )
        main_layout.add_widget(self.spinner)

        # スピナー切り替えボタン
        spinner_button = MDRaisedButton(
            text="スピナーを表示/非表示",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            size_hint_y=0.08,
            on_press=self.toggle_spinner
        )
        main_layout.add_widget(spinner_button)

        # === 線形プログレスバー（MDProgressBar） ===
        linear_label = MDLabel(
            text="線形プログレスバー",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.06
        )
        main_layout.add_widget(linear_label)

        self.linear_progress = MDProgressBar(
            size_hint_x=0.9,
            pos_hint={'center_x': 0.5},
            size_hint_y=None,
            height=dp(4),
            value=0,
        )
        main_layout.add_widget(self.linear_progress)

        # プログレスバー開始ボタン
        progress_button = MDRaisedButton(
            text="プログレスバーを開始",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            size_hint_y=0.08,
            on_press=self.start_linear_progress
        )
        main_layout.add_widget(progress_button)

        # === 円形プログレスインジケーター ===
        circular_label = MDLabel(
            text="円形プログレスインジケーター",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.06
        )
        main_layout.add_widget(circular_label)

        self.circular_progress = MDCircularProgressIndicator(
            size_hint=(None, None),
            size=(dp(48), dp(48)),
            pos_hint={'center_x': 0.5},
        )
        main_layout.add_widget(self.circular_progress)

        # 円形プログレス開始ボタン
        circular_button = MDRaisedButton(
            text="円形プログレスを開始",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            size_hint_y=0.08,
            on_press=self.start_circular_progress
        )
        main_layout.add_widget(circular_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="ボタンを押してローディング表示を試してください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.12
        )
        main_layout.add_widget(self.result_label)

        screen.add_widget(main_layout)

        return screen

    def toggle_spinner(self, instance):
        """
        スピナーの表示/非表示を切り替え

        Args:
            instance: 押されたボタンのインスタンス
        """
        self.spinner.active = not self.spinner.active

        if self.spinner.active:
            self.result_label.text = "スピナーを表示中..."
        else:
            self.result_label.text = "スピナーを非表示にしました"

    def start_linear_progress(self, instance):
        """
        線形プログレスバーを開始

        Args:
            instance: 押されたボタンのインスタンス
        """
        # 既存のイベントをキャンセル
        if self.progress_event:
            self.progress_event.cancel()

        # プログレスをリセット
        self.current_progress = 0
        self.linear_progress.value = 0

        self.result_label.text = "線形プログレスバーを開始しました（0%）"

        # 0.05秒ごとにプログレスを更新
        self.progress_event = Clock.schedule_interval(self.update_linear_progress, 0.05)

    def update_linear_progress(self, dt):
        """
        線形プログレスバーの値を更新

        Args:
            dt: delta time
        """
        self.current_progress += 1
        progress_percent = self.current_progress

        self.linear_progress.value = progress_percent
        self.result_label.text = f"線形プログレス: {progress_percent}%"

        # 100%に達したら停止
        if progress_percent >= 100:
            if self.progress_event:
                self.progress_event.cancel()
                self.progress_event = None
            self.result_label.text = "線形プログレス: 完了！"

    def start_circular_progress(self, instance):
        """
        円形プログレスインジケーターを開始（アニメーション）

        Args:
            instance: 押されたボタンのインスタンス
        """
        # 0から100までアニメーション（5秒間）
        self.circular_progress.determinate = True

        # アニメーションをリセット
        Animation.cancel_all(self.circular_progress)
        self.circular_progress.determinate_value = 0

        # アニメーション作成
        anim = Animation(determinate_value=100, duration=5)
        anim.bind(on_progress=self.update_circular_progress)
        anim.bind(on_complete=self.circular_progress_complete)
        anim.start(self.circular_progress)

        self.result_label.text = "円形プログレスを開始しました（0%）"

    def update_circular_progress(self, animation, widget, progression):
        """
        円形プログレスの進行状況を表示

        Args:
            animation: アニメーションオブジェクト
            widget: ウィジェット
            progression: 進行度（0.0-1.0）
        """
        percent = int(progression * 100)
        self.result_label.text = f"円形プログレス: {percent}%"

    def circular_progress_complete(self, animation, widget):
        """
        円形プログレスが完了した

        Args:
            animation: アニメーションオブジェクト
            widget: ウィジェット
        """
        self.result_label.text = "円形プログレス: 完了！"


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
    SpinnerApp().run()


if __name__ == '__main__':
    main()
