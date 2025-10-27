#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
14_switch_checkbox.py - MDSwitch/MDCheckboxを使った切り替えUI

このサンプルでは、スイッチとチェックボックスの使い方を学びます。
- MDSwitch（ON/OFF切り替え）
- MDCheckbox（チェックボックス）
- 状態の取得と設定
- イベント処理
- 実践的な使用例（設定画面）

実行方法:
    python practice/14_switch_checkbox.py
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.switch import MDSwitch
from kivymd.uix.checkbox import MDCheckbox
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.divider import MDDivider
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp


class SwitchCheckboxApp(MDApp):
    """
    スイッチ/チェックボックスのサンプルアプリケーション

    設定画面を想定したUIで、ON/OFF切り替えとチェックボックスを実装します。
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 設定の状態を保持
        self.settings = {
            'notifications': False,
            'dark_mode': False,
            'sound': False,
            'auto_update': False,
        }
        # 選択された趣味リスト
        self.selected_hobbies = []

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
            spacing=dp(10)
        )

        # タイトルラベル
        title_label = MDLabel(
            text="スイッチ/チェックボックス",
            halign="center",
            font_name="Roboto",
            font_style="H5",
            size_hint_y=0.1
        )
        main_layout.add_widget(title_label)

        # === 設定セクション（MDSwitch） ===
        settings_label = MDLabel(
            text="設定（スイッチ）",
            halign="left",
            font_name="Roboto",
            font_style="H6",
            size_hint_y=0.06,
            padding=[dp(10), 0]
        )
        main_layout.add_widget(settings_label)

        # スクロール可能なリスト
        scroll = MDScrollView(size_hint_y=0.35)
        settings_list = MDList()

        # 通知設定
        notification_item = self.create_switch_item(
            "通知",
            "notifications",
            "bell"
        )
        settings_list.add_widget(notification_item)

        # ダークモード設定
        darkmode_item = self.create_switch_item(
            "ダークモード",
            "dark_mode",
            "theme-light-dark"
        )
        settings_list.add_widget(darkmode_item)

        # サウンド設定
        sound_item = self.create_switch_item(
            "サウンド",
            "sound",
            "volume-high"
        )
        settings_list.add_widget(sound_item)

        # 自動更新設定
        auto_update_item = self.create_switch_item(
            "自動更新",
            "auto_update",
            "update"
        )
        settings_list.add_widget(auto_update_item)

        scroll.add_widget(settings_list)
        main_layout.add_widget(scroll)

        main_layout.add_widget(MDDivider())

        # === チェックボックスセクション ===
        checkbox_label = MDLabel(
            text="趣味を選択（チェックボックス）",
            halign="left",
            font_name="Roboto",
            font_style="H6",
            size_hint_y=0.06,
            padding=[dp(10), 0]
        )
        main_layout.add_widget(checkbox_label)

        # チェックボックスのグリッド
        checkbox_layout = MDBoxLayout(
            orientation="vertical",
            size_hint_y=0.25,
            spacing=dp(5)
        )

        hobbies = ["読書", "音楽", "スポーツ", "映画", "旅行"]

        for hobby in hobbies:
            hobby_box = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(40),
                spacing=dp(10)
            )

            checkbox = MDCheckbox(
                size_hint=(None, None),
                size=(dp(48), dp(48)),
            )
            checkbox.bind(active=lambda x, value, h=hobby: self.on_checkbox_change(h, value))

            hobby_label = MDLabel(
                text=hobby,
                font_name="Roboto",
                halign="left",
                valign="center"
            )

            hobby_box.add_widget(checkbox)
            hobby_box.add_widget(hobby_label)
            checkbox_layout.add_widget(hobby_box)

        main_layout.add_widget(checkbox_layout)

        # 確認ボタン
        confirm_button = MDRaisedButton(
            text="設定を確認",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
            size_hint_y=0.08,
            on_press=self.show_settings
        )
        main_layout.add_widget(confirm_button)

        # 結果表示ラベル
        self.result_label = MDLabel(
            text="設定を変更してください",
            halign="center",
            font_name="Roboto",
            size_hint_y=0.1
        )
        main_layout.add_widget(self.result_label)

        screen.add_widget(main_layout)

        return screen

    def create_switch_item(self, text, setting_key, icon):
        """
        スイッチ付きリストアイテムを作成

        Args:
            text: 表示テキスト
            setting_key: 設定キー
            icon: アイコン名

        Returns:
            OneLineAvatarIconListItem: リストアイテム
        """
        class SwitchListItem(OneLineAvatarIconListItem):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                # スイッチを追加
                switch = MDSwitch(
                    pos_hint={"center_y": 0.5},
                )
                switch.bind(active=lambda x, value: self.on_switch_change(value))
                self.add_widget(switch)
                self.switch = switch
                self.setting_key = None
                self.app = None

            def on_switch_change(self, value):
                if self.app and self.setting_key:
                    self.app.on_switch_change(self.setting_key, value)

        item = SwitchListItem(text=text)
        item.setting_key = setting_key
        item.app = self

        # アイコンを追加
        icon_widget = IconLeftWidget(icon=icon)
        item.add_widget(icon_widget)

        return item

    def on_switch_change(self, setting_key, value):
        """
        スイッチの状態が変更された

        Args:
            setting_key: 設定キー
            value: 新しい値（True/False）
        """
        self.settings[setting_key] = value
        status = "ON" if value else "OFF"

        setting_names = {
            'notifications': '通知',
            'dark_mode': 'ダークモード',
            'sound': 'サウンド',
            'auto_update': '自動更新'
        }

        self.result_label.text = f"{setting_names.get(setting_key, setting_key)}: {status}"

    def on_checkbox_change(self, hobby, value):
        """
        チェックボックスの状態が変更された

        Args:
            hobby: 趣味の名前
            value: チェック状態（True/False）
        """
        if value and hobby not in self.selected_hobbies:
            self.selected_hobbies.append(hobby)
        elif not value and hobby in self.selected_hobbies:
            self.selected_hobbies.remove(hobby)

        if self.selected_hobbies:
            hobbies_text = "、".join(self.selected_hobbies)
            self.result_label.text = f"選択: {hobbies_text}"
        else:
            self.result_label.text = "趣味が選択されていません"

    def show_settings(self, instance):
        """
        現在の設定を表示

        Args:
            instance: 押されたボタンのインスタンス
        """
        # スイッチ設定
        on_settings = [k for k, v in self.settings.items() if v]
        settings_text = "なし" if not on_settings else ", ".join([
            {'notifications': '通知', 'dark_mode': 'ダークモード',
             'sound': 'サウンド', 'auto_update': '自動更新'}[k]
            for k in on_settings
        ])

        # チェックボックス選択
        hobbies_text = "なし" if not self.selected_hobbies else "、".join(self.selected_hobbies)

        self.result_label.text = f"ON設定: {settings_text}\n選択趣味: {hobbies_text}"


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
    SwitchCheckboxApp().run()


if __name__ == '__main__':
    main()
