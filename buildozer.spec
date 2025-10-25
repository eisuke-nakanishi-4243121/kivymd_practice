[app]

# アプリケーション名（ホーム画面に表示される名前）
title = KivyMD Practice

# パッケージ名
package.name = kivymdpractice

# パッケージドメイン
package.domain = org.morijyobi

# ソースコードのディレクトリ
source.dir = .

# ソースコードに含める拡張子
source.include_exts = py,png,jpg,kv,atlas,ttc,ttf,otf

# ソースコードから除外するパターン
source.exclude_dirs = tests, bin, venv, __pycache__

# バージョン情報
version = 0.1

# 必要なPythonパッケージ（Kivy 2.2.1 + KivyMD）
requirements = python3,kivy==2.2.1,kivymd

# 画面の向き（portrait=縦、landscape=横、all=両方）
orientation = portrait

# アプリアイコン（未設定の場合はデフォルト）
#icon.filename = %(source.dir)s/assets/images/icon.png

# プレスプラッシュ画像（起動時の画面）
#presplash.filename = %(source.dir)s/assets/images/presplash.png

# Androidパーミッション
android.permissions = INTERNET

# Android APIバージョン
android.api = 31

# Android NDKバージョン（推奨: 25b）
android.ndk = 25b

# 最小SDKバージョン
android.minapi = 21

# ターゲットSDKバージョン
android.sdk = 31

# Android アーキテクチャ（armeabi-v7a, arm64-v8a, x86, x86_64）
android.archs = arm64-v8a,armeabi-v7a

# フルスクリーン表示
fullscreen = 0

# ログレベル（0=なし、1=エラー、2=警告、3=情報、4=デバッグ）
log_level = 2

# Warningを非表示にする
warn_on_root = 1


[buildozer]

# ビルドディレクトリ
log_level = 2

# 警告を非表示
warn_on_root = 1
