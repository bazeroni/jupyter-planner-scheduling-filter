import operator

#gamer = {'Very Vicky': ['Monday', 'Tuesday']}

gamers = []

kimberly = {'name': 'Kimberly Warner', 'availability': ['Mondays', 'Tuesdays', 'Fridays']}

def add_gamer(gamer, gamers_list):
    if 'name' and 'availability' in gamer:
        gamers_list.append(gamer)
    return gamers_list

add_gamer({'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#print(gamers)

def build_daily_frequency_table():
    return {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0, }
count_availability = build_daily_frequency_table()
#print(count_availability.get('Monday'))


def calculate_availability(gamers_list, available_frequency):
    for profile in gamers_list:
        #print(profile)
        for day in profile.get('availability'):
            #print(day)
            count_availability[day] = count_availability.get(day) + 1
    return count_availability

days_available = calculate_availability(gamers, count_availability)
#print(sorted(days_available.values()))

def find_best_night():
    value_check = 0
    best_night = ''
    for value in count_availability.values():
        if value > value_check:
            value_check = value
        else:
            continue
    for key in count_availability.keys():
        if count_availability.get(key) == value_check:
            best_night = key
    return best_night
    #return max(count_availability, key=count_availability.get)

game_name = '\"Abruptly Goblins!\"'
game_night = find_best_night()
#print(game_night)

def available_on_night(gamers_list, day):
    attending = []
    for profile in gamers_list:
        if day in profile.get('availability'):
            #print(profile)
            attending.append(profile.get('name'))
    return attending

attending_game_night = available_on_night(gamers, game_night)
#print(attending_game_night)

form_email = 'Hello, {name}! We found a game of {game} available on {day_of_week}.'

def send_mail(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))
    return

send_mail(attending_game_night, game_night, game_name)

def unable_to_attend_best_night(gamers_list, day):
    unable = []
    for profile in gamers_list:
        if not day in profile.get('availability'):
            #print(profile)
            unable.append(profile.get('name'))
    return unable

unable_attend = unable_to_attend_best_night(gamers, game_night)
#print(unable_attend)

def second_night_availability():
    second_best_night = ''
    sort_best_days = sorted(days_available.values())
    for key in count_availability.keys():
        if count_availability.get(key) == sort_best_days[5]:
            second_best_night = key
    return second_best_night

second_night = second_night_availability()
#print(second_night)

send_mail(unable_attend, second_night, game_name)