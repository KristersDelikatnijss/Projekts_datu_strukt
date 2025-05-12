# Projekta apraksts
Šī projekta ietvaros es izveidoju programmu, kas ievāc jaunākās ziņas no mājaslapas BBC, par jaunākajām ziņām pasaulē un Formula 1 jaunumiem. Programmā es izmantoju RSS plūsmas un webscraping ar BeautifulSoup. Programma izvada ziņas terminālī, kas ļauj man tieši aiziet un rakstu, kas man interesē.


# Izmantotās bibliotēkas
1. **requests:**
  Šī bibliotēka tika izmantota, lai iegūtu HTML saturu no šajā gadījumā BBC portāla, kas ļauj piekļūt mājaslapas saturam, lai pēc tam iegūtu nepieciešamo informāciju.
2. **BeautifulSoup:**
  BeautifulSoup bibliotēka tiek lielākoties lietota webscrapingam. Šajā projektā es to izmantoju, lai iegūtu ziņas/rakstus no BBC galvenās ziņu sadaļas un BBC Formula1 sadaļas. filtrējot pēc HTML elementiem(`<p>` un `<a>`), kur `<p>` satur virsrakstu un `<a>` satur linku uz rakstu.


# Datu struktūra
  Šajā projektā es izmantoju ļoti vienkāršu datu struktūru, kura saglabā katra izvadītā raksta nosaukumu, saiti uz to un avots(Šajā gadījumā vai nu BBC galvenās lapas ziņas, vai F1 sporta ziņas)
```class News:
  def __init__(self, title, link, source):
  self.title = title        # saglabā virsrakstu
  self.link = link          # saglabā linku uz rakstu
  self.source = source      # saglabā avotu (BBC News vai BBC F1, tas palīdz, jo papildinot kodu ar jauniem avotiem tiks saglabāta kārtība)
  ```


# Izmantotās metodes
  1. **def bbc_news():**
  - Iet cauri pirmajiem 15 ierakstiem un no katra iegūst virsrakstu un linku uz rakstu
  - Katrai ziņai tiek izveidots savs News objekts, kur avots ir BBC ziņas
  - Beigās funckija atgriež 15 News objektus 
  2. **f1_news():**
  - Meklē visus `<a>` tagus ar klasi ssrcss-mnw9yn-PromoLink, katram linkam meklē <p>, kurš satur virssrakstu.
  - Šī funkcija arī apstrādā tikai pirmās 15 ziņas, kur katrai izveido savu News objektu ar avotu "BBC F1"
  3. **print_news();**
  - Šīs metodes galvenais uzdevums ir apvienot bb_news sarakstu kopā ar f1_news.
  - no sākuma tā izsauc bbc_news, iegūst no tās sarakstu, tad izsauc f1_news, iegūst tās sarakstu un sāk formatēt salasāmu izvadi terminālīl.
  - izvada saturu ar print()