import pandas as pd
import gspread_pandas

path = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vScsLKFhcW1iLORA-zePnDSoZfat-BNSeKt1c1XGoNAVoGP7Xqj5OE8q553A-QvrzvpHeQTvv8DBphW/pub?output=csv'
df0 = pd.read_csv(path, parse_dates=['Зарегистрирован'])

df = df0.copy()

def udf_phone(phone):
    if phone.startswith('9'):
        return '7' + phone
    elif phone.startswith('8'):
        return phone.replace('8', '7', 1)
    else:
        return phone
    
df1 = (df
    .assign(Источник = 'Визитки', #df.Роль.apply(lambda x: 'Клуб риелторов' if x == 'Агентство недвижимости' else 'Визитки'),
            Email = df['E-mail'].str.lower(),
            ФИО = df[['Фамилия', 'Имя', 'Отчество']].apply(' '.join, 1),
            мобильныйтелефон = df['Номер телефона'].str.replace('[\s"+()-]', '')
                                                   .apply(udf_phone),
            Тип = 'Контактное лицо',
            Типконтактноголица = df.Роль.apply(lambda x: 'Частный маклер' if x == 'Частный риелтор' else x),
            Контрагент = df.Роль.apply(lambda x: '' if x == 'Частный риелтор' else 'Уточнить, ручная загрузка из Excel') 
           )
    .drop(columns='Город') 
    .rename(columns={'Событие': 'Комментарий к источнику', 
                     'Зарегистрирован': 'Дата создания',
                     'Город.1': 'Город',
                     'Типконтактноголица': 'Тип контактного лица'
            })
    .loc[:, ['Источник', 'Комментарий к источнику', 'Дата создания', 'Email', 'ФИО', 
             'мобильныйтелефон', 'Город', 'Тип', 'Тип контактного лица', 'Контрагент']]    
)

df_an = df1.query('`Тип контактного лица` == "Агентство недвижимости"')
df_others = df1.query('`Тип контактного лица` != "Агентство недвижимости"')

config = gspread_pandas.conf.get_config('/home/yakovlevaev/', 'm2-main-cd9ed0b4e222.json') 

udf_sheet = lambda sheet: gspread_pandas.Spread('1-NenYnXa7K9CL6iXNauJU9G_BDveGS_vlGTvXJ2PjM8', 
                                                sheet=sheet, config=config, create_sheet=True)

udf_to_sheet = lambda df, sheet: sheet.df_to_sheet(df, replace=True, index=False)

an = udf_sheet('АН')
others = udf_sheet('ЧМАК и др')

udf_to_sheet(df_an, an)
udf_to_sheet(df_others, others)