{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8544e74",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:16:03.853421Z",
     "start_time": "2022-01-26T13:16:02.629321Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import gspread_pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "66f46968",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:17.928927Z",
     "start_time": "2022-01-26T13:29:15.470021Z"
    }
   },
   "outputs": [],
   "source": [
    "path = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vScsLKFhcW1iLORA-zePnDSoZfat-BNSeKt1c1XGoNAVoGP7Xqj5OE8q553A-QvrzvpHeQTvv8DBphW/pub?output=xlsx'\n",
    "df0 = pd.read_excel(path, parse_dates=['Зарегистрирован'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ed1468c5",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:19.378813Z",
     "start_time": "2022-01-26T13:29:19.340435Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Событие</th>\n",
       "      <th>Город</th>\n",
       "      <th>Адрес</th>\n",
       "      <th>Дата</th>\n",
       "      <th>Заказ</th>\n",
       "      <th>Код</th>\n",
       "      <th>Штрихкод</th>\n",
       "      <th>Зарегистрирован</th>\n",
       "      <th>Оплатил</th>\n",
       "      <th>Сумма</th>\n",
       "      <th>...</th>\n",
       "      <th>Отчество</th>\n",
       "      <th>Город.1</th>\n",
       "      <th>Роль</th>\n",
       "      <th>Название компании</th>\n",
       "      <th>Рекламная кампания</th>\n",
       "      <th>Источник трафика</th>\n",
       "      <th>Канал регистрации</th>\n",
       "      <th>GA ClientID</th>\n",
       "      <th>Пришёл</th>\n",
       "      <th>Комментарий</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>Без города</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2022-01-19 10:00:00</td>\n",
       "      <td>40497320</td>\n",
       "      <td>51733126:21940606</td>\n",
       "      <td>1000219406067</td>\n",
       "      <td>2022-01-13 13:35:10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Олеговна</td>\n",
       "      <td>Екатеринбург</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Сеть офисов недвижимости \"Миэль\"</td>\n",
       "      <td>Produkt</td>\n",
       "      <td>M2_CRM</td>\n",
       "      <td>Email</td>\n",
       "      <td>1.832388e+09</td>\n",
       "      <td>Нет</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>Без города</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2022-01-19 10:00:00</td>\n",
       "      <td>40497334</td>\n",
       "      <td>51733150:22390530</td>\n",
       "      <td>1000223905303</td>\n",
       "      <td>2022-01-13 13:35:47</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Михайловна</td>\n",
       "      <td>Санкт петербург</td>\n",
       "      <td>Частный риелтор</td>\n",
       "      <td>Диалог-СПб</td>\n",
       "      <td>Produkt</td>\n",
       "      <td>M2_CRM</td>\n",
       "      <td>Email</td>\n",
       "      <td>4.673389e+08</td>\n",
       "      <td>Нет</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>Без города</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2022-01-19 10:00:00</td>\n",
       "      <td>40497337</td>\n",
       "      <td>51733154:38598784</td>\n",
       "      <td>1000385987841</td>\n",
       "      <td>2022-01-13 13:35:51</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Вячеславовна</td>\n",
       "      <td>Егорьевск</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Сто ключей</td>\n",
       "      <td>Produkt</td>\n",
       "      <td>M2_CRM</td>\n",
       "      <td>Email</td>\n",
       "      <td>6.064615e+07</td>\n",
       "      <td>Нет</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>Без города</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2022-01-19 10:00:00</td>\n",
       "      <td>40497339</td>\n",
       "      <td>51733156:71268606</td>\n",
       "      <td>1000712686065</td>\n",
       "      <td>2022-01-13 13:35:58</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Владимировна</td>\n",
       "      <td>Новосибирск</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Жилфонд</td>\n",
       "      <td>Produkt</td>\n",
       "      <td>M2_CRM</td>\n",
       "      <td>Email</td>\n",
       "      <td>1.640624e+09</td>\n",
       "      <td>Нет</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>Без города</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2022-01-19 10:00:00</td>\n",
       "      <td>40497345</td>\n",
       "      <td>51733191:43542048</td>\n",
       "      <td>1000435420489</td>\n",
       "      <td>2022-01-13 13:36:05</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>Павловна</td>\n",
       "      <td>Санкт-Петербург</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>DVORETSKY Estate</td>\n",
       "      <td>Produkt</td>\n",
       "      <td>M2_CRM</td>\n",
       "      <td>Email</td>\n",
       "      <td>7.075727e+08</td>\n",
       "      <td>Нет</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 29 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Событие       Город  Адрес  \\\n",
       "0  Ипотечный брокер: как работает сервис и для че...  Без города    NaN   \n",
       "1  Ипотечный брокер: как работает сервис и для че...  Без города    NaN   \n",
       "2  Ипотечный брокер: как работает сервис и для че...  Без города    NaN   \n",
       "3  Ипотечный брокер: как работает сервис и для че...  Без города    NaN   \n",
       "4  Ипотечный брокер: как работает сервис и для че...  Без города    NaN   \n",
       "\n",
       "                  Дата     Заказ                Код       Штрихкод  \\\n",
       "0  2022-01-19 10:00:00  40497320  51733126:21940606  1000219406067   \n",
       "1  2022-01-19 10:00:00  40497334  51733150:22390530  1000223905303   \n",
       "2  2022-01-19 10:00:00  40497337  51733154:38598784  1000385987841   \n",
       "3  2022-01-19 10:00:00  40497339  51733156:71268606  1000712686065   \n",
       "4  2022-01-19 10:00:00  40497345  51733191:43542048  1000435420489   \n",
       "\n",
       "      Зарегистрирован  Оплатил  Сумма  ...      Отчество          Город.1  \\\n",
       "0 2022-01-13 13:35:10      NaN    NaN  ...      Олеговна     Екатеринбург   \n",
       "1 2022-01-13 13:35:47      NaN    NaN  ...    Михайловна  Санкт петербург   \n",
       "2 2022-01-13 13:35:51      NaN    NaN  ...  Вячеславовна        Егорьевск   \n",
       "3 2022-01-13 13:35:58      NaN    NaN  ...  Владимировна      Новосибирск   \n",
       "4 2022-01-13 13:36:05      NaN    NaN  ...      Павловна  Санкт-Петербург   \n",
       "\n",
       "                     Роль                 Название компании  \\\n",
       "0  Агентство недвижимости  Сеть офисов недвижимости \"Миэль\"   \n",
       "1         Частный риелтор                        Диалог-СПб   \n",
       "2  Агентство недвижимости                        Сто ключей   \n",
       "3  Агентство недвижимости                           Жилфонд   \n",
       "4  Агентство недвижимости                  DVORETSKY Estate   \n",
       "\n",
       "  Рекламная кампания Источник трафика Канал регистрации   GA ClientID Пришёл  \\\n",
       "0            Produkt           M2_CRM             Email  1.832388e+09    Нет   \n",
       "1            Produkt           M2_CRM             Email  4.673389e+08    Нет   \n",
       "2            Produkt           M2_CRM             Email  6.064615e+07    Нет   \n",
       "3            Produkt           M2_CRM             Email  1.640624e+09    Нет   \n",
       "4            Produkt           M2_CRM             Email  7.075727e+08    Нет   \n",
       "\n",
       "  Комментарий  \n",
       "0         NaN  \n",
       "1         NaN  \n",
       "2         NaN  \n",
       "3         NaN  \n",
       "4         NaN  \n",
       "\n",
       "[5 rows x 29 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df0.copy()\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a73b2088",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:16:29.874796Z",
     "start_time": "2022-01-26T13:16:29.859409Z"
    }
   },
   "outputs": [],
   "source": [
    "def udf_phone(phone):\n",
    "    if phone.startswith('9'):\n",
    "        return '7' + phone\n",
    "    elif phone.startswith('8'):\n",
    "        return phone.replace('8', '7', 1)\n",
    "    else:\n",
    "        return phone"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "28fed65f",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:23.002611Z",
     "start_time": "2022-01-26T13:29:22.950717Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-17-076e4bbb7557>:5: FutureWarning: The default value of regex will change from True to False in a future version.\n",
      "  мобильныйтелефон = df['Номер телефона'].str.replace('[\\s\"+()-]', '')\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Источник</th>\n",
       "      <th>Комментарий к источнику</th>\n",
       "      <th>Дата создания</th>\n",
       "      <th>Email</th>\n",
       "      <th>ФИО</th>\n",
       "      <th>мобильныйтелефон</th>\n",
       "      <th>Город</th>\n",
       "      <th>Тип</th>\n",
       "      <th>Тип контактного лица</th>\n",
       "      <th>Контрагент</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Визитки</td>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>2022-01-13 13:35:10</td>\n",
       "      <td>ekaterinburg@miel.ru</td>\n",
       "      <td>Дрокова Екатерина Олеговна</td>\n",
       "      <td>79089208050</td>\n",
       "      <td>Екатеринбург</td>\n",
       "      <td>Контактное лицо</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Уточнить, ручная загрузка из Excel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Визитки</td>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>2022-01-13 13:35:47</td>\n",
       "      <td>viktoria7507@yandex.ru</td>\n",
       "      <td>Ломакина Виктория Михайловна</td>\n",
       "      <td>79119233838</td>\n",
       "      <td>Санкт петербург</td>\n",
       "      <td>Контактное лицо</td>\n",
       "      <td>Частный маклер</td>\n",
       "      <td></td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Визитки</td>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>2022-01-13 13:35:51</td>\n",
       "      <td>1745749@100kl.ru</td>\n",
       "      <td>Яснова Кристина Вячеславовна</td>\n",
       "      <td>79851745749</td>\n",
       "      <td>Егорьевск</td>\n",
       "      <td>Контактное лицо</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Уточнить, ручная загрузка из Excel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Визитки</td>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>2022-01-13 13:35:58</td>\n",
       "      <td>kitova.s@jilfond.ru</td>\n",
       "      <td>Китова Светлана Владимировна</td>\n",
       "      <td>79831287704</td>\n",
       "      <td>Новосибирск</td>\n",
       "      <td>Контактное лицо</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Уточнить, ручная загрузка из Excel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Визитки</td>\n",
       "      <td>Ипотечный брокер: как работает сервис и для че...</td>\n",
       "      <td>2022-01-13 13:36:05</td>\n",
       "      <td>info@daestate.ru</td>\n",
       "      <td>Полторанина Юлия Павловна</td>\n",
       "      <td>79814627964</td>\n",
       "      <td>Санкт-Петербург</td>\n",
       "      <td>Контактное лицо</td>\n",
       "      <td>Агентство недвижимости</td>\n",
       "      <td>Уточнить, ручная загрузка из Excel</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Источник                            Комментарий к источнику  \\\n",
       "0  Визитки  Ипотечный брокер: как работает сервис и для че...   \n",
       "1  Визитки  Ипотечный брокер: как работает сервис и для че...   \n",
       "2  Визитки  Ипотечный брокер: как работает сервис и для че...   \n",
       "3  Визитки  Ипотечный брокер: как работает сервис и для че...   \n",
       "4  Визитки  Ипотечный брокер: как работает сервис и для че...   \n",
       "\n",
       "        Дата создания                   Email                           ФИО  \\\n",
       "0 2022-01-13 13:35:10    ekaterinburg@miel.ru    Дрокова Екатерина Олеговна   \n",
       "1 2022-01-13 13:35:47  viktoria7507@yandex.ru  Ломакина Виктория Михайловна   \n",
       "2 2022-01-13 13:35:51        1745749@100kl.ru  Яснова Кристина Вячеславовна   \n",
       "3 2022-01-13 13:35:58     kitova.s@jilfond.ru  Китова Светлана Владимировна   \n",
       "4 2022-01-13 13:36:05        info@daestate.ru     Полторанина Юлия Павловна   \n",
       "\n",
       "  мобильныйтелефон            Город              Тип    Тип контактного лица  \\\n",
       "0      79089208050     Екатеринбург  Контактное лицо  Агентство недвижимости   \n",
       "1      79119233838  Санкт петербург  Контактное лицо          Частный маклер   \n",
       "2      79851745749        Егорьевск  Контактное лицо  Агентство недвижимости   \n",
       "3      79831287704      Новосибирск  Контактное лицо  Агентство недвижимости   \n",
       "4      79814627964  Санкт-Петербург  Контактное лицо  Агентство недвижимости   \n",
       "\n",
       "                           Контрагент  \n",
       "0  Уточнить, ручная загрузка из Excel  \n",
       "1                                      \n",
       "2  Уточнить, ручная загрузка из Excel  \n",
       "3  Уточнить, ручная загрузка из Excel  \n",
       "4  Уточнить, ручная загрузка из Excel  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = (df\n",
    "    .assign(Источник = 'Визитки', #df.Роль.apply(lambda x: 'Клуб риелторов' if x == 'Агентство недвижимости' else 'Визитки'),\n",
    "            Email = df['E-mail'].str.lower(),\n",
    "            ФИО = df[['Фамилия', 'Имя', 'Отчество']].apply(' '.join, 1),\n",
    "            мобильныйтелефон = df['Номер телефона'].str.replace('[\\s\"+()-]', '')\n",
    "                                                   .apply(udf_phone),\n",
    "            Тип = 'Контактное лицо',\n",
    "            Типконтактноголица = df.Роль.apply(lambda x: 'Частный маклер' if x == 'Частный риелтор' else x),\n",
    "            Контрагент = df.Роль.apply(lambda x: '' if x == 'Частный риелтор' else 'Уточнить, ручная загрузка из Excel') \n",
    "           )\n",
    "    .drop(columns='Город') \n",
    "    .rename(columns={'Событие': 'Комментарий к источнику', \n",
    "                     'Зарегистрирован': 'Дата создания',\n",
    "                     'Город.1': 'Город',\n",
    "                     'Типконтактноголица': 'Тип контактного лица'\n",
    "            })\n",
    "    .loc[:, ['Источник', 'Комментарий к источнику', 'Дата создания', 'Email', 'ФИО', \n",
    "             'мобильныйтелефон', 'Город', 'Тип', 'Тип контактного лица', 'Контрагент']]    \n",
    ")\n",
    "\n",
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7b85ad81",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:25.938132Z",
     "start_time": "2022-01-26T13:29:25.917998Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Источник                           object\n",
       "Комментарий к источнику            object\n",
       "Дата создания              datetime64[ns]\n",
       "Email                              object\n",
       "ФИО                                object\n",
       "мобильныйтелефон                   object\n",
       "Город                              object\n",
       "Тип                                object\n",
       "Тип контактного лица               object\n",
       "Контрагент                         object\n",
       "dtype: object"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b324edee",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:27.693398Z",
     "start_time": "2022-01-26T13:29:27.677064Z"
    }
   },
   "outputs": [],
   "source": [
    "df_an = df1.query('`Тип контактного лица` == \"Агентство недвижимости\"')\n",
    "df_others = df1.query('`Тип контактного лица` != \"Агентство недвижимости\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "447b8c88",
   "metadata": {},
   "outputs": [],
   "source": [
    "config = gspread_pandas.conf.get_config('/home/web_analytics/', 'm2-main-cd9ed0b4e222.json') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a29ba87d",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:16:40.258267Z",
     "start_time": "2022-01-26T13:16:40.248294Z"
    }
   },
   "outputs": [],
   "source": [
    "udf_sheet = lambda sheet: gspread_pandas.Spread('1-NenYnXa7K9CL6iXNauJU9G_BDveGS_vlGTvXJ2PjM8', \n",
    "                                                sheet=sheet, config=config, create_sheet=True)\n",
    "\n",
    "udf_to_sheet = lambda df, sheet: sheet.df_to_sheet(df, replace=True, index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1bcdabca",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:35.867210Z",
     "start_time": "2022-01-26T13:29:30.496361Z"
    }
   },
   "outputs": [],
   "source": [
    "an = udf_sheet('АН')\n",
    "others = udf_sheet('ЧМАК и др')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "10f23906",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T13:29:43.315738Z",
     "start_time": "2022-01-26T13:29:36.794281Z"
    }
   },
   "outputs": [],
   "source": [
    "udf_to_sheet(df_an, an)\n",
    "udf_to_sheet(df_others, others)"
   ]
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
