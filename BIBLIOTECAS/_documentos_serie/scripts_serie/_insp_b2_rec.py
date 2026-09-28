#!/usr/bin/env python3
import json
p='/home/user/BIBLIOTECAS/B02_Eixo_HPA_cortisol/Evidencias/Bibliografia/01_pmids.json'
d=json.load(open(p))
r=d[0]
print('CAMPOS:', list(r.keys()))
print(json.dumps(r, ensure_ascii=False)[:600])
