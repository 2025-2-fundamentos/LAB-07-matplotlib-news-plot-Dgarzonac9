"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    colors = {
        "Newspaper": "gray",
        "Radio": "lightgray",
        "Television": "dimgray",
        "Internet": "tab:blue",
    }

    zorder = {
        "Newspaper": 1,
        "Radio": 1,
        "Television": 1,
        "Internet": 2,
    }

    linewidth = {
        "Newspaper": 2,
        "Radio": 2,
        "Television": 2,
        "Internet": 3,
    }

    df = pd.read_csv("files/input/news.csv", index_col=0)

    df.index = df.index.astype(int)

    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidth[col],
        )
    
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            x=first_year - 0.2,
            y=df[col][first_year],
            s=col + " " + str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        plt.text(
            x=last_year + 0.2,
            y=df[col][last_year],
            s=str(df[col][last_year]) + "% " + col,
            ha="left",
            va="center",
            color=colors[col],
        )
    # Crear directorio si no existe
    os.makedirs("files/plots", exist_ok=True)

    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.show()

if "__main__" == __name__:
    pregunta_01()