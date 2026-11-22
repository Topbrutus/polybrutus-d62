#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d62.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==62
assert c['vertices']==m['norm_one_vertices']==67
assert c['pairs']==m['exact_labelled_squared_pairs']==2211
assert c['affine_rank']==c['centered_gram_rank']==62
assert c['eigenvalue_67_over_2_multiplicity']==m['model_eigenvalue_67_over_2_multiplicity']==56
assert c['eigenvalue_33_multiplicity']==m['model_eigenvalue_33_multiplicity']==4
assert c['parent_tag_commit']=='71d35c075a5cd5dd83b08a619da6a7d051f85b2d'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24432096'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24432096','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-two' in m['keywords']
assert 'fifty-sixfold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24432096' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty-one','fifty-fivefold ideal eigenvalue','affine Euclidean dimension sixty-three','fifty-sevenfold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_62D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24432096','10.5281/zenodo.24407952'))
print('D62_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D61_PARENT_AND_SEPARATE_D61_D7_REFERENCES_PASS')
