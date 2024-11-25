# todo-server

- [client リポジトリ](https://github.com/pisces2336/todo-client)

## 概要

- djangorestframework で作成した todo アプリのサーバーサイドリポジトリです。

## 大変だったところ

- カスタムユーザー周りの実装に時間がかかってしまった

## こだわったところ

- ModelViewSet を活用して簡潔なルーティングを目指した
- 必要に応じて APIView を用いてエンドポイントを分けことで、必要十分な構成を目指した
- モデルは非常に少ないものの、select_related を用いて N+1 問題への対応を行った
