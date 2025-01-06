# 🧺api-test-django

## 実行
`rye run python src/manage.py runserver`

## 手順

- `python manage.py startapp costdates`でNEWアプリ追加
- `models.py`にテーブル定義作成
- マイグレーションを作成
  - `python manage.py makemigrations`
  - `python manage.py migrate`で適用する
  - `python manage.py showmigrations`で適用状態確認
  - DBはsrc配下で`sqlite3 db.sqlite3`
    - テーブル一覧は`.tables`で確認
- `admin.py`追加
- `serializers.py`にシリアライザー作成
- `views.py`にAPI処理を実装
- API呼び出しURLを`urls.py`に追加

## ✏️メモ

- Django
  - SQLを書かなくてもDBを操作できるフレームワーク
  - models.pyでデータベースの構造をPythonのクラスとして定義する
  - マイグレーションを実行すると、モデルに基にデータベースが更新される
