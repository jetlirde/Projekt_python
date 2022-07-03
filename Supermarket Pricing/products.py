class Produkti:
  emri = ""
  pesha = 0
  njesia_matese = ""
  cmimi = 0
  zbritja = 0
  sasia = 0

  def __init__(self, _emri, _pesha, _njesia_matese, _cmimi,  _zbritja, _sasia):
      self.emri = _emri
      self.pesha = _pesha
      self.njesia_matese = _njesia_matese
      self.cmimi = _cmimi
      self.zbritja = _zbritja
      self.sasia = _sasia

  def pagesaPerPije(self):
    #variabla per llogaritjen e zbritjes per produktin e trete 
    zbritjaProduktiTrete = self.cmimi - (self.cmimi * (self.zbritja / 100))
    if(self.sasia < 3):
      return(self.sasia * self.cmimi)
    #P.sh per 3 produkte qe kushtojne nga 2 euro, produkti i trete llogaritet me nje perqindje te zbritur ne cmim dhe jo falas
    #(Kerkesa nr.3 ne detyre)
    elif(self.sasia == 3):
      return((self.cmimi * 2) + zbritjaProduktiTrete)  
    #Nese sasia eshte me e madhe se 3, 3 produkte llogariten me oferte, kurse te tjerat llogariten me cmimin e nje produkti vec e vec
    #Ky kusht vlen vetem per produktet qe kur modulohen me 3, nuk japin rezultatin 0. P.sh 5 produkte
    #(Kerkesa nr.1 ne detyre)
    elif(self.sasia > 3 and self.sasia % 3 != 0):
      return((self.cmimi * 2) + zbritjaProduktiTrete + ((self.sasia - 3)) * self.cmimi)  
    #nese produktet perfshihen ne oferte, psh 6 produkte, 9 produkte
    elif(self.sasia % 3 == 0):
      return(((self.cmimi * 2) + zbritjaProduktiTrete)*(self.sasia/3)) 
    
  def pagesaPijePaOferte(self):
      return(self.sasia * self.cmimi)

  def pagesaPerFruta(self):
    #Sasia e dhene nga perdoruesi shumezohet me cmimin per kilogram
    #Kerkesa nr.2 e detyres
    return(self.sasia * self.cmimi)

#objektet e produkteve     
molla = Produkti("Molla", 1,"kg", 1.50, 0, 0)
dardha = Produkti("Dardha", 1, "kg", 2.00, 0, 0)
kumbulla = Produkti("Kumbulla", 1, "kg", 1.30, 0, 0)
qershi = Produkti("Qershi", 1, "kg", 1.70, 0, 0)
pjeshka = Produkti("Pjeshka", 1, "kg", 1.20, 0, 0)
fanta = Produkti("Fanta", 2, "l", 1.80, 20, 0)
cocacola = Produkti("Coca-Cola", 2, "l", 1.50, 40, 0)
sprite = Produkti ("Sprite", 1.5, "l", 1.30, 30, 0)
aloevera = Produkti ("Aloe Vera", 1.5, "l", 1.10, 30, 0)
icetea = Produkti ("Ice Tea", 1.5, "l", 1.40, 30, 0)


pijetMeOferte = [fanta, cocacola, aloevera]
pijetPaOferte = [sprite, icetea]
frutat = [molla, dardha, kumbulla, qershi, pjeshka]


    


    
