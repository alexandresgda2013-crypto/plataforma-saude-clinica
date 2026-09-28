import json, re, urllib.request, xml.etree.ElementTree as ET, unicodedata

GRP = {
'HIST': ['4863731','10775017','9818625','8852528','10775019','12953623','36000248','26043325','37857415','19498050'],
'5HT': ['19428959','27623971','16154547','17971260','31120232','19423077','24936175','24337875','23492554','28232871','25823514','33651238','33673205','33672070','30144453','30430940','27353308','9844013','22832966','28920103','26083190'],
'DEPL':['11331552','11063917','12431859','11922881','8988796','15131521','14647394','14731308','12955284','33574223','37430145','3275471','15450786'],
'DA':  ['16566899','20603146','26323245','29106542','29573379','29309799','26525751','18654637','33631251','36889362','28870407','37301129','32363761','23711983'],
'LC':  ['12668290','28367128','19960531','39427811','41167443','42332025','40219735','18255055','20210846','28596922','26607253','27616990','36289638','37139472','40442382','41938091','26212712','28708061','29341884','41066175','41000807','38155473','29593511','31801809','41225565','33911187'],
'INF': ['27480574','39694342','34265868','34285088'],
'MOD': ['29033793','28926161','38816586','42198336','25813654'],
'B2X': ['7899535'],
}
ALL=[p for g in GRP.values() for p in g]
EXC_TARDIA='39696597'  # Evans 2024 = modelo 5XFAD Alzheimer -> fora de escopo permanente (corte no abstract)
assert len(ALL)==94 and len(set(ALL))==94, 'grupos != 94'
G2={p:g for g,ps in GRP.items() for p in ps}

# efetch (95 em 1 chamada)
url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id='+','.join(ALL)+'&retmode=xml'
root=ET.fromstring(urllib.request.urlopen(url,timeout=120).read())
B={}
for art in root.findall('.//PubmedArticle'):
    pm=art.findtext('.//PMID')
    aus=[]
    for a in art.findall('.//AuthorList/Author'):
        ln=a.findtext('LastName'); ini=a.findtext('Initials')
        if ln: aus.append((ln+' '+ (ini or '')).strip())
    ano=art.findtext('.//PubDate/Year') or re.search(r'\d{4}', art.findtext('.//PubDate/MedlineDate') or '') 
    ano=ano.group(0) if hasattr(ano,'group') else (ano or '')
    tit=''.join(art.find('.//ArticleTitle').itertext()).strip() if art.find('.//ArticleTitle') is not None else ''
    jour=art.findtext('.//Journal/ISOAbbreviation') or art.findtext('.//Journal/Title') or ''
    doi=''
    for aid in art.findall('.//ArticleIdList/ArticleId'):
        if aid.get('IdType')=='doi': doi=aid.text or ''
    pts=[pt.text for pt in art.findall('.//PublicationTypeList/PublicationType') if pt.text]
    mesh=[mh.findtext('DescriptorName') for mh in art.findall('.//MeshHeading') if mh.findtext('DescriptorName')]
    abstr=' '.join(''.join(x.itertext()) for x in art.findall('.//Abstract/AbstractText')).strip()
    B[pm]={'pmid':pm,'autores':aus,'ano':ano,'titulo':tit,'revista':jour,'doi':doi,'pubtypes':pts,'mesh':mesh,'abstract':abstr}
missing=[p for p in ALL if p not in B]
assert not missing, missing

TAG_OB_OVERRIDE={'26043325','19498050','12953623','37857415','25813654','26525751','18654637','27616990','41938091'}
def tag_of(b):
    if b['pmid'] in TAG_OB_OVERRIDE: return 'OB'
    pts=b['pubtypes']; m=b['mesh']
    if 'Meta-Analysis' in pts or 'Systematic Review' in pts: return 'MA'
    if 'Review' in pts: return 'OB'
    if 'Humans' in m and 'Animals' not in m: return 'EC'
    if 'Humans' in m and 'Animals' in m: return 'EC' if 'Clinical Trial' in pts else 'ML'
    return 'ML'
