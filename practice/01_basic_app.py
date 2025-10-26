#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
01_basic_app.py - 基本的なKivyMDアプリケーション

このサンプルでは、KivyMDアプリケーションの最も基本的な構造を学びます。
- MDAppクラスの継承
- build()メソッドの実装
- MDLabelを使った中央テキスト表示
- ウィンドウサイズの設定
- 日本語フォントの登録と使用

実行方法:
    python practice/01_basic_app.py
"""

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivy.core.window import Window


class BasicApp(MDApp):
    """
    基本的なKivyMDアプリケーションクラス

    MDAppクラスを継承して、独自のアプリケーションを作成します。
    build()メソッドでUIを構築し、返されたウィジェットがルートウィジェットになります。
    """

    def build(self):
        """
        UIを構築するメソッド

        このメソッドで返されたウィジェットが、アプリケーションのルートウィジェットになります。
        ここでは、中央に「KivyMDへようこそ！」と表示するシンプルなラベルを返しています。

        Returns:
            MDLabel: ルートウィジェット（中央にテキストを表示するラベル）
        """
        # アプリのテーマ設定
        self.theme_cls.primary_palette = "Blue"  # プライマリカラー（青）
        self.theme_cls.accent_palette = "Amber"  # アクセントカラー（琥珀色）
        self.theme_cls.theme_style = "Light"     # ライトテーマ（"Dark"でダークテーマ）

        # MDLabelを作成して返す
        # halign="center": 水平方向の配置を中央に
        # text: 表示するテキスト（日本語対応）
        # font_name: 使用するフォント名（日本語フォントを指定）
        return MDLabel(
            text="KivyMDへようこそ！\n\nこれは最も基本的なMDAppの例です。",
            halign="center"
        )


def main():
    """
    アプリケーションのエントリーポイント

    日本語フォントを登録してから、アプリケーションを起動します。
    """
    # デスクトップ実行時のウィンドウサイズを設定（幅360px × 高さ640px）
    # スマートフォンの縦画面をシミュレート
    Window.size = (360, 640)

    # 日本語フォントの登録
    # デフォルトフォント（Roboto）を日本語フォントで上書き
    # KivyMD 1.2.0 では個別ウィジェットに font_name を指定できないため、
    # デフォルトフォントを置き換えることで日本語を表示する
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/NotoSansCJKjp-Regular.otf'
    )

    # BasicAppクラスのインスタンスを作成して実行
    BasicApp().run()


# このスクリプトが直接実行された場合のみmain()を呼び出す
if __name__ == '__main__':
    main()
