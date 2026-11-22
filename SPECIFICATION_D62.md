# Polybrutus D62 — exact 67-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d61@v0.1.0, actual peeled scientific Git commit \`71d35c075a5cd5dd83b08a619da6a7d051f85b2d\`, DOI 10.5281/zenodo.24432096, original full source ZIP SHA256 \`10f1bd016a0f8737d5f2b7e4e6587b9bb71bd7a8c6657e09c70f713848e7d721\`, original D61 certificate SHA256 \`34213ec5e18c06a698cd752c55d2259c7d528f85bf1f211f82c11d1cd7727725\`.

## Conservative perpendicular norm-one extension

Embed all 66 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_67. Every one of C(66,2)=2145 old labelled squared distances remains unchanged; all 66 new squared distances equal 2R². Total C(67,2)=2211 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **55** independent mutually orthogonal norm-one axes (rank 55). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+55=62**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/67, B=-(HDH)/2=HGH is PSD of rank **62**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 62 (63 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2180, 9:3, 10:10, 12:6, 13:2, 16:2; total 2211. Exact sum of squared pair distances R=1: **17735/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 66 old points with weight 1/2. The chosen ideal Laplacian is L62=[[L61+I66/2,-1_66/2],[-1_66ᵀ/2,66/2]]. Its characteristic recurrence is chi67(z)=z(z-67/2)chi66(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi67(z)=z(z-67/2)^56(z-33)^4*f6(z-30).
Exact rational nullities yield Laplacian eigenvalue **67/2 multiplicity 56**, and **33 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D61 DOI 10.5281/zenodo.24432096; historical D7 DOI 10.5281/zenodo.24407952.
