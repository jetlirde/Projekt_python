from products import *

def sasia(produkt):
    if produkt.njesia_matese == 'kg':
        pyetja_sasise1 = input("Shkruani sasine ne kg! P.sh 0.30. ")
        produkt.sasia = float(pyetja_sasise1)
    else:
        pyetja_sasise2 = input("Shkruani sasine ne cope! ")
        produkt.sasia = int(pyetja_sasise2)
    return produkt.sasia

def pagesa_produktit(produkt):
    
    if produkt in pijetMeOferte:
        pagesa = produkt.pagesaPerPije()
      
    elif produkt in pijetPaOferte:
        pagesa = produkt.pagesaPijePaOferte()
      
    elif produkt in frutat:
        pagesa = produkt.pagesaPerFruta()

    return pagesa

def main():

    pyetja_produktit = input("Cfare produkti deshironi te blini? ")
    produkt = eval(pyetja_produktit)
    
    pagesa_totale = 0
  # Variabla per te ju pergjigjur programit
    pyetja = ('po', 'jo', 'ndalu')
    lajmerim = ''
    sasia(produkt)
    pagesa = pagesa_produktit(produkt)
    pagesaeProduktit = "Cmimi eshte: %.2f€. Shkruani 'po' ose 'jo' per blerje " %pagesa

    while pyetja != 'ndalu':
        blej_produktin = input(pagesaeProduktit)
      
        if blej_produktin == 'po':
          pagesa_totale = pagesa_totale + pagesa
          totaliipageses = "Totali i pageses suaj eshte: %.2f€. Shtypni OK " %pagesa_totale 
          pyetja = input("Deshironi te vazhdoni me blerjen?. Shkruani 'po' ose 'jo'! ")
          
          if pyetja == 'po':
                pyetja_produktit = input("Cfare produkti deshironi te blini? ")
                produkt = eval(pyetja_produktit)
                sasia(produkt)

                pagesa = pagesa_produktit(produkt)
                pagesaeProduktit = "Cmimi eshte: %.2f€. Shkruani 'po' ose 'jo' per blerje " %pagesa
                
          if pyetja == 'jo':
              totaliipageses = "Totali i pageses suaj eshte: %.2f€" %pagesa_totale
              cmimieshte = input(totaliipageses)
              
              break
        elif blej_produktin == 'jo':
          pyetja = input("Deshironi te vazhdoni me blerjen? Shkruani 'vazhdo' ose 'ndalu'! ")
          
          if pyetja == 'vazhdo':
              pyetja_produktit = input("Cfare produkti deshironi te blini? ")
              
              produkt = eval(pyetja_produktit)

              sasia(produkt)
              pagesa = pagesa_produktit(produkt)
              pagesaeProduktit = "Cmimi eshte: %.2f€. Shkruani 'po' ose 'jo' per blerje " %pagesa
          else:
              totaliipageses = "Totali i pageses suaj eshte: %.2f€" %pagesa_totale
              cmimieshte = input(totaliipageses)
              
              break
        else:
          lajmerim = input("Fjala nuk eshte e vlefshme! Shtypni OK! ")
          
          pyetja_produktit = input("Cfare produkti deshironi te blini? ")
              
          produkt = eval(pyetja_produktit)
          sasia(produkt)
          pagesa = pagesa_produktit(produkt)
          pagesaeProduktit = "Cmimi eshte: %.2f€. Shkruani 'po' ose 'jo' per blerje " %pagesa

main()










