

Créer les filtres suivants :
- Autres filtres : méthode unique de capteur, filtre de Kalman, filtre complémentaire

```


# Transformation du carré en cercle
if(cercle) :
    norme = sqrt(xx*xx + yy*yy)
    if(norme != 0.0) :
        if(abs(xx) > abs(yy)) :
            gain = abs(xx) / norme
        else :
            gain = abs(yy) / norme
        x = xx * gain
        y = yy * gain
    else :
        x = 0.0
        y = 0.0


# Transformation du carré en losange (car c'est comme ça)
if(losange) :
    if(xx != 0.0 or yy != 0.0) :
        if(abs(xx) > abs(yy)) :
            gain = full / abs(xx)
        else :
            gain = full / abs(yy)
        vmax = gain * (abs(xx) + abs(yy))
        x = xx * full / vmax
        y = yy * full / vmax
    else :
        x = 0.0
        y = 0.0
```