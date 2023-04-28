import pymysql

import config
import hash


class db_mysql:
    def mysql_connect(self):
        try:
            self.conn = pymysql.connect(host=config.db[0], port=config.db[1], user=config.db[2], password=config.db[3],
                                        db=config.db[4])
            self.cursor = self.conn.cursor()
            if self.cursor:
                return True
            else:
                return False
        except:
            return False

    def create_mysql(self):
        self.mysql_connect()
        try:
            self.cursor.execute(config.mysql_create)
            self.cursor.execute(config.mysql_users)
            self.cursor.execute(config.mysql_datas)
            self.conn.commit()
            return True
        except pymysql.err.ProgrammingError:
            return True
        except:
            return

    def sql_users(self, username, password):
        self.mysql_connect()
        try:
            if self.cursor.execute(config.sql_pass.format(username, password)) == 1:
                return True
            else:
                return False
        except:
            return False

    def query(self, username, password):
        hash_md5 = hash.encode_md5(password)
        try:
            if self.cursor.execute(config.query_pass.format(username, hash_md5)) == 1:
                return True
            else:
                return False
        except:
            return False

    def query_name(self, username):
        self.mysql_connect()
        self.cursor.execute(config.query_name.format(username))
        result = self.cursor.fetchone()
        if result[0] == 1:
            return True
        else:
            return False

    def query_data(self):
        self.mysql_connect()
        self.cursor.execute(config.query_data)
        rows = self.cursor.fetchall()
        for row in rows:
            dict_row = {}
            dict_row['id'] = row[0]
            dict_row['name'] = row[1]
            dict_row['class'] = row[2]
            dict_row['yuwen'] = row[3]
            dict_row['math'] = row[4]
            dict_row['english'] = row[5]
            config.result.append(dict_row)
        print(config.result)

    def insert_data(self, Stutdent_list):
        self.mysql_connect()
        if self.if_insert_data(Stutdent_list):
            return 'exist'
        try:
            Stutdent_list_dict = Stutdent_list[0]
            Stutdent_lists = (Stutdent_list_dict['id'], Stutdent_list_dict['name'], Stutdent_list_dict['class'],
                              Stutdent_list_dict['yuwen'], Stutdent_list_dict['math'], Stutdent_list_dict['english'])
            if self.cursor.execute(config.insert_date, Stutdent_lists) == 1:
                return True
            return False
        except:
            return False

    def if_insert_data(self, Stutdent_list):
        self.mysql_connect()
        Stutdent_list_dict = Stutdent_list[0]
        Stutdent_lists = (Stutdent_list_dict['id'])

        if self.cursor.execute(config.if_insert_data, Stutdent_lists) == 1:
            return True
        else:
            return False

    def delete_data(self, data):
        try:
            self.mysql_connect()
            if self.cursor.execute(config.del_data_sql, data) == 1:
                return True
            return False
        except TypeError:
            return None

    def alter_data(self, data):
        self.mysql_connect()
        if self.cursor.execute(config.alter_data_sql, data) == 1:
            return True
        return False

    def query_data_vague(self, *args):
        config.result_data.clear()
        print(args[0])
        self.mysql_connect()
        self.cursor.execute(config.vague_query_data_sql, (
        f'{args[0][0]}', f'{args[0][1]}', f'{args[0][2]}', f'{args[0][3]}', f'{args[0][4]}', f'{args[0][5]}'))
        result = self.cursor.fetchall()
        if result:
            for row in result:
                dict_row = {}
                dict_row['id'] = row[0]
                dict_row['name'] = row[1]
                dict_row['class'] = row[2]
                dict_row['yuwen'] = row[3]
                dict_row['math'] = row[4]
                dict_row['english'] = row[5]
                config.result_data.append(dict_row)
            print(config.result_data)
            return True
        else:
            return False

    def xlsx_load(self):
        success = True
        for data in config.cell_values:
            try:
                self.cursor.execute(config.load_data_sql, data)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(f"插入数据失败: {e}")
                success = None
                break
            except:
                self.conn.rollback()
                print("插入数据失败")
                success = False

        if success:
            print("插入数据成功")
            return True
        if success == None:
            print('数据id已存在')
            return None
        else:
            print("插入数据失败")
            return False

    def xlsx_save(self):
        try:
            self.cursor.execute(config.query_data)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"查询数据失败: {e}")
            return False

    def repass(self, *args):
        passwd = args[0]
        user = args[1]
        md5_pass = hash.encode_md5(passwd)
        md5_tuple = (md5_pass, user)
        self.mysql_connect()
        try:
            if self.cursor.execute(config.repass_sql, md5_tuple):
                return True
            return False
        except pymysql.err.OperationalError as e:
            print(f'数据库啥的问题:{e}')
            return False

    def create_user(self):
        try:
            user = config.user_pass[0]
            passwd = config.user_pass[1]
        except AttributeError as e:
            print(f'不创建用户{e}')
            return
        else:
            self.cursor.execute(config.sql_pass.format(user, passwd))

    def show_user(self):
        self.mysql_connect()
        self.cursor.execute(config.show_user_sql)
        result = self.cursor.fetchall()
        if result:
            config.show_user.append('1')
            return
        return False

    def del_user(self, *args):
        self.mysql_connect()
        if self.cursor.execute(config.del_user_sql, args) == 1:
            return True
        return False
