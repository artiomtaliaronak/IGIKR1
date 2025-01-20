import re
from collections import Counter 

def stat(text):
    wc = Counter(re.sub(r'[^\w\s]', '', text.lower()).split())
    l = [len(re.findall(r'\w+', s)) for s in re.split(r'[.!?]', text)]
    avgwc = sum(l) / len(l) if l else 0
    l.sort()
    medianwc = l[len(l) // 2] if l else 0
    return wc, avgwc, medianwc

def ngrams(text, n, k):
    w = re.sub(r'[^\w\s]', '', text.lower()) .split()
    return Counter([' '.join(w[i:i + n]) for i in range(len(w) - n + 1)]).most_common(k) 

text = "Lorem ipsum dolor sit amet, illud quidam convenire te pri, mea sanctus repudiare maiestatis ad, eu vis debitis inermis. Id quidam pertinacia his, et omnesque abhorreant eam, eu persius tractatos vis. His case tota timeam in, ex congue laoreet nec. Stet mandamus ei pri, ut mei alienum noluisse definitionem. Sea veritus appareat ex, te eum veri persecuti. Vis id esse postulant gubergren, vix mediocrem ocurreret evertitur ex.Vis in quot periculis incorrupte. Ei duo epicurei salutatus, te feugiat molestiae pro. Nec ne menandri sententiae scriptorem, summo lobortis has no. Ex est diam adolescens neglegentur, per sumo noluisse id.Id natum impedit sit, ferri dolore persequeris pro cu. Usu oblique assentior an, eu his tritani inimicus adolescens. Alterum fabulas euripidis ad has, mucius dissentias et mel. Nulla oblique signiferumque ei sea. His mutat debet eleifend ut, laoreet suscipit ne quo.At eam assum vitae labores. His postulant sadipscing no, ad unum errem vel. Ne pro autem aliquid, cu augue tacimates conclusionemque pro. Qui summo paulo recusabo te. Ut natum affert pri, est et sonet intellegam.Nobis dicam vituperatoribus vix te. Has legere albucius concludaturque no, no movet accusamus incorrupte est. Ut ridens tritani scripserit vix, eu vel dicit verear insolens. Sea ei quod iusto blandit.An sit dolor iisque salutandi, consulatu sententiae vix ea. At quo brute conceptam vituperatoribus. Vim fierent corrumpit temporibus ne, cum impetus deserunt ut. Eum laudem eloquentiam te, pri eu amet nullam mentitum.Eu vel saepe voluptaria. Usu et persius iracundia. Eam homero legendos interpretaris eu, vel ne voluptaria definitiones. Eum cu alii minim suscipit, eu maiorum eloquentiam usu, sed laudem intellegam at. Et sed esse mediocrem eloquentiam, verear fabellas scribentur ad eum.Ut forensibus rationibus mei. An illum equidem propriae usu, duis fugit postea sed te, in dolorum suscipiantur vix. Dico suas est at, sit civibus explicari in, cibo nemore quaeque ad sed. Modo justo et cum, munere disputando vis ad. Nonumes appareat no has.Usu ad wisi denique, ad simul tempor impetus pro. Epicurei neglegentur et sit, vim at velit saperet. An cum oportere erroribus scriptorem, elit intellegebat duo ad. Vis eu repudiare definitionem.Ex eam vero nusquam, timeam debitis ocurreret mel ex. Vim ei illud dolorum, ad doming periculis dissentiet sea, usu congue consetetur constituam et. Mundi graeco eam in, explicari persequeris ei eam, pri ea euripidis signiferumque. Vitae aeterno laoreet has id."
n = int(input("N: ") or 4)
k = int(input("K: ") or 10)
wc, avgwc, medianwc = stat(text)
print(f"\nAverage word count: {avgwc:.2f}")
print(f"Median word count: {medianwc}")
print(f"Top-{k} {n}-grams:") 
for n_gram, count in ngrams(text, n, k) :
    print(f"{n_gram}: {count}") 
print("Word count: ", wc)

