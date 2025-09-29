#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite (>= 1)

    Returns:
        list: la suite de Syracuse de source n jusqu'à 1 inclus
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n doit être un entier >= 1")

    l = [n]
    while l[-1] != 1:
        u = l[-1]
        if u % 2 == 0:
            l.append(u // 2)
        else:
            l.append(3 * u + 1)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol (nombre d'itérations pour atteindre 1)
    """
    if not l:
        return 0
    return max(0, len(l) - 1)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Déf.: nombre d'itérations pendant lesquelles les termes restent
    STRICTEMENT supérieurs à l'initial n, jusqu'au premier terme <= n.

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    if not l:
        return 0
    n0 = l[0]
    count = 0
    for x in l[1:]:
        if x > n0:
            count += 1
        else:
            break
    return count

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale (0 si liste vide)
    """
    return max(l) if l else 0


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
