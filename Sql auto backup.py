import time, sys, os

class Backup():
	def __init__(self):
			self.settings = {'string': '', 'db_name': '', 'path': '', 'integrated_login': '', 'login': '', 'pass': '', 'immediate_backup' : ''}
			self.default_settings = ['Configuration Script For Auto SQL Backup',
			'------------------------------',
			'STRING: VAIO\SQLEXPRESS',
			'DB_NAME: HubNET',
			'Integrated login options Y/N',
			'INTEGRATED_LOGIN: Y',
			'LOGIN: login',
			'PASSWORD: pass',
			'PATH: D:\\',
			'Immediate backup options Y/N',
			'IMMEDIATE_BACKUP: N',
			'Backup Times:',
			'add as many lines as you need',
			'TIME: 06:00',
			'TIME: 18:00',
			'TIME:',
			'TIME:',
			'TIME:']
			self.times = []
			self.command_string = ''
			self.settings_from_file = ''
			self.time_now = ''
			self.ver = 'v0.7'
			self.logo = [" (         (                                                              ",
			" )\ )  (   )\ )     (             )        (               )              ",
			"(()/(( )\ (()/(     )\      (  ( /(      ( )\     )     ( /(   (          ",
			" /(_))((_) /(_)) ((((_)(   ))\ )\())(    )((_) ( /(  (  )\()) ))\ `  )    ",
			"(_))((_)_ (_))    )\ _ )\ /((_|_))/ )\  ((_)_  )(_)) )\((_)\ /((_)/(/(    ",
			"/ __|/ _ \| |     (_)_\(_|_))(| |_ ((_)  | _ )((_)_ ((_) |(_|_))(((_)_\   ",
			"\__ \ (_) | |__    / _ \ | || |  _/ _ \  | _ \/ _` / _|| / /| || | '_ \)  ",
			"|___/\__\_\____|  /_/ \_\ \_,_|\__\___/  |___/\__,_\__||_\_\ \_,_| .__/   ",
			"                                                               |_|        ",
			"		" + self.ver.rjust(7) + "										   "]
								
	def open_settings(self):
		if os.path.isfile('settings.txt') == False:
			print('* Settings not found, default will be recover')
			with open('settings.txt', 'w') as self.settings_obj:
				for i in range(len(self.default_settings)):
					self.settings_obj.write(self.default_settings[i] + '\n')
			self.settings_obj.close()
			time.sleep(0.3)
			print('\nSettings recovered, settings.txt was created!')
			x = input('Enter to exit')
			os.sys.exit(0)
			
		print('* Settings found!\n')
		with open('settings.txt', 'r') as self.settings_obj:
			self.settings_from_file = self.settings_obj.readlines()
		self.settings_obj.close()
		
				
	def strip_settings(self):
		for i in self.settings_from_file:
			if 'STRING' in i:
				self.settings['string'] = i[7:].lstrip().rstrip('\n')
			elif 'DB_NAME' in i:
				self.settings['db_name'] = i[8:].lstrip().rstrip('\n')
			elif 'PATH' in i:
				self.settings['path'] = i[5:].lstrip().rstrip('\n')
				if self.settings['path'][-1] != '\\':
					self.settings['path'] += '\\'
			elif 'INTEGRATED_LOGIN' in i:
				self.settings['integrated_login'] = i[17:].lstrip().rstrip('\n')
			elif 'LOGIN' in i:
				self.settings['login'] = i[6:].lstrip().rstrip('\n')
			elif 'PASS' in i:
				self.settings['pass'] = i[5:].lstrip().rstrip('\n')
			elif 'IMMEDIATE_BACKUP' in i:
				self.settings['immediate_backup'] = i[17:].lstrip().rstrip('\n')
			elif 'TIME' in i:
				if i[5:].lstrip().rstrip('\n') != '':
					self.times.append(i[5:].lstrip().rstrip('\n'))
						
	def print_settings(self):
		self.print_logo()
		print('Connection string: '.ljust(25,'.') + self.settings['string'])
		print('Database name: '.ljust(25,'.') + self.settings['db_name'])
		print('Path: '.ljust(25,'.') + self.settings['path'])
		print('Integrated_login: '.ljust(25,'.') + self.settings['integrated_login'])
		if self.settings['integrated_login'] == 'N':
			print('Login: '.ljust(25,'.') + self.settings['login'])
			print('Pass: '.ljust(25,'.') + self.settings['pass'],)
		print('Immediate backup: '.ljust(25,'.') + self.settings['immediate_backup'])
			
		time.sleep(0.3)
		print('\n' + 'Times of backup\n******************************')
		for i in self.times:
			print('Time: '.ljust(25,'.') + i)
		print()
		
	def print_logo(self):
		for i in self.logo:
			print(i.rjust(75,))
				
	def generate_link_system_login(self):
		self.command_string = ('sqlcmd -S ' + self.settings['string'] + ' -E -Q "BACKUP DATABASE ' \
		+ self.settings['db_name'] + ' TO DISK = \'' + self.settings['path'] + self.settings['db_name'] \
		+ (time.strftime('_D_%y_%m_%d_T_')) + self.time_now.replace(':', '_') + '.bak\'\"')
		
	def generate_link_user_login(self):
		self.command_string = ('sqlcmd -U ' + self.settings['login'] + ' -P ' + self.settings['pass'] +' -S ' \
		+ self.settings['string'] + ' -Q "BACKUP DATABASE ' + self.settings['db_name'] + ' TO DISK = \'' \
		+ self.settings['path'] + self.settings['db_name'] + (time.strftime('_D_%y_%m_%d_T_')) + self.time_now(':', '_') + '.bak\'\"')
		
	def time_now_update(self):
		self.time_now = time.strftime('%H:%M')
		#print(self.time_now)

	def time_line(self, v):
		print('...........................................................', end='\r', flush = True)
		if v < 60:
			v = v * '#'
			print(v, end = '\r')
		else:
			print('...........................................................', end='', flush = True)

	def start(self):
		if self.settings['immediate_backup'] == 'Y' or self.settings['immediate_backup'] == 'y':
			self.rapid_backup()
		else:
			self.start_loop()
	
	def start_loop(self):
		x = 1
		while True:
			for i in range(60):
				if i < 60:
					time.sleep(1)
					self.time_line(i)
				else:
					i = 1		
			self.time_now_update()
			if self.time_now in self.times:
				if self.settings['integrated_login'] == 'Y' or self.settings['integrated_login'] == 'y':
					backup.generate_link_system_login()
				else:
					backup.generate_link_user_login()
				print('\n','* backup start at ' + time.strftime('_D_%y_%m_%d_T_') + self.time_now)
				#subprocess.Popen(self.command_string)
				result_obj = os.popen(self.command_string)
				print(result_obj.read())
				
				#add to zip
				
	def rapid_backup(self):
		self.time_now_update()
		if self.settings['integrated_login'] == 'Y':
			backup.generate_link_system_login()
		else:
			backup.generate_link_user_login()
		print('* backup start at ' + self.time_now)
		print(self.command_string)
		#subprocess.call(self.command_string)			
		result_obj = os.popen(self.command_string)
		print(result_obj.read())
		self.start_loop()
		
	def about(self):
		print(self.logo)
		print('App created by\n M.J.S.')
		
				
if __name__ == '__main__':
	backup = Backup()
	try:
		if len(sys.argv) < 2:		
			backup.open_settings()
			backup.strip_settings()
			backup.print_settings()
			backup.start()
			#backup.rapid_backup()
			x = input('enter to exit')
			sys.exit(0)
		elif sys.argv[1] == '-?' or sys.argv[1] == '?':
			backup.print_logo()
			backup.about()
		else:
			pass
	except IndexError:
		pass
