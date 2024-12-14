def transformar_dolar(file_path):
    dolar_temp = pd.read_csv(file_path)
    dolar_temp['VIGENCIADESDE'] = pd.to_datetime(dolar_temp['VIGENCIADESDE'], format='%d/%m/%Y')

    df_filtered = dolar_temp[dolar_temp['VIGENCIADESDE'].dt.year >= 2015]
    df_filtered.to_csv('TRM_final.csv', index=False)

    dolar = df_filtered.sort_values(by='VIGENCIADESDE', ascending=True).reset_index(drop=True)
    dolar = dolar.rename(columns={'VIGENCIADESDE': 'Date'}).set_index('Date')

    for column in dolar.columns:
        dolar[column] = pd.to_numeric(dolar[column], errors='coerce')

    dolar_final = dolar.resample('ME').mean().drop('VIGENCIAHASTA', axis=1)
    return dolar_final.rename(columns={'VALOR': 'Valor Dolar'})