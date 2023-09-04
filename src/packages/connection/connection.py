from pymysql import Connect

db = Connect(
	host='localhost',
	user='root',
	passwd='',
	database='sms_deliveryapp_usuarios'
)