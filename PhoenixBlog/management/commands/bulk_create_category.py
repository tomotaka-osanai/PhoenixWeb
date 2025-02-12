from django.core.management.base import BaseCommand
from PhoenixBlog.models import Category
from django.db import connection

class Command(BaseCommand):
    help = 'Insert category data for PhoenixBlog'

    def handle(self, *args, **options):
        self.stdout.write("カテゴリー登録処理開始")

        # 存データを削除する
        self.stdout.write("既存データ削除開始")
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE "PhoenixBlog_category";')
        self.stdout.write("既存データ削除完了")

        # 新規データ登録
        self.stdout.write("新規データ登録開始")
        objs = [
            Category(id='1', category_name='生活雑貨'),
            Category(id='2', category_name='家電'),
            Category(id='3', category_name='パソコン・周辺機器'),
            Category(id='4', category_name='カメラ'),
            Category(id='5', category_name='ビューティー・ヘルス'),
            Category(id='6', category_name='コスメ・化粧品'),
            Category(id='7', category_name='コンタクトレンズ'),
            Category(id='8', category_name='食品'),
            Category(id='9', category_name='ドリンク・お酒'),
            Category(id='10', category_name='キッチン用品'),
            Category(id='11', category_name='ファッション'),
            Category(id='12', category_name='靴・シューズ'),
            Category(id='13', category_name='腕時計・アクセサリー'),
            Category(id='14', category_name='ベビー・キッズ・マタニティ'),
            Category(id='15', category_name='インテリア・家具'),
            Category(id='16', category_name='趣味・ホビー'),
            Category(id='17', category_name='アウトドア・キャンプ'),
            Category(id='18', category_name='DIY・工具・エクステリア'),
            Category(id='19', category_name='スポーツ用品'),
            Category(id='20', category_name='釣具・釣り用品'),
            Category(id='21', category_name='ペットフード ・ ペット用品'),
            Category(id='22', category_name='本・CD・DVD'),
            Category(id='23', category_name='テレビゲーム・周辺機器'),
            Category(id='24', category_name='車・バイク'),
            Category(id='25', category_name='ギフト・プレゼント'),
            Category(id='26', category_name='住宅設備・リフォーム'),
            Category(id='27', category_name='スマホ・携帯電話'),
            Category(id='28', category_name='インターネット回線モバイルWi-Fiルーター、ホームルーター、国内レンタルWi-Fi'),
            Category(id='29', category_name='格安SIM'),
            Category(id='30', category_name='投資・資産運用'),
            Category(id='31', category_name='クレジットカード・キャッシュレス決済'),
            Category(id='32', category_name='ローン・借入'),
            Category(id='33', category_name='保険'),
            Category(id='34', category_name='曲'),
            Category(id='35', category_name='アプリ'),
            Category(id='36', category_name='サービス'),
            Category(id='37', category_name='その他'),
        ]
        Category.objects.bulk_create(objs)
        self.stdout.write("新規データ登録完了")
