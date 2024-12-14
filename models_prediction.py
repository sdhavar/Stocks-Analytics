# ANN

def predecir_ann(datos_procesados):
    resultados = {}
    for accion, datos in datos_procesados.items():
        X_train, X_test = datos["X_train"], datos["X_test"]
        y_train, y_test = datos["y_train"], datos["y_test"]
        ann = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
        ann.fit(X_train, y_train)
        y_pred = ann.predict(X_test)
        resultados[accion] = {
            "MAE": mean_absolute_error(y_test, y_pred),
            "MSE": mean_squared_error(y_test, y_pred),
            "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
            "R2": r2_score(y_test, y_pred),
        }
    return resultados