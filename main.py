import requests
from bs4 import BeautifulSoup
import json
cookies = {
    '__ddg1_': 'CmFqDyeIurN4EPVsuBK9',
    '_xsrf': '8464204d2a428f4a110b640ad83281a1',
    'region_clarified': 'NOT_SET',
    'crypted_hhuid': '9D04666D4FDBA6113F665D5D5669DC29A6B450FB9CB40C5102201E7DA180D5D8',
    'hhtoken': 'zY6amNlQyAbmzEgYy6oHtHLVpmXH',
    'hhuid': 'yBHzhNlKOfYwAGPRBKQw4w--',
    '_ym_uid': '1674642598139452201',
    '_ym_d': '1674642598',
    'iap.uid': '5bcb3801a97c4ecd80c9a9dde2358723',
    'tmr_lvid': '2ea3e5331aa0fb67523310febabbfea9',
    'tmr_lvidTS': '1674642601671',
    'redirect_host': 'tomsk.hh.ru',
    'crypted_id': '07906500B93B619C6E9D053C62533499A5471C6F722104504734B32F0D03E9F8',
    'hhul': 'f478341142377b6b261d95ca82cf89542b0eb071f7520bb830088aacd0093195',
    'hhrole': 'applicant',
    'regions': '2',
    'display': 'desktop',
    'GMT': '3',
    '_gid': 'GA1.2.304541009.1676316808',
    '_ym_isad': '2',
    'gssc58': '',
    '_ga_44H5WGZ123': 'GS1.1.cc68fb99161741917de7ce42493d2cccf81d5253efad8ddbdf8b0f087a5959c3.3.1.1676317210.59.0.0',
    '_gat_gtag_UA_11659974_2': '1',
    '_ga': 'GA1.2.804040968.1674642598',
    '_gat_gtag_UA_11659974_2_DG': '1',
    '_hi': '50730328',
    '__zzatgib-w-hh': 'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9EJjFfbR9SGHwSH0peCn0rTUZ6KCUMDBBeP3NueS9xZSRfeBQjdRNTayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIpUggSXT5DcHMyN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LFndyJk8KDWMvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQmsgYE5bIEVYTnohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1pJmNOXShFEVM2KR0Yd2spCxARF3J3KnpbOyBTZEgUUTVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisgF3psKlEIDV4+QmllbQwtUlFRS2IPHxo0aQteTA==ffe/6w==',
    '__zzatgib-w-hh': 'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9EJjFfbR9SGHwSH0peCn0rTUZ6KCUMDBBeP3NueS9xZSRfeBQjdRNTayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIpUggSXT5DcHMyN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LFndyJk8KDWMvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQmsgYE5bIEVYTnohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1pJmNOXShFEVM2KR0Yd2spCxARF3J3KnpbOyBTZEgUUTVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisgF3psKlEIDV4+QmllbQwtUlFRS2IPHxo0aQteTA==ffe/6w==',
    'device_breakpoint': 'xs',
    'cfidsgib-w-hh': 'Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==',
    'total_searches': '11',
    'cfidsgib-w-hh': 'Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==',
    'cfidsgib-w-hh': 'Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==',
    'gsscgib-w-hh': 'zOTzM0rDDTbBu+fEcyd4PYuR/UOzll56PsqCR1JZYCAD1oj+pM5t0LbEfpSoX7HEeF0jCKXmKubpznuHlDHNo96Uu0J9LWeF10v4EwrNHLT88zLJRL4VfRUZ162J7SxRfW95SiD0ns2WM8Wcd986JtxylHiz6xqHcHLfLHbnInlue4tolhCYcID2XElAfNyKPcZtsmWDjHuMl+nc7id0if2B+WXLcbmkVD5yEJ5bonJQYDKChxFUqvzlU4wXB7T5gw==',
    'gsscgib-w-hh': 'zOTzM0rDDTbBu+fEcyd4PYuR/UOzll56PsqCR1JZYCAD1oj+pM5t0LbEfpSoX7HEeF0jCKXmKubpznuHlDHNo96Uu0J9LWeF10v4EwrNHLT88zLJRL4VfRUZ162J7SxRfW95SiD0ns2WM8Wcd986JtxylHiz6xqHcHLfLHbnInlue4tolhCYcID2XElAfNyKPcZtsmWDjHuMl+nc7id0if2B+WXLcbmkVD5yEJ5bonJQYDKChxFUqvzlU4wXB7T5gw==',
    'tmr_detect': '0%7C1676317215159',
    'fgsscgib-w-hh': 'CICq4752c0e24d11172d830de127319ccb45934a',
    'fgsscgib-w-hh': 'CICq4752c0e24d11172d830de127319ccb45934a',
}

