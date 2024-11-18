# PID parallèle (avant traitement) : U(t) = Kp*E(t) + Ki*intégrale E(t) + Kd*dérivée E(t)
# 
# Modèles de PID continus (les 3 sont équivalentes mathématiquement)
# - PID parallele                : H(p) = Kp    + Ki/p    + Kd*p
# - PID série                    : H(p) = K1*(1 + K2/p)(1 + K3*p)
# - PID standard / mixte / idéal : H(p) = Kp*(1 + K4/p    + K5*p)
#
# Estimations de l'intégrale
# - Approximation rectangulaire devancée : Tz/(z-1)
# - Approximation rectangulaire          : T/(z-1)
# - Approximation trapézoïdale           : T(z+1)/2(z-1)
#
# Estimation de la dérivée  :
# - Approximation par défaut : (z-1)/T
# - d'autres existent ...
#
# Implémentations PID discrets
# 
# 1. PID série minimaliste (sans calcul - http://www.ferdinandpiette.com/)
# - Equations :
#   commande = Kp*erreur + Ki*dt*somme_erreurs + Kd/dt*(erreur - erreur_précédente)
#
# 2. PID mixte (https://sikula-robotik.desbwa.org)
# - Intégrale : Approximation trapézoïdale
# - Dérivée   : Approximation par défaut
# - Equations :
#   q0 = Kp * (Ki*dt/2+Kd/dt+1)
#   q1 = Kp * (Ki*dt/2-Kd/dt*2-1)
#   q2 = Kp * Kd/dt
#   y += q0 * e + q1 * e_1 + q2 * e_2
#
# Commandes
# - PID.stop()     : Désactivation du PID
# - PID.start()    : Activation du PID
# - PID.reset()    : Reset des variables du PID
# - PID.output(dt) : Fonction à appeler pour avoir la sortie calculée en fonction du pas dt si PID actif
#
# Réglages :
# - Paramètres :
#   - PID.par.kp  : Regle le parametre proportionnel (PID parallèle)
#   - PID.par.ki  : Regle le parametre intégrateur   (PID parallèle)
#   - PID.par.kd  : Regle le parametre proportionnel (PID parallèle)
# - Paramètres
#   - PID.fct.i   : fonction input    à renseigner pour avoir la valeur d'entrée
#   - PID.fct.c   : fonction commande à renseigner pour avoir la commande d'entrée
# - Flag
#   - flag.modele : modèle de PID numérique à utiliser
#
# D'autres possibilités existent :
# - https://www.jumo.fr/web/services/faq/controller/pid-controller
# - https://engineering.stackexchange.com/questions/26537/what-is-a-definitive-discrete-pid-controller-equation
# - https://www.acsysteme.com/fr/ressources-documentaires/pid-serie-ou-parallele-quelle-structure-choisir/
# - https://public.iutenligne.net/automatique-et-automatismes-industriels/duplaix/mau3/RegIndus/RegPid.html
# - https://fr.wikipedia.org/wiki/R%C3%A9gulateur_PID
# - http://www.ferdinandpiette.com/blog/2011/08/implementer-un-pid-sans-faire-de-calculs/
# - https://sikula-robotik.desbwa.org/connaissances/asserv/pidnum.php
# - https://www.scilab.org/discrete-time-pid-controller-implementation
#
# Autres filtres : méthode unique de capteur, filtre de Kalman, filtre complémentaire

from .limit import cut_upper_aera
from toolbox.others import Parameter


