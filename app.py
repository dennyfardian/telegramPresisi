import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Holy_8448', #ubah ke password kalian ya
    database='pt_presisi'
)


#cek akses database
print(mydb)

#input ke SQL
sql = mydb.cursor()

api = '1444723350:AAF_rboqMrkT5tbX2-7CSqPp7QnLNcKsk5E'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['allPegawai'])
def allpegawai(message):
    #split message
    texts = message.text.split(' ')
    print(texts)

    #input utk SQL
    sql.execute("SELECT nama, id_telegram, divisi FROM pekerja")    
    result_sql = sql.fetchall()
    
    response_message = 'Nama  id                      divisi\n'
    for x in result_sql:
        response_message = response_message + str(x) + '\n'
        
    response_message = response_message.replace("(", "").replace(",", "").replace(")", "").replace("'", "")
    bot.reply_to(message, response_message)
    #print(resultsql)    

    # first_name = message.chat.first_name
    # last_name = message.chat.last_name
    # bot.reply_to(message, 'Hi, apa kabar {} {}?'.format(first_name, last_name))
    # print(message)

@bot.message_handler(commands=['allProyek'])
def allProyek(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)

@bot.message_handler(commands=['addPegawai'])
def addPegawai(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)

@bot.message_handler(commands=['addProyek'])
def addProyek(message):
    texts = message.text.split(' ')
    id_proyek = texts[1]
    namaproyek = texts[2]
    deadline = texts[3]
    deskripsi = texts[4]

    insert = "INSERT INTO proyek(ID_proyek, namaProyek, deadline, deskripsi) VALUES (%s, %s, %s, %s)"
    val = (id_proyek, namaproyek, deadline, deskripsi)
    sql.execute(insert, val)
    mydb.commit() #kalau ada modifikasi basis data harus pake commit


    bot.reply_to(message, 'Sudah tersimpan ' + namaproyek)

@bot.message_handler(commands=['addProgress'])
def addProgress(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)



@bot.message_handler(commands=['remindMe'])
def remindMe(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id
    
    id_telegram_str = str(id_telegram)
    
    #query sql
    query_sql = "SELECT id_proyek, namaProyek, deadline FROM bekerja WHERE bekerja.nama = (SELECT nama FROM pegawai WHERE pegawai.id_telegram = %s )"    
    val = id_telegram_str
    sql.execute(query_sql, val)
    result_sql = sql.fetchall()
    print(result_sql)

    #result query sql
#     response_message = '''
# Hai {} {} ! Ini deadlinemu:   
# IDProyek  Nama Proyek                      Deadline\n'
#     '''

#     for x in result_sql:
#         response_message = response_message + str(x) + '\n'
        
#     response_message = response_message.replace("(", "").replace(",", "").replace(")", "").replace("'", "")
#     bot.reply_to(message, response_message)

#     bot.reply_to(message, '''
# Hai {} {} ! Ini deadlinemu:

#         '''.format(first_name,last_name) + result)
            
@bot.message_handler(commands=['remindAll'])
def remindAll(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)

@bot.message_handler(commands=['progressPegawai'])
def progressPegawai(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)

@bot.message_handler(commands=['progressProyek'])
def progressProyek(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)

#tar kasi command help buat user
@bot.message_handler(commands=['help'])
def help(message):
    response_message = 'Ini fungsi {}'.format(message.text)
    bot.reply_to(message, response_message)


#command Help *jangan dihapus
@bot.message_handler(commands=['helpAdmin']) #khusus admin, kalau buat user /help tapi terbatas fungsinya
def action_helpAdmin(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.reply_to(message, '''
Hi {} {}, ini list command:
/allPegawai -> Melihat seluruh pegawai
/allProyek -> Melihat seluruh proyek (status masih berjalan) 
/addPegawai [id-telegram] [nama-pegawai] [jabatan] ->
/addProyek [id-proyek] [nama-proyek] -> 
/addProgress [nama-pegawai] [id-proyek] [catatan-progress]  -> 
/remindMe -> Memberikan reminder proyek kepada user terkait berdasarkan ID-telegram
/remindProyek [nama-proyek] -> Memberikan reminder proyek tertentu ke dalam grup
/remindAll -> Mengirimkan reminder 
/progressPegawai [nama-pegawai] [id-proyek] [nama-proyek] [waktu-progress] [progress]-> Menampilkan progres  pegawai dalam mengerjakan proyek`
/progressProyek [id-proyek] [nama-proyek] [progress] [deadline]-> Menampilkan progres proyek yang dikerjakan
/help -> List Command Bot utk User
'''.format(first_name,last_name))

### FUNGSI TAMBAHAN
@bot.message_handler(commands=['id']) #buat tau kita id-telegramnya apa
def action_id(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id
    bot.reply_to(message, '''
Hai, ini ID Telegram kamu
Nama = {} {} 
ID = {}
        '''.format(first_name,last_name, id_telegram))




print('bot start running')

bot.polling()

    
