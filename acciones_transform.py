def transformar_acciones(file_path):
    acciones_temp = pd.read_csv(file_path)
    acciones_temp['Date'] = pd.to_datetime(acciones_temp['Date'])

    acciones_filtered = acciones_temp[
        (acciones_temp['Date'] >= '2015-01-01') & (acciones_temp['Date'] <= '2022-07-20')
    ]
    acciones_filtered.to_csv('mag7_final.csv', index=False)

    acciones = acciones_filtered.sort_values(by='Date', ascending=True).reset_index(drop=True)
    acciones.set_index('Date', inplace=True)

    for column in acciones.columns:
        acciones[column] = pd.to_numeric(acciones[column], errors='coerce')

    return acciones.resample('ME').mean()