class PID():
    def __init__(self, parameter=(1, 0, 0), fct=(None, None), modele="minimaliste", limite=0):
        self.flag = Parameter()
        self.flag.modele  = modele
        self.flag._start  = False   # Caché
        
        self.par = Parameter()
        self.par.kp = parameter[0]
        self.par.ki = parameter[1]
        self.par.kd = parameter[2]
        
        self.fct = Parameter()
        self.fct.i       = fct[0]
        self.fct.c       = fct[1]
        self.fct._modele = None     # Caché
        
        self._limite     = limite
        self._PID_modele = {
            "minimaliste" : self._minimaliste,
            "serie"       : None,
            "parallele"   : self._parallele,
            "mixte"       : self._mixte,
            }
        
        self.reset()
    
    
    def stop(self):
        self.flag._start = False
    
    
    def reset(self):
        if self.flag.modele not in self._PID_modele :
            self.flag.modele = "minimaliste"
        
        self.fct._modele = self._PID_modele[self.flag.modele]
        self._somme_e = 0   # Somme des erreurs  
        
        self._c = [0]*3     # Valeurs input
        self._i = [0]*3     # Valeurs commande
        self._o = [0]*3     # Valeurs output
        self._e = [0]*3     # Valeurs erreur (entre input et commande)
    
    
    def start(self):
        self.flag._start = True
        
        # Vérification des parametres
        try :
            self.fct.i(0)
            self.fct.c(0)
        except :
            pass
        
        self.reset()
        return self.flag._start  
    
    
    # Calcul du PID lorsque appelé
    def output(self, dt, in_=None, cmd=None):
        if self.flag._start :
            if dt >= 0.001 :
                # Ajout des nouvelles valeurs d'entrée
                self._c.insert(0, cmd if cmd != None else self.fct.c(dt))
                self._i.insert(0, in_ if in_ != None else self.fct.i(dt))
                self._e.insert(0, self._c[0] - self._i[0])

                # Ajout de la nouvelle valeur de sortie
                output = self.fct._modele(dt)
                if self._limite :
                    output = cut_upper_aera(self.fct._modele(dt), self._limite)
                self._o.insert(0, output)
                
                # Retrait des anciennes valeurs d'entrée / de sortie
                self._c.pop()
                self._i.pop()
                self._e.pop()
                self._o.pop()
                
        return self._o[0]
    
    
    def _minimaliste(self, dt): 
        # Mise à jour des variables intermédiaires
        delta_e        = self._e[0] - self._e[1]
        self._somme_e += self._e[0]
        if self._limite :
            self._somme_e  = cut_upper_aera(self._somme_e, self._limite)
        
        # Correction P I D
        p = self.par.kp        # Correction kp sur l'erreur
        i = self.par.ki * dt   # Correction ki sur l'intégrale de l'erreur
        d = self.par.kd / dt   # Correction kd sur la dérivée de l'erreur
        
        return p*self._e[0] + i*self._somme_e + d*delta_e 
    
    
    def _parallele(self, dt):
        # Mise à jour des variables intermédiaires
        p = self.par.kp
        i = self.par.ki * dt / 2
        d = self.par.kd / dt
        
        # Calcul des coefficients
        q0 =  p + i + d
        q1 = -p + i - d*2
        q2 =  d
        
        return self._o[0] + q0*self._e[0] + q1*self._e[1] + q2*self._e[2]
    
    
    def _mixte(self, dt):
        # Mise à jour des variables intermédiaires
        p = self.par.kp
        i = self.par.ki * dt / 2
        d = self.par.kd / dt
        
        # Calcul des coefficients
        q0 = p*(i + d   + 1)
        q1 = p*(i - d*2 - 1)
        q2 = p*d
        
        return self._o[0] + q0*self._e[0] + q1*self._e[1] + q2*self._e[2]


if __name__ == '__main__':
    # Parametres a modifier 
    dt         = 0.01           # 0.001s - 1s
    pid_modele = "parallele"    # parallele, mixte, minimaliste
    pid_coeffs = (5, 50, 0.1)   # marche pour tous les modeles
    limite     = 10             # 10 au lieu de 1 car il faut laisser de la marge de dépassement au modele
    
    # A ne pas modifier
    #
    # ############ Plan systeme 1 ############
    # cmd  -----V
    # etat -->i E o--> etat
    #
    # ############ Plan systeme 2 ############
    # cmd  -----V
    # etat -->i PID
    #           V
    # etat -->i E o--> etat
    
    # cmd
    def commande(dt):
        return 1
    
    # etat
    etat_systeme_1 = 0
    def input_1(dt):
        return etat_systeme_1
    
    etat_systeme_2 = 0
    def input_2(dt):
        return etat_systeme_2
    
    # systeme E
    def systeme(in_, cmd_):
        return cmd_ + (in_ - cmd_) * 0.9900498
    
    # PID
    pid = PID(parameter=pid_coeffs, fct=(input_2, commande), modele=pid_modele, limite=limite)
    pid.start()
    
    # simulation
    for i in range(0, 5000, int(dt*1000)):
        if i % 200 == 0 :
            print(etat_systeme_1, etat_systeme_2)
        etat_systeme_1 = systeme(input_1(dt), commande(dt))
        etat_systeme_2 = systeme(input_2(dt), pid.output(dt))
        
