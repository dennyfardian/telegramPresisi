import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='********',
    database='data_satu'
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
    sql.execute("SELECT nama, id, proyek FROM pekerja")    
    result_sql = sql.fetchall()
    
    response_message = 'Nama    id    proyek\n'
    for x in result_sql:
        response_message = response_message + str(x) + '\n'
        
    response_message = response_message.replace("(", "").replace(",", "").replace(")", "").replace("'", "")
    bot.reply_to(message, response_message)
    #print(resultsql)    

    # first_name = message.chat.first_name
    # last_name = message.chat.last_name
    # bot.reply_to(message, 'Hi, apa kabar {} {}?'.format(first_name, last_name))
    # print(message)

@bot.message_handler(commands=['addProyek'])
def addProyek(message):
    texts = message.text.split(' ')
    idproyek = texts[1]
    namaproyek = texts[2]
    klienproyek = texts[3]
    keterangan = texts[4]

    insert = "INSERT INTO proyek(id, nama_proyek, klien, keterangan) VALUES (%s, %s, %s, %s)"
    val = (idproyek, namaproyek, klienproyek, keterangan)
    sql.execute(insert, val)
    mydb.commit()


    bot.reply_to(message, 'Sudah tersimpan ' + namaproyek)

@bot.message_handler(commands=['id'])
def action_id(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id
    bot.reply_to(message, '''
Hai, ini ID Telegram kamu
Nama = {} {} 
ID = {}
        '''.format(first_name,last_name, id_telegram))

@bot.message_handler(commands=['remindMe'])
def remindMe(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id

    #query sql
    

    #result query sql

    bot.reply_to(message, '''
Hai {} {} ! Ini deadlinemu:

        '''.format(first_name,last_name) + result)
            

#tar kasi command help buat user



#command Help *jangan dihapus
@bot.message_handler(commands=['helpAdmin'])
def action_helpAdmin(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.reply_to(message, '''
Hi {} {}, ini list command:
/allPegawai -> Melihat seluruh pegawai
/allProyek -> Melihat seluruh proyek (status masih berjalan)
/allProyekAll -> Melihat seluruh proyek 
/allTeam -> Melihat seluruh team
/addPegawai [id-telegram] [nama-pegawai] [jabatan] ->
/addProyek [id-proyek] [nama-proyek] -> 
/addProgress [nama-pegawai] [id-proyek] [catatan-progress]  -> 
/remindMe -> Memberikan reminder proyek kepada user terkait berdasarkan ID-telegram
/remindProyek [nama-proyek] -> Memberikan reminder proyek tertentu ke dalam grup
/remindAll -> Mengirimkan reminder 
/progressPegawai [] -> 
/progressProyek -> 
/help -> List Command Bot utk User
'''.format(first_name,last_name))

print('bot start running')

bot.polling()

    