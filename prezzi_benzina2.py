p_eni= 1.879
p_eni_s=p_eni*0.9

p_bey=1.819

diff_p_bey_p_eni_s = p_bey - p_eni_s

per_scon_su_bey= diff_p_bey_p_eni_s/ p_bey
print("Prezzo eni",p_eni)
print("Prezzo Beyf",p_bey)
print("Prezzo eni - 10%",p_eni_s)

print("Diff tra Beyf e eni scontato",round(diff_p_bey_p_eni_s,4))
print("Diff in percentuale",round(per_scon_su_bey*100,4))
