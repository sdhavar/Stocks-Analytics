def merge_datasets(dolar_final, acciones_separadas):
    merged = {}
    for key, accion in acciones_separadas.items():
        merged[key] = pd.merge(dolar_final, accion, on='Date')
    return merged