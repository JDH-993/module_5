class User:
	Us = []

	def __new__(cls, *args):
		args = args
		cls.Us.append(args)
		return super().__new__(cls)

	def __init__(self, nickname, password, age):
		self.nickname = nickname


class Video:
	Vid = []

	def __new__(cls, *args, time_now = 0, adult_mode = False):
		args = (args[0], args[1], time_now, adult_mode)
		cls.Vid.append(args)
		return super().__new__(cls)

	def __init__(self, title, duration, time_now = 0, adult_mode = False):
		self.title = title
		self.time_now = time_now
		self.adult_mode = adult_mode


class UrTube:
	users = []
	videos = None
	current_user = None
	cor = []

	def __init__(self, nickname, password, *args):
		self.nickname = nickname
		self.password = password
		self.args = args

	def add(*args):
		var = Video.Vid
		UrTube.videos = var

	def log_out(*args):
		UrTube.current_user = None
		return UrTube.current_user

	def log_in(*args):
		args = args
		if UrTube.users is None:
			return print("пользователей нет")
		for i in range(len(UrTube.users)):
			print(len(UrTube.users))
			for j in range(len(UrTube.users[i])):
				if args[0] == UrTube.users[i][j] and args[1] == UrTube.users[i][j + 1]:
					if len(UrTube.users) == 1:
						UrTube.current_user = UrTube.users
						return UrTube.current_user
					else:
						UrTube.current_user = UrTube.users[i]
						return UrTube.current_user
				else:
					print("Такого пользователя нет")
					return UrTube.current_user

	def register(*args):
		if len(UrTube.users) == 0:
			p = (args[0], args[1], args[2])
			UrTube.users.append(p)
			UrTube.current_user = p
			return UrTube.current_user
		for i in range(len(UrTube.users)):
			for j in range(len(UrTube.users[i])):
				if UrTube.users[i][j] == args[0]:
					print(f'Пользователь {args[0]} уже существует')
					return UrTube.users
				else:
					p = (args[0], args[1], args[2])
					UrTube.users.append(p)
					UrTube.current_user = p
					return UrTube.users

	def get_videos(*args):
		p = ""
		UrTube.cor.clear()
		for i in range(len(UrTube.videos)):
			p = ""
			for g in range(len(UrTube.videos[i][0])):
				if UrTube.videos[i][0][g] != " ":
					p = p + UrTube.videos[i][0][g].lower()
				else:
					p = p + " "
			if args[0].lower() in p:
				UrTube.cor.append(UrTube.videos[i][0])
		return UrTube.cor

	def watch_video(*args):
		k = []
		for u in range(len(UrTube.videos)):
			if args[0] == UrTube.videos[u][0]:
				k = UrTube.videos[u]
		if len(k) == 0:
			return 
		if k is not None:
			if UrTube.current_user is None:
				print("Войдите в аккаунт, чтобы смотреть видео")
				return 
			elif k[-1] is True and UrTube.current_user[-1] < 18:
				print("Вам нет 18 лет, пожалуйста покиньте страницу")
				return
			elif k[2] == 0:
				for p in range(1, k[-3] + 1):
					print(p, end = " ")
				print("Конец видео")
				return
			elif k[2] > 0:
				for p in range(k[2], k[1]+1):
					print(p, end = " ")
				print("Конец видео")
				return
		return


ur = UrTube

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user[0])

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