headers = {
    'authority': 'spb.hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '__ddg1_=CmFqDyeIurN4EPVsuBK9; _xsrf=8464204d2a428f4a110b640ad83281a1; region_clarified=NOT_SET; crypted_hhuid=9D04666D4FDBA6113F665D5D5669DC29A6B450FB9CB40C5102201E7DA180D5D8; hhtoken=zY6amNlQyAbmzEgYy6oHtHLVpmXH; hhuid=yBHzhNlKOfYwAGPRBKQw4w--; _ym_uid=1674642598139452201; _ym_d=1674642598; iap.uid=5bcb3801a97c4ecd80c9a9dde2358723; tmr_lvid=2ea3e5331aa0fb67523310febabbfea9; tmr_lvidTS=1674642601671; redirect_host=tomsk.hh.ru; crypted_id=07906500B93B619C6E9D053C62533499A5471C6F722104504734B32F0D03E9F8; hhul=f478341142377b6b261d95ca82cf89542b0eb071f7520bb830088aacd0093195; hhrole=applicant; regions=2; display=desktop; GMT=3; _gid=GA1.2.304541009.1676316808; _ym_isad=2; gssc58=; _ga_44H5WGZ123=GS1.1.cc68fb99161741917de7ce42493d2cccf81d5253efad8ddbdf8b0f087a5959c3.3.1.1676317210.59.0.0; _gat_gtag_UA_11659974_2=1; _ga=GA1.2.804040968.1674642598; _gat_gtag_UA_11659974_2_DG=1; _hi=50730328; __zzatgib-w-hh=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9EJjFfbR9SGHwSH0peCn0rTUZ6KCUMDBBeP3NueS9xZSRfeBQjdRNTayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIpUggSXT5DcHMyN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LFndyJk8KDWMvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQmsgYE5bIEVYTnohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1pJmNOXShFEVM2KR0Yd2spCxARF3J3KnpbOyBTZEgUUTVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisgF3psKlEIDV4+QmllbQwtUlFRS2IPHxo0aQteTA==ffe/6w==; __zzatgib-w-hh=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9EJjFfbR9SGHwSH0peCn0rTUZ6KCUMDBBeP3NueS9xZSRfeBQjdRNTayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIpUggSXT5DcHMyN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LFndyJk8KDWMvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQmsgYE5bIEVYTnohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1pJmNOXShFEVM2KR0Yd2spCxARF3J3KnpbOyBTZEgUUTVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeisgF3psKlEIDV4+QmllbQwtUlFRS2IPHxo0aQteTA==ffe/6w==; device_breakpoint=xs; cfidsgib-w-hh=Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==; total_searches=11; cfidsgib-w-hh=Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==; cfidsgib-w-hh=Ay6lE8DUfFinEVEp/b0qWTVmg6OiUAK38v3I7pWSp/6PziRVftLBj5Zt0yp+GIahiPVpW8BL3y6XEWZsMuf6NnZN594GWmJtdnwcvylZEYg/e4Y/CkWg0gGqDGBRiajnZtI+4eQjXlsFlu1hWm4Dabw/M5LPH0royfp8EA==; gsscgib-w-hh=zOTzM0rDDTbBu+fEcyd4PYuR/UOzll56PsqCR1JZYCAD1oj+pM5t0LbEfpSoX7HEeF0jCKXmKubpznuHlDHNo96Uu0J9LWeF10v4EwrNHLT88zLJRL4VfRUZ162J7SxRfW95SiD0ns2WM8Wcd986JtxylHiz6xqHcHLfLHbnInlue4tolhCYcID2XElAfNyKPcZtsmWDjHuMl+nc7id0if2B+WXLcbmkVD5yEJ5bonJQYDKChxFUqvzlU4wXB7T5gw==; gsscgib-w-hh=zOTzM0rDDTbBu+fEcyd4PYuR/UOzll56PsqCR1JZYCAD1oj+pM5t0LbEfpSoX7HEeF0jCKXmKubpznuHlDHNo96Uu0J9LWeF10v4EwrNHLT88zLJRL4VfRUZ162J7SxRfW95SiD0ns2WM8Wcd986JtxylHiz6xqHcHLfLHbnInlue4tolhCYcID2XElAfNyKPcZtsmWDjHuMl+nc7id0if2B+WXLcbmkVD5yEJ5bonJQYDKChxFUqvzlU4wXB7T5gw==; tmr_detect=0%7C1676317215159; fgsscgib-w-hh=CICq4752c0e24d11172d830de127319ccb45934a; fgsscgib-w-hh=CICq4752c0e24d11172d830de127319ccb45934a',
    'pragma': 'no-cache',
    'referer': 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2',
    'sec-ch-ua': '"Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0',
}

params = {
    'text': 'python django flask',
    'salary': '',
    'area': [
        '1',
        '2',
    ],
    'ored_clusters': 'true',
    'enable_snippets': 'true'
}

response = requests.get('https://spb.hh.ru/search/vacancy', params=params, cookies=cookies, headers=headers).text
soup = BeautifulSoup(response, "lxml")
parsed_data=[]
vacancies = soup.find_all('div', class_="serp-item")
for vacancy in vacancies:
    money = vacancy.find('span', class_="bloko-header-section-3")
    if money is None:
        money="Вилка з/п не указана"
    else:
        money=money.text
    print(money)
    temp_data={
    'tittle': vacancy.find('a', class_="serp-item__title").text,
    'money': money,
    'company': vacancy.find('a', class_="bloko-link bloko-link_kind-tertiary").text,
    'link': vacancy.find('a', class_="serp-item__title").get('href'),
    'city': vacancy.find('div', attrs={'class': 'bloko-text', 'data-qa': 'vacancy-serp__vacancy-address'}).text
    }
    parsed_data.append(temp_data)
with open('hh_python_job.json', 'w') as file:
    json.dump(parsed_data, file, indent=5, ensure_ascii=False)