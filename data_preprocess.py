def preprocesar_datos(merged_data):
    datos_procesados = {}
    for key, df in merged_data.items():
        X = df[['Valor Dolar']]
        y = df[key]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        datos_procesados[key] = {
            "X_train": X_train_scaled,
            "X_test": X_test_scaled,
            "y_train": y_train,
            "y_test": y_test,
        }
    return datos_procesados