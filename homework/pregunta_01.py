# %%
# Cargue los datos de las tabla "files/input/drivers.csv" a una variable llamada
# drivers, usando pandas 
import pandas as pd
drivers = pd.read_csv("files/input/drivers.csv")


# %%
# Cargue los datos de las tabla "files/input/timesheet.csv" a una variable llamada
# timesheet, usando pandas
timesheet = pd.read_csv("files/input/timesheet.csv")

# %%
# Calcule el promedio de las columnas "hours-logged" y "miles-logged" en la 
# tabla "timesheet", agrupando los resultados por cada conductor (driverId).
avg_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].mean().reset_index()
avg_timesheet

# %%
# Cree una tabla llamada "timesheet_with_means" basada en la tabla "timesheet", 
# agregando una columna con el promedio de "hours-logged" para cada conductor (driverId).
timesheet_with_means = timesheet.merge(avg_timesheet[["driverId", "hours-logged"]], on="driverId", suffixes=("", "_mean"))

# %%
# Cree una tabla llamada "timesheet_below" a partir de "timesheet_with_means", filtrando los registros 
# donde "hours-logged" sea menor que "mean_hours-logged".
timesheet_below = timesheet_with_means[timesheet_with_means["hours-logged"] < timesheet_with_means["hours-logged_mean"]]
timesheet_below

# %%
