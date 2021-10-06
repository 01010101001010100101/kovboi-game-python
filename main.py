import random
a=0
b=0
c=0
x = input("Oyun kurallarını öğrenmek için x , Oyuna girmek için y tuşuna basınız")
if x == "x":
  print("Rakip oyuna sonsuz mermi ve 2 can ile başlar.Oyuncu ise 0 mermi ve 1 can ile başlar.Oyunda 3 seçenek vardır...  1.Mermi doldurma : Mermi 2 artar 2. Ateş etme : Rakibe 1 atış yapılarak 1 mermi harcanır.Rakibi yaralar.Eğer yaralı ise öldürür(oyun kazanılır)Rakip yaralıysa ve rakip de ateş ediyorsa oyun berabere biter.Rakip yaralı değilse ve rakip de ateş ediyorsa oyun kaybedilir.  3.Kalkan : Kalkan yaparak o turu pas geçebilirsin.\nOyunun amacı rakibi yaraladıktan sonra rakibe 1 atış yapabilmek.")
if x == "y":
  while(a!=50):
    pc=random.randint(1,2)
    kisi=int(input("1.mermi\n2.ateş\n3.kalkan\nmermin ={}".format(c)))
    if (kisi == 1 and pc == 2):
      print("Rakip takım ateş etmedi ve mermini doldurdun. (+2 mermi eklendi)")
      c=c+2
    elif (kisi == 2 and pc==2 and c>0 ):
     print("Rakip ateş etmedi ateş ediyorsun ve rakibi yaralıyorsun")
     b=b+1
     c=c-1
    elif (kisi== 2 and pc== 1 and b==0 and c>0 ):
     print("İki taraf da ates ediyor. Rakibin mermisi kafana  isabet ediyor ve ölüyorsun senin mermin ise onun bacağına gidiyor ve sadece  yaralanıyor.Kaybettin :c")
     c=c-1
     a=a+50
    elif (kisi==3):
      print("Tur atlatıldı ")
    elif(kisi==1 and pc==1):
     print("rakip sen mermini doldururken seni vuruyor ve ölüyorsun")
     a=a+50
    elif(kisi==2 and pc ==2 and b==1 and c>0):
     print("Yaralı rakibin acı çekerken onu vurarak öldürüyorsun.Kazandın")
     c=c-1
     a=a+50
    elif(kisi==2 and pc ==1 and b==1 and c>0):
      print("2 taraf da ates ediyor. Rakibin mermisi senin kafana isabet ediyor ve ölüyorsun.senin mermin ise rakibin bacağına isabet ediyor zaten yaralı olan rakibin bacağa isabet eden bir mermiye de ölüyor.Berabere ")
      c=c-1
      a=a+50
    elif(kisi==2 and c==0):
      print("mermi  araken öldün sj")
      a=a+50
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

