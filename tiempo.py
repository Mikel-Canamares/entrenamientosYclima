class tiempo():
    
    def __init__(self, fecha,tempMin, tempMax,precip, cielo, humedadMax, humedadMin):
        self.fecha = fecha
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.precip = precip
        self.cielo = cielo
        self.humedadMax = humedadMax
        self.humedadMin = humedadMin
        
    def __repr__(self):
        return f"Fecha: {self.fecha} \nMinima:{self.tempMin} Maxima:{self.tempMax} Prov. Lluvia:{self.precip}% Humedad max:{self.humedadMax} Humedad min:{self.humedadMin}\nCielo: {self.cielo} \n"