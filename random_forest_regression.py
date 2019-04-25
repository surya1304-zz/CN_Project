def rando():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    dataset = pd.read_csv('regression_small.csv')
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values
    y = y/100000

    # Fitting Random Forest Regression to the dataset
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=1000, random_state=0)
    regressor.fit(X, y)

    # Predicting a new result
    a = np.array([6.5, 4.5])
    y_pred = regressor.predict(np.reshape(a+1, (-1, 1)))

    # Visualising the Random Forest Regression results
    X_grid = np.arange(min(X), max(X), 0.01)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = 'red')
    plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
    plt.title('Predicting the new values in the buffer')
    plt.xlabel('values in previous buffer')
    plt.ylabel('router')
    plt.show()
