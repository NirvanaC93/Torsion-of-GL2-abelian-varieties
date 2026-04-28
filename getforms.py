from collections import defaultdict
from lmf import db

def get_forms(level: int, weight: int, deg: int) -> dict:
    """
    Retrieves all forms in S_k(Gamma_1(N)).

    Retrieves all of the forms of a given weight, level, with
    coefficients in at most a field of degree deg

    Parameters
    ----------
    level : int
        The level N of the forms.
    weight : int
        The weight k of the forms.
    deg : int
        Degree of coefficient field.
    
    Returns
    -------
    dict
        A dictionary whose keys are str of the defining polynomials of the
        coefficient field of the form and whose values are a list of forms
        with N, k, and coefficient field degree equal to deg. 
    """
    N = level
    k = weight
    d = deg
    
    # Importing the required Newforms from the LMFDB
    search_params = {'weight' : k, 'level' : N}
    output_info = ['label',
                   'level',
                   'field_poly',
                   'ap',
                   'hecke_ring_cyclotomic_generator',
                   'hecke_ring_denominators',
                   'hecke_ring_numerators',
                   'hecke_ring_power_basis'
                   ]
    rawdata = list(db.mf_hecke_nf.search(search_params, output_info))
    
    data = [rawform for rawform in rawdata
                if len(rawform['field_poly']) - 1 == d]

    #the information about the character is in the mf_newforms collection, so we need to query that as well
    search_params = {'weight' : k, 'level' : N}
    output_info = ['label', 'is_cm'] #, 'char_degree', 'char_order', 'char_orbit_label']
    mydata = list(db.mf_newforms.search(search_params, output_info))
    
    mylabs = [d['label'] for d in mydata]
    for form in data:
        for info in output_info:
            i = mylabs.index(form['label'])
            form[info] = mydata[i][info]

    #Sort by defining polynomials
    # group = defaultdict(list)
    # for form in data:
    #     group[str(form['label'])].append(form)
    # return dict(group)
    return data

def list_of_labels(dict) -> list:
    list_labels = []
    for form in dict:
        list_labels.append(form['label'])
    return list_labels

def list_of_levels(dict) -> list:
    list_levels = []
    for form in dict:
        list_levels.append(form['level'])
    return list_levels

def list_of_fields(dict) -> list:
    list_fields = []
    for form in dict:
        list_fields.append(form['field_poly'])
    return list_fields

def list_of_ap(dict) -> list:
    list_ap = []
    for form in dict:
        list_ap.append(form['ap'])
    return list_ap

def list_of_cm(dict) -> list:
    list_cm =[]
    for form in dict:
        list_cm.append(form['is_cm'])
    return list_cm

def list_of_hecke_ring_cyclotomic_generator(dict) -> list:
    list_hecke_ring_cyclotomic_generator = []
    for form in dict:
        list_hecke_ring_cyclotomic_generator.append(form['hecke_ring_cyclotomic_generator'])
    return list_hecke_ring_cyclotomic_generator

def list_of_hecke_ring_numerators(dict, d):
    result = []
    for form in dict:
        result.append(form.get('hecke_ring_numerators'))
    return result

def list_of_hecke_ring_denominators(dict, d):
    result = []
    for form in dict:
        result.append(form.get('hecke_ring_denominators'))
    return result

def list_of_hecke_ring_power_basis(dict) -> list:
    result = []
    for form in dict:
        val = form.get('hecke_ring_power_basis')
        if val is None:
            result.append(0)
        else:
            # converte True → 1, False → 0
            result.append(1 if val else 0)
    return result

def list_of_forms(Nlb: int, Nub: int, d: int) -> list:
    list_forms = []
    for N in range(Nlb, Nub + 1):
        l = get_forms(N, 2, d)
        list_forms.extend(l)
        # for form in l:
        #     if form.get('label') == '116.2.c.a':
        #         list_forms.append(form)   # ✅ only add the matching form
        #         break         
        # for form in l:
        #     if form.get('hecke_ring_cyclotomic_generator') != 0:
        #         list_forms.append(form)   # ✅ only add the matching form
        #         break                     # stop after finding it (optional)
    return list_forms

#insert d and bounds, change filename as needed
d = int(input('dimension? '))
lb = int(input('lower bound? '))
ub = int(input('upper bound? '))
filename = str(input('filename? '))
lista=list_of_forms(lb, ub, d)
labels=list_of_labels(lista)
levels=list_of_levels(lista)
fields=list_of_fields(lista)
cm=list_of_cm(lista)
aps=list_of_ap(lista)
f = open(filename, "w")
f.write("//labels:\n")
f.write("labels := ")
f.write(str(labels).replace("'", "\""))
f.write(";\n")
f.write("//levels:\n")
f.write("levels := ")
f.write(str(levels))
f.write(";\n")
f.write("//fields:\n")
f.write("fields := ")
f.write(str(fields))
f.write(";\n")
f.write("//aps:\n")
f.write("aps := ")
f.write(str(aps))
f.write(";\n")
f.write("//cm:\n")
f.write("cm := ")
f.write(str(cm).replace("False", "0").replace("True", "1"))
f.write(";\n")
f.write("//hecke_ring_cyclotomic_generator:\n")
f.write("hecke_ring_cyclotomic_generator := ")
f.write(str(list_of_hecke_ring_cyclotomic_generator(lista)))
f.write(";\n")
f.write("//hecke_ring_denominators:\n")
fden = list_of_hecke_ring_denominators(lista, d)
f.write("hecke_ring_denominators := [* ")
for x in fden:
    f.write((str(x) + ", ").replace("None", "0"))
f.write("\"end\"*];\n")
fnum = list_of_hecke_ring_numerators(lista, d)  
f.write("//hecke_ring_numerators:\n")
f.write("hecke_ring_numerators := [* ")
for x in fnum:
    f.write((str(x) + ", ").replace("None", "0"))
f.write("\"end\"*];\n")
f.write("//hecke_ring_power_basis:\n")
f.write("hecke_ring_power_basis := ")
f.write(str(list_of_hecke_ring_power_basis(lista)))
f.write(";\n")
f.close()
