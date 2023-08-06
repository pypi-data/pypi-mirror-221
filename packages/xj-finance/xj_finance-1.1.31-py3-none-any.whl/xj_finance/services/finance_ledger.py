from django.db import connection

from xj_finance.utils.utility_method import aggregate_data


class FinanceLedgerService:
    @staticmethod
    def ledger():
        query = "SELECT title,full_name,field_6,field_1 FROM thread t LEFT JOIN user_base_info u ON  t.user_id = u.id where category_id=160;"
        results_list = FinanceLedgerService.execute_raw_sql(query)
        results_list = aggregate_data(results_list, "field_6", ['field_1'])
        print(results_list)
        # 将结果输出到控制台，使用UTF-8编码
        # for item in results_list:
        #     print(item)

        return results_list, None

    @staticmethod
    def execute_raw_sql(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return results

# def execute_raw_sql(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         rows = cursor.fetchall()
#     return rows
# def execute_raw_sql(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         results = cursor.fetchall()
#         result_list = []
#         for row in results:
#             row_list = [str(item, 'utf-8') if isinstance(item, bytes) else item for item in row]
#             result_list.append(row_list)
#         return result_list
