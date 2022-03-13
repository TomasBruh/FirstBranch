from datetime import datetime
date_1 = datetime.strptime(input("Please input your birthday date: "), '%Y %m %d').date()
date_1 = date_1.replace(year=datetime.now().year)
date_2 = datetime.now().date()
difference = date_1 - date_2
#for(int i = 0; i < 12-13pask_Kontrolinis)
#delta??
print(difference)
