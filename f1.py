from bs4 import BeautifulSoup
import requests
import pandas as pd


def f1():
    while True:
        year = input('\n\n\nWhich year table do you want? : ')
        url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'

        try:

            r = BeautifulSoup(requests.get(url).text,'html.parser')

            first_name = []
            last_name = []
            full_name = []
            car_names = []
            pts = []
            country = []
            ranks = []

            #Getting Driver's Full Name
            main_divv = r.html.find('div',{'class':'resultsarchive-wrapper'})
            f_names = main_divv.find_all('span',{'class':'hide-for-tablet'})
            [first_name.append(ft.text) for ft in f_names]
            l_names = main_divv.find_all('span',{"class":"hide-for-mobile"})
            [last_name.append(lt.text) for lt in l_names]
            [full_name.append(''+name[0]+' '+name[1]) for name in zip(first_name,last_name)]

            #Getting Driver's car names
            cars = main_divv.find_all('a',{'class':'grey semi-bold uppercase ArchiveLink'})
            [car_names.append('      '+ct.text) for ct in cars]


            #Getting Driver's score point
            points = main_divv.find_all('td',{'class':'dark bold'})
            [pts.append('      '+pt.text) for pt in points]


            #Getting Driver's Nationality
            nationality = main_divv.find_all('td',{'class':'dark semi-bold uppercase'})
            [country.append('      '+ct.text) for ct in nationality]


            #Getting Ranks
            r = 1
            while r <= len(full_name):
                ranks.append(r)
                r+=1


            data = {
                
                'NAME         ':full_name,
                '         COUNTRY':country,
                'CAR':car_names,
                'PTS':pts,
            }

            arranged = pd.DataFrame(data,index=ranks)
            print(arranged)

        except:
            print('Something went wrong!!!')



if __name__ == '__main__':
    f1()