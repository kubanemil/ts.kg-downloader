from ts_kg import *

shows = open('.\\link.txt', 'r')
show_list = shows.read().split('\n')
show_list = show_list[:-1]
print('Choose show(Enter its order number) ')
print('For example: 3. Бумажный дом')
print('Then enter: => 3')
for i in range(len(show_list)):
	print(str(i+1)+'. '+get_title(show_list[i]))
while True:
	try:
		show_int = int(input('\t=>'))
		break
	except ValueError:
		print('Incorrect input. Try again')

show_link = show_list[show_int-1]


while True:
	print('Enter "exit" or nothing to quit.')
	print('Do you want to download one episode or last episode or more?(one/last/more)')
	ask = input('\t=> ')
	if ask == '' or ask=='exit':
		break
	elif ask == 'one':
		episode_link = input('Send me link of this episode: ')
		if link_exist(episode_link):
			if isEpisode(episode_link):
				print(episode_link)
				download_episode(episode_link)
			else:
				print('That is not an episodes link.')
				print('Example link: "https://www.ts.kg/show/rick_and_morty/3/9"')
		else:
			print('No such link! Try again')
	elif ask == 'more':
		print('Which seasons you want to download?')
		print('Enter "ALL" to download all episodes from all seasons.')
		print('Enter in format "1, 2, 3, 4" to download several seasons.')
		print('Enter in format "1", to download only one season.')
		season = input('\t=> ')
		if season == 'ALL':
			print('Wait, while downloading all episodes...')
			domain_segments = show_link.split('/')
			season = 1
			isNextSeason = True
			while isNextSeason:
				episode = 1
				while True:
					episode_link = "/".join(domain_segments[:5])+'/'+str(season)+'/'+str(episode)+'/'
					if link_exist(episode_link):
						print(episode_link)
						download_episode(episode_link)
						episode += 1
					else: 
						season += 1
						break
				if episode < 2:
					isNextSeason = False
		elif len(season) > 2:
			season_list = season.split(',')
			season_numbers = []
			for season in season_list:
				season = int(season)
				season_numbers.append(season)
			domain_segments = show_link.split('/')
			for ses in season_numbers:
				episode = 1
				while True:
					episode_link = "/".join(domain_segments[:5])+'/'+str(season)+'/'+str(episode)+'/'
					if link_exist(episode_link):
						print(episode_link)
						download_episode(episode_link)
						episode += 1
					else:
						break

		elif len(season) <= 2:
			the_season = season.split()[0]
			domain_segments = show_link.split('/')
			episode = 1
			while True:
				episode_link = "/".join(domain_segments[:5])+'/'+str(season)+'/'+str(episode)+'/'
				if link_exist(episode_link):
					print(episode_link)
					download_episode(episode_link)
					episode += 1
				else: 
					break

	elif ask == 'last':
		show_episode = []
		domain_segments = show_link.split('/')
		r = open('.\\dataset.txt', 'r')
		all_episode_list = r.read().split('\n')
		for link in all_episode_list:
			if domain_segments[4] in link:
				show_episode.append(link)
		print(show_episode[-1])
		download_episode(show_episode[-1])
	else:
		print('????I dont understand you????')
print('Finished.')
input()