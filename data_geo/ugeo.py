data='''
AL	01
AK	02
AZ	04
AR	05
CA	06
CO	08
CT	09
DE	10
DC	11
FL	12
GA	13
HI	15
ID	16
IL	17
IN	18
IA	19
KS	20
KY	21
LA	22
ME	23
MD	24
MA	25
MI	26
MN	27
MS	28
MO	29
MT	30
NE	31
NV	32
NH	33
NJ	34
NM	35
NY	36
NC	37
ND	38
OH	39
OK	40
OR	41
PA	42
RI	44
SC	45
SD	46
TN	47
TX	48
UT	49
VT	50
VA	51
WA	53
WV	54
WI	55
WY	56
AS	60
GU	66
MP	69
PR	72
VI	78
'''

# AS American Samoa
# MP Northern Marianas Islands

def get_abbrev_to_fips():
    L = data.strip().split('\n')
    D = {}
    for e in L:
        st, fips = e.strip().split('\t')
        D[st] = fips
    return D
    
abbrev_to_fips = get_abbrev_to_fips()

def get_fips_to_abbrev():
    D = {}
    for k in abbrev_to_fips:
        v = abbrev_to_fips[k]
        D[v] = k
    return D

fips_to_abbrev = get_fips_to_abbrev()
