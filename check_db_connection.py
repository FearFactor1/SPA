import pymysql.cursors




def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='ga-ortax-db.ga.stoloto.su',
                                 user='ortax_adm',
                                 password='ortax_adm',
                                 db='db_ortax',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection






def test_phone_info_ortax():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute("select * FROM db_ortax.phone WHERE phone_number = 79005553535")
        for row in cursor:
            a = row["security_code"]
            print(f'security_code: {a}')
#            print(" ----------- ")
#            print("Row: ", row)
#            print("id: ", row["id"])
#            print("person_id: ", row["person_id"])
#            print("phone_number: ", row["phone_number"])
#            print("phone_status: ", row["phone_status"])
#            print("verification_code: ", row["verification_code"])
#            print("verification_error_count: ", row["verification_error_count"])
#            print("security_code: ", row["security_code"])
#            print("security_error_count: ", row["security_error_count"])
#            print("created_date: ", row["created_date"], type(row["created_date"]))
 #           print("verified_date: ", row["verified_date"], type(row["verified_date"]))
 #           print("invalidated_date: ", row["invalidated_date"])
    finally:
        connection.close()

if __name__ == '__main__':
    test_phone_info_ortax()

#-----------------------------------------------------------------------


