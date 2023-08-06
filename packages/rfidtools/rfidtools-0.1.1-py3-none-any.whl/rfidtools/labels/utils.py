import re
import csv
import webbrowser
from datetime import datetime

import pyodbc as db
from fabric import Connection

PRINT_LOGS_PATH = 'C:\\Print_Logs\\'
PRINT_ARCHIVES_PATH = 'C:\\Print_Archives\\'

# SQL connection
sql_connection = 'Driver={ODBC Driver 18 for SQL Server};Server=192.168.2.67;Database=DataWhseCiot;UID=SA;PWD=Passw0rd;Encrypt=no'

# SSH connection
ssh_kwargs = {'host': '192.168.2.67', 'user': 'RFIDAdmin', 'connect_timeout': 10, 'connect_kwargs': {'password': 'Passw0rd2987'}}


# type: 'Porcelain' OR 'Slabs'
def listlogs(type) -> list:
    if type not in {'Porcelain', 'Slabs'}:
        print('Something went very wrong.\nInvalid type argument, object has impossible name.')
        raise TypeError

    with Connection(**ssh_kwargs) as c, c.sftp() as sftp:
        sftp.chdir(PRINT_LOGS_PATH)
        logs = sftp.listdir()

    return [log for log in logs if re.search(f'^{type}_[0-9]*.txt', log) or re.search(f'^{type}_nf_[0-9]*.txt', log)]


# type: 'Porcelain' OR 'Slabs'
def parse_log(type, log, bin) -> list[tuple]:
    data = list()

    if type == 'Porcelain':
        def label(row) -> tuple:
            return (
                row['rfid'],  # ProductTagID
                211,  # WarehouseCode
                'Recieved',  # Status
                datetimestamp,  # ReceivedDateTimeStamp
                'script',  # CreatedBy
                bin,  # Bin
                bytearray.fromhex(row['rfid']).decode(),  # ProductTagName
                row['code'])  # ProductCode

    elif type == 'Slabs':
        def label(row) -> tuple:
            return (
                row['code'] + '-' + row['lot'] + row['serial'],  # Barcode
                row['rfid'],  # TagID
                row['code'],  # ProductCode
                row['lot'],  # BlockNumber
                row['serial'].strip('-'),  # SlabNumber
                row['dim_x'],  # Length
                row['dim_y'],  # Width
                211,  # WarehouseCode
                bin,  # LocationCode
                2,  # StatusID
                datetimestamp)  # ReceivedDateTimeStamp

    else:
        print('Something went very wrong.\nInvalid type argument, object has impossible name.')
        raise TypeError

    with Connection(**ssh_kwargs) as c, c.sftp() as sftp:
        datetimestamp = datetime.fromtimestamp(sftp.stat(PRINT_LOGS_PATH + log).st_mtime)
        with sftp.open(PRINT_LOGS_PATH + log, mode='r') as csvfile:
            rows = csv.DictReader(csvfile, dialect='unix')
            for row in rows:
                data.append(label(row))

    return data


# type: 'Porcelain' OR 'Slabs'
def send_print(type, payload) -> bool:
    if type == 'Porcelain':
        url = 'http://192.168.2.67:8080/bartender/print/rfid_templates/porcelain_nf.btw?'
        for key, value in payload.items():
            if isinstance(value, str) is str:
                value = value.replace(' ', '%20')

            url += f'{key}={value}&'
        url = url[:-1]

        webbrowser.open(url)

    elif type == 'Slabs':
        url = 'http://192.168.2.67:8080/bartender/print/rfid_templates/slabs_nf.btw?'
        for key, value in payload.items():
            if isinstance(value, str) is str:
                value = value.replace(' ', '%20')

            url += f'{key}={value}&'
        url = url[:-1]

        webbrowser.open(url)

    else:
        print('Something went very wrong.\nInvalid type argument, object has impossible name.')
        raise TypeError
        return False

    return True


def query(data, query) -> bool:
    connection = db.connect(sql_connection)
    cursor = connection.cursor()
    try:
        connection.autocommit = False
        cursor.fast_executemany = True
        cursor.executemany(query, data)

    except db.DatabaseError as err:
        print('Database Error: ' + str(err))
        connection.rollback()
        return False

    else:
        connection.commit()
        return True
    connection.close()


def archive(log) -> bool:
    try:
        with Connection(**ssh_kwargs) as c:
            c.run(f'mv {PRINT_LOGS_PATH}{log} {PRINT_ARCHIVES_PATH}{log}')

    except Exception as e:
        print('Something went wrong, logs were not archived.\n' + str(e))
        return False

    else:
        return True
