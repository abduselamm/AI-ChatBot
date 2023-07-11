import mysql.connector


def chat(message):
    mydb = mysql.connector.connect(
        host="cloud.mindsdb.com",
        user='abduselamm320@gmail.com',
        password='Java@123',
        port="3306"
    )

    cursor = mydb.cursor()
    cursor.execute(
        'SELECT response FROM mindsdb.oipdc_chat_model WHERE usr_name = "abduselam" AND text = "{}"'.format(message))
    rows = cursor.fetchmany(100)
    reply = ""
    for x in rows:
        for y in x:
            reply += y
    return reply