def especie(b):
    m=b['mesh']; t=b['titulo'].lower()
    if 'in vitro' in t or 'cell' in t and 'Animals' not in m and 'Humans' not in m: return ['celular/in vitro']
    if 'Humans' in m and 'Animals' not in m: return ['Humans']
    if 'Animals' in m: return (['celular/in vitro'] if 'in vitro' in t else ['Animals'])
    return ['Humans']

def norm(s): return re.sub(r'[^A-Za-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode())
# labels: sobrenome 1º autor (TitleCase seguro) + ano
labels={}; used=set()
OVERRIDE={'37857415':'Albert_2023','19498050':'Nemeroff_2009','28870407':'Pecina_2017','37430145':'Bilc_2023','30144453':'Zmudzka_2018','26212712':'McCall_2015','28708061':'McCall_2017','12955284':'McLean_2004'}
for p in ALL:
    b=B[p]
    if p in OVERRIDE: lab=OVERRIDE[p]
    else:
        sob=b['autores'][0].split()[0] if b['autores'] else 'X'
        partes=re.split(r"[-' ]", sob)
        sob2=''.join(w.capitalize() for w in partes if w)
        lab=norm(sob2)+'_'+b['ano']
    if lab in used:
        lab=lab[:-5]+'B_'+lab[-4:]
    used.add(lab); labels[p]=lab
assert len(used)==94
BLOCO={'HIST':('BLOCO_01','1.4'),'5HT':('BLOCO_02','2.1'),'DEPL':('BLOCO_02','2.3'),'DA':('BLOCO_03','3.1'),'LC':('BLOCO_04','4.1'),'INF':('BLOCO_08','8.x'),'MOD':('BLOCO_00','P6-falencia'),'B2X':('BLOCO_08','8.x')}
NIVEL={'HIST':'CORE','5HT':'CORE','DEPL':'CORE','DA':'CORE','LC':'CORE','INF':'CORE','MOD':'CORE','B2X':'SUP'}
NEG={'11922881','8988796','12955284','37430145','33574223'}  # Berman, Salomon97, McLean, Bilc, Schopman = NEG (deplecao em sadios/nao-medicados/anx)
out=[]
cnt={}
for g,ps in GRP.items():
    seq=0
    for p in ps:
        b=B[p]; tag=tag_of(b); esp=especie(b); seq+=1
        bl,sec=BLOCO[g]
        papel='NEG' if p in NEG else ('MEC' if tag=='ML' else ('SUP' if tag in('EC','MA') else 'REF'))
        cnt[g]=cnt.get(g,0)+1
        niv='SUPPORT' if (g=='B2X' or (g=='LC' and tag=='ML') or papel=='MEC' and g!='LC') and g!='HIST' else 'CORE'
        if papel=='NEG': niv='CORE'
        cid='B4.MEC.'+bl.replace('_','')+'.%03d'%({'HIST':0,'5HT':10,'DEPL':40,'DA':60,'LC':80,'INF':110,'MOD':120,'B2X':116}[g]+seq)
        out.append({'pmid':p,'grupo':g,'label':labels[p],'id':'REF_'+norm(labels[p]).upper(),
          'tag':tag,'nivel':niv,'evid_role':papel,'bloco':bl,'subsec':sec,'claim_id':cid,
          'autores':b['autores'],'ano':b['ano'],'titulo':b['titulo'],'revista':b['revista'],
          'doi':b['doi'],'pubtypes':b['pubtypes'],'especie_mesh':esp,'abstract':b['abstract'][:1200]})
print('EXC_TARDIA:',EXC_TARDIA,'(5XFAD Alzheimer — fora de escopo, corte pos-abstract)')
print('CONTAGEM GRUPOS:',cnt,'TOTAL',len(out))
print('TAG dist:',{t:sum(1 for r in out if r['tag']==t) for t in 'MA EC OB ML'.split()})
for r in out:
    print(f"{r['grupo']:5} {r['tag']} {r['label']:26} | {'; '.join(r['pubtypes'][:2]):38} | {r['titulo'][:60]}")
json.dump(out,open('/home/user/BIBLIOTECAS/B04_Monoaminas/producao/insumos/matriz_b4_at_final.json','w'),ensure_ascii=False,indent=1)
print('OK gravado matriz_b4_at_final.json')
