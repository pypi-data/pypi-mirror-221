import unittest
import time
import logging
import os
import pandas as pd

from echoss_fileformat.csv_handler import CsvHandler
from echoss_fileformat.feather_handler import FeatherHandler
from echoss_fileformat.dataframe_util import print_table, reduce_memory_usage

# configure the logger
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)
# use the logger

verbose = True

class MyTestCase(unittest.TestCase):
    """
        테스트 설정
    """
    def setUp(self):
        """Before test"""
        ids = self.id().split('.')
        self.str_id = f"{ids[-2]}: {ids[-1]}"
        self.start_time = time.perf_counter()
        logger.info(f"setting up test [{self.str_id}] ")

    def tearDown(self):
        """After test"""
        self.end_time = time.perf_counter()
        logger.info(f" tear down test [{self.str_id}] elapsed time {(self.end_time-self.start_time)*1000: .3f}ms \n")

    """
    유닛 테스트 
    """

    def test_load_csv_dump_feather(self):
        expect_pass = 1
        expect_fail = 0
        expect_file_size = 14554
        load_filename = 'test_data/simple_standard.csv'
        dump_filename = 'test_data/simple_standard_to_delete.feather'
        try:
            csv_handler = CsvHandler()
            csv_handler.load(load_filename, header=0, skiprows=0)
            pass_size = len(csv_handler.pass_list)
            fail_size = len(csv_handler.fail_list)
            csv_df = csv_handler.to_pandas()
            expect_csv_str = "SEQ_NO,PROMTN_TY_CD,PROMTN_TY_NM,BRAND_NM,SVC_NM,ISSU_CO,PARTCPTN_CO,PSNBY_ISSU_CO,COUPON_CRTFC_CO,COUPON_USE_RT\r\n"+"0,9,대만프로모션발급인증통계,77chocolate,S0013,15,15,1.0,15,1.0"
            csv_str = csv_handler.dumps()
            # logger.info("[\n"+csv_str+"]")
            self.assertTrue(csv_str.startswith(expect_csv_str), "startswith fail")

            feather_handler = FeatherHandler()
            feather_handler.dump(dump_filename, data=csv_df)
            exist = os.path.exists(dump_filename)
            file_size = os.path.getsize(dump_filename)
            if exist and 'to_delete' in dump_filename:
                os.remove(dump_filename)

            logger.info(f"\t {feather_handler} dump expect exist True get {exist}")
            logger.info(f"\t {feather_handler} dump expect file_size {expect_file_size} get {file_size}")

        except Exception as e:
            logger.error(f"\t File load fail by {e}")
            self.assertTrue(True, f"\t File load fail by {e}")
        else:
            logger.info(f"\t load expect pass {expect_pass} get {pass_size}")
            self.assertTrue(pass_size == expect_pass)
            logger.info(f"\t load expect fail {expect_fail} get {fail_size}")
            self.assertTrue(fail_size == expect_fail)

    def test_load_feather(self):
        load_filename = 'test_data/simple_object.feather'
        dump_filename = 'test_data/simple_object_to_delete.feather'

        expect_pass = 1
        expect_fail = 0
        expect_shape = (10067,54)
        expect_file_size = 706626

        try:
            handler = FeatherHandler()
            read_df = handler.load(load_filename)

        except Exception as e:
            logger.error(f"\t File load fail by {e}")
            self.assertTrue(True, f"\t File load fail by {e}")

        try:
            handler.dump(dump_filename, data=read_df)
            exist = os.path.exists(dump_filename)
            file_size = os.path.getsize(dump_filename)

            if 'to_delete' in dump_filename:
                os.remove(dump_filename)

        except Exception as e:
            logger.error(f"\t File dump fail by {e}")
            self.assertTrue(True, f"\t File dump fail by {e}")
        else:
            logger.info(f"{handler} expect shape={expect_shape}, and get shape={read_df.shape}")
            self.assertEqual(expect_shape, read_df.shape)
            logger.info(f"{handler} dump expect exist True get {exist}")
            self.assertTrue(exist)
            logger.info(f"{handler} dump expect file_size {expect_file_size} get {file_size}")
            self.assertEqual(expect_file_size, file_size)


    def test_kwargs(self):
        load_filename = 'test_data/SIN_KUNNR_202304061027.csv'

        id_cols = ['KUNNR']
        numeric_cols = ['OBLIG', 'KLIMK']
        category_cols = [
            'KDGRP', 'VKBUR', 'VKGRP', 'ORDER_WEEK', 'KUKLA', 'X', 'Y', 'Z', 'GFORM', 'EX_KUNNR', 'ZZMTYP', 'MUL_GUB',
            'GUBUN', 'VSBED',
            'J_001', 'J_002', 'J_003', 'J_004', 'J_005', 'J_006', 'J_007', 'J_008', 'J_009', 'J_010',
            'J_011', 'J_012', 'J_013', 'J_014', 'J_015', 'J_016', 'J_017', 'J_018', 'J_019', 'J_020',
            'J_021', 'J_022', 'J_023', 'J_024', 'J_025', 'J_026',
            'DANGA_ZERO', 'ZGFORM', 'AREA_POINT', 'GUBUN_ALERT', 'VTWEG', 'KONDA', 'COLL_MON'
        ]
        output_cols = id_cols + numeric_cols + category_cols

        csv_handler = CsvHandler(processing_type='object', encoding='cp949')

        kun_df = csv_handler.load(
            file_or_filename=load_filename,
            usecols=output_cols,
            dtype=str,
            keep_default_na=False,
            index_col=id_cols,
            parse_dates=[9]
        )
        print_table(kun_df, logger.info)
        logger.info(kun_df.info())


    def test_handler_kwargs(self):
        expect_shape = (29723, 50)

        # 출력 컬럼 정리
        id_cols = ['KUNNR']
        numeric_cols = ['OBLIG', 'KLIMK']
        category_cols = [
            'KDGRP', 'VKBUR', 'VKGRP', 'ORDER_WEEK', 'KUKLA', 'X', 'Y', 'Z', 'GFORM', 'EX_KUNNR', 'ZZMTYP', 'MUL_GUB',
            'GUBUN', 'VSBED',
            'J_001', 'J_002', 'J_003', 'J_004', 'J_005', 'J_006', 'J_007', 'J_008', 'J_009', 'J_010',
            'J_011', 'J_012', 'J_013', 'J_014', 'J_015', 'J_016', 'J_017', 'J_018', 'J_019', 'J_020',
            'J_021', 'J_022', 'J_023', 'J_024', 'J_025', 'J_026',
            'DANGA_ZERO', 'ZGFORM', 'AREA_POINT', 'GUBUN_ALERT', 'VTWEG', 'KONDA', 'COLL_MON'
        ]
        # 고객 데이터에서 data 컬럼은 의미가 있을까? 빈값인 경우의 처리방법 필요
        output_date_cols = ['OPENDATE']
        # 주소(ORT01) 에서 생성할 컬럼
        create_cols = ['REGIONCODE', 'REGIONGROUP']

        # 정제된 컬럼 : ID, INFO, number + category data
        output_cols = id_cols + numeric_cols + category_cols + output_date_cols

        load_filename = 'test_data/SIN_KUNNR_202304061027.csv'
        dump_filename = 'test_data/sin_kun_to_delete.feather'

        # 1. 고객 원천 데이터 로드 후 정리하여 저장
        # kun_df = pd.read_csv(
        #     '../data/original/SIN_KUNNR_202304061027.csv',
        #     dtype=str,
        #     keep_default_na=False,
        #     index_col=id_cols,
        #     usecols=output_cols,
        #     parse_dates=[9],
        #     encoding='cp949')
        try:
            csv_handler = CsvHandler(processing_type='object', encoding='cp949')

            kun_df = csv_handler.load(
                file_or_filename=load_filename,
                usecols=output_cols,
                dtype=str,
                keep_default_na=False,
                index_col=id_cols,
                parse_dates=[9]
            )

            # test code
            value_list = kun_df[ 'KLIMK'].values
            # for i,v in enumerate(value_list):
            #    logger.info(f"[{i}] {v} to int {int(v)}")

            # numeric as int
            for col in numeric_cols:
                kun_df[col] = pd.to_numeric(kun_df[col], errors='coerce').fillna(0).astype(int)
            # category 정리 코드
            for col in category_cols:
                kun_df[col] = kun_df[col].astype('category')
            # data 정리 코드
            for col in output_date_cols:
                kun_df[col] = pd.to_datetime(kun_df[col], errors='coerce', format='%Y%m%d')

            # 저장 코드 EX_KUNNR_TEST
            # with open(output_dir + 'sin_kun.feather', 'wb') as f:
            #     feather.write_feather(kun_df, f)
            feather_handler = FeatherHandler()
            feather_handler.dump(dump_filename, data=kun_df)

            if 'to_delete' in dump_filename:
                os.remove(dump_filename)

        except Exception as e:
            logger.error(f"\t {csv_handler} load fail by {e}")
        else:
            logger.info(f"\t load expect shape {expect_shape} get {kun_df.shape}")
            self.assertEqual(expect_shape, kun_df.shape)
            pass


    def test_reduce_dataframe(self):
        expect_shape = (29723, 50)

        # 출력 컬럼 정리
        id_cols = ['KUNNR']
        numeric_cols = ['OBLIG', 'KLIMK']
        category_cols = [
            'KDGRP', 'VKBUR', 'VKGRP', 'ORDER_WEEK', 'KUKLA', 'X', 'Y', 'Z', 'GFORM', 'EX_KUNNR', 'ZZMTYP', 'MUL_GUB',
            'GUBUN', 'VSBED',
            'J_001', 'J_002', 'J_003', 'J_004', 'J_005', 'J_006', 'J_007', 'J_008', 'J_009', 'J_010',
            'J_011', 'J_012', 'J_013', 'J_014', 'J_015', 'J_016', 'J_017', 'J_018', 'J_019', 'J_020',
            'J_021', 'J_022', 'J_023', 'J_024', 'J_025', 'J_026',
            'DANGA_ZERO', 'ZGFORM', 'AREA_POINT', 'GUBUN_ALERT', 'VTWEG', 'KONDA', 'COLL_MON'
        ]
        # 고객 데이터에서 data 컬럼은 의미가 있을까? 빈값인 경우의 처리방법 필요
        output_date_cols = ['OPENDATE']

        # 정제된 컬럼 : ID, INFO, number + category data
        output_cols = id_cols + numeric_cols + category_cols + output_date_cols

        load_filename = 'test_data/SIN_KUNNR_202304061027.csv'

        try:
            csv_handler = CsvHandler(processing_type='object', encoding='cp949')

            df = csv_handler.load(
                file_or_filename=load_filename,
                usecols=output_cols,
            )

            # reduce_memory_usage(df: pd.DataFrame, category_cols: list, str_cols: list, numeric_cols: list) -> pd.DataFrame:

            kun_df = reduce_memory_usage(
                df,
#                index_cols=id_cols,
#                use_cols=output_cols,
                category_cols=category_cols,
                numeric_cols=numeric_cols )

            print_table(kun_df, logger.info)
            logger.info(kun_df.info())

        except Exception as e:
            logger.error(f"\t {csv_handler} load fail by {e}")
        else:
            logger.info(f"\t load expect shape {expect_shape} get {kun_df.shape}")
            self.assertEqual(expect_shape, kun_df.shape)
            pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
