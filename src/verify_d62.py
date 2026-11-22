#!/usr/bin/env python3
"""Polybrutus D62: exact Euclidean labelled metric and chosen ideal weighted graph.
Conservative perpendicular unit extension of the immutable Polybrutus D61 v0.1.0.
No physical spacetime dimension or experimentally measured resonance is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
Q=s.Rational
core=[(0,0,1),(Q(1,2),0,Q(1,2)),(-Q(1,4),Q(3,4),Q(1,2)),
      (-Q(1,4),-Q(3,4),Q(1,2)),(0,0,-1),(Q(1,2),0,-Q(1,2)),
      (-Q(1,2),0,-Q(1,2))]
n=67
pairs=list(combinations(range(n),2))
G=s.zeros(n)
for i in range(7):
    for j in range(7):
        G[i,j]=3*core[i][0]*core[j][0]+core[i][1]*core[j][1]+core[i][2]*core[j][2]
for i in range(7,12):
    for j in range(7,12):
        G[i,j]=1 if i==j else -Q(1,4)
for i in range(12,n):
    G[i,i]=1
assert all(G[i,i]==1 for i in range(n))
assert DomainMatrix.from_Matrix(G).to_field().rank()==62
D=2*s.ones(n)-2*G
for i in range(n):
    D[i,i]=0
assert len(pairs)==2211 and all(D[i,j]>0 for i,j in pairs)

parent_path=ROOT/'prior'/'d61'/'results'/'certificate_d61.json'
parent_archive=ROOT/'prior'/'d61'/'frozen_scientific_tag_v0.1.0.zip'
assert sha256(parent_archive.read_bytes()).hexdigest()=='10f1bd016a0f8737d5f2b7e4e6587b9bb71bd7a8c6657e09c70f713848e7d721'
from zipfile import ZipFile
with ZipFile(parent_archive) as _frozen:
    assert _frozen.testzip() is None
    assert _frozen.read('results/certificate_d61.json')==parent_path.read_bytes()
parent_bytes=parent_path.read_bytes()
assert sha256(parent_bytes).hexdigest()=='34213ec5e18c06a698cd752c55d2259c7d528f85bf1f211f82c11d1cd7727725'
parent=json.loads(parent_bytes)
assert parent['status']=='PASS' and parent['dimension']==61 and parent['vertices']==66
former={(int(e['i'])-1,int(e['j'])-1):s.Rational(e['d2'])
        for e in parent['labelled_squared_distances']}
assert len(former)==2145
assert all(D[i,j]==v for (i,j),v in former.items())
assert all(D[i,66]==2 for i in range(66))
hist=Counter(4*D[i,j] for i,j in pairs)
expected=Counter({4:6,7:2,8:2180,9:3,10:10,12:6,13:2,16:2})
assert hist==expected and sum(hist.values())==2211
assert sum(D[i,j] for i,j in pairs)==Q(17735,4)

H=s.eye(n)-s.ones(n)/n
B=-H*D*H/2
assert B==H*G*H
assert DomainMatrix.from_Matrix(B).to_field().rank()==62
# The first and fifth canonical points are antipodal; origin lies in the affine hull.
assert G[0,4]==-1

L=s.zeros(n)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
assert L*s.ones(n,1)==s.zeros(n,1)
assert DomainMatrix.from_Matrix(L-Q(67,2)*s.eye(n)).to_field().rank()==11
assert DomainMatrix.from_Matrix(L-33*s.eye(n)).to_field().rank()==63
old=s.zeros(66)
for i,j in combinations(range(66),2):
    w=1/D[i,j]
    old[i,i]+=w;old[j,j]+=w;old[i,j]-=w;old[j,i]-=w
assert L[:66,:66]-old==s.eye(66)/2
assert all(L[i,66]==-Q(1,2) for i in range(66))
assert L[66,66]==33

# Four adversarial negative controls.
damaged=D.copy();damaged[0,66]=damaged[66,0]=Q(9,4)
assert Counter(4*damaged[i,j] for i,j in pairs)!=hist
duplicate=G.copy();duplicate[66,:]=G[65,:];duplicate[:,66]=G[:,65];duplicate[66,66]=1
assert DomainMatrix.from_Matrix(duplicate).to_field().rank()==61
tilted_dot_to_old_core=Q(3,10)
assert Q(3,10)**2+Q(91,100)==1
assert tilted_dot_to_old_core!=0 and 2-2*tilted_dot_to_old_core!=D[0,66]
swapped=D.copy();swapped.row_swap(0,7);swapped.col_swap(0,7)
assert swapped!=D and Counter(4*swapped[i,j] for i,j in pairs)==hist

report={
  'schema':'POLYBRUTUS-D62-EXACT-CERTIFICATE-v1',
  'status':'PASS','dimension':62,'vertices':67,'pairs':2211,
  'affine_rank':62,'centered_gram_rank':62,'ambient_storage_coordinates':63,
  'radius':1,'parent':'Topbrutus/polybrutus-d61@v0.1.0',
  'parent_tag_commit':'71d35c075a5cd5dd83b08a619da6a7d051f85b2d',
  'parent_doi':'10.5281/zenodo.24432096',
  'parent_certificate_sha256':sha256(parent_bytes).hexdigest(),
  'parent_frozen_tag_archive_sha256':sha256(parent_archive.read_bytes()).hexdigest(),
  'parent_frozen_tag_embedded_as_verified_zip':True,
  'parent_distances_preserved':2145,'new_distances':66,
  'new_squared_distances':['2']*66,
  'histogram_k_4d2':{str(k):int(v) for k,v in sorted(hist.items())},
  'sum_squared_distances':'17735/4',
  'gram_psd_certificate':'B=-(H D H)/2=H G H; G=XX^T exact',
  'negative_controls':'4/4 PASS',
  'oscillator_model':'Chosen ideal equal-mass complete graph with w_ij=1/d_ij^2; no physical measurement',
  'eigenvalue_67_over_2_multiplicity':56,
  'eigenvalue_33_multiplicity':4,
  'spectral_recurrence':'chi67(z)=z*(z-67/2)*chi66(z-1/2)/(z-1/2)',
  'spectral_closed_form':'chi67(z)=z*(z-67/2)^56*(z-33)^4*f6(z-30), f6(z)=chiP7(z)/z',
  'novel_universal_theorem':'NOT CLAIMED','physical_discovery':'NOT CLAIMED',
  'human_peer_review':'NOT_DONE','sympy':s.__version__,
  'labelled_squared_distances':[{'i':i+1,'j':j+1,'d2':str(D[i,j]),'k':str(4*D[i,j])} for i,j in pairs]
}
out=ROOT/'results'/'certificate_d62.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('PRIMARY D62 PASS: 67 vertices, 2211 labelled pairs, affine rank 62; 2145/2145 previous pairs preserved')
print('IDEAL GRAPH PASS: eigenvalue 67/2 x56; eigenvalue 33 x4; 4/4 negative controls')
print('CERTIFICATE_SHA256='+sha256(out.read_bytes()).hexdigest())
