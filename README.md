# GeoDjango ORM Demo


## Overview
- This is an application to check Spatial Functions and GeoDjango ORM
- 空間関数とGeoDjangoORM確認用アプリケーション

---

## Docker version
```sh
docker version --format '{{.Server.Version}}'
20.10.11
```

---

## Installation
```sh
# edit .env
cp ./geodjango/.env.sample ./geodjango/.env
vi ./geodjango/.env

cp ./postgres/.env.db.sample ./postgres/.env.db
vi ./postgres/.env.db


docker compose up --build -d
```

---

## Command
### create superuser
```sh
docker container exec -it geodjango_orm python3 manage.py createsuperuser
```

### import Shapefile
```sh
docker container exec -it geodjango_orm python3 manage.py shell -c "from world import load; load.main()"
```

---

## Usage
- データ取り込み後、以下にアクセスするとトップページに遷移  
http://localhost:8000/
- `Spatial Funciton`で実行したい空間関数、`Airport`で対象の空港を選択し、`Run`をクリック
- 空港ポリゴンに対して、空間関数を実行した結果がフロントに描画される
- `Jump Endpoint`をクリックすると、Browsable APIの画面に遷移
- Django Debug Toolberから、実行されたSQLおよびパフォーマンスが確認可能

---

## Style
- [MapTiler](https://maptiler.jp/)スタイルの地図を表示する場合は、`geodjango/world/static/world/js/app.js`の`[Maptiler API key]`を有効なAPIキーに更新
```js
const maptiler = L.tileLayer(
    'https://api.maptiler.com/maps/jp-mierune-streets/{z}/{x}/{y}.png?key=[Maptiler API key]',
);
```

---

## Data
国土数値情報 ダウンロードサービス - http://nlftp.mlit.go.jp/ksj/index.html

- 国土交通省国土政策局「国土数値情報（行政区域データ）」北海道 令和4年 (N03-20220101_01_GML.zip)  
https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html

- 国土交通省国土政策局「国土数値情報（空港データ）」令和3年(C28-21_GML.zip)  
https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-C28-v3_0.html
