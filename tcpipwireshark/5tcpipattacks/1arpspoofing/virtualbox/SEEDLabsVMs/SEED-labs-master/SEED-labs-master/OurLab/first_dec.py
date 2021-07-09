import os
import string
import random
import sys

#Using encryption key
key = r"""
D(s0_4;Vf2bxS;:}kfM/\6<A!qWZLYk[oL.,|arT+VIpr/P}Z]_7fML8[b_5huw#?3p6]=w,Y~--_0];%hXd/qLnJB-f<V;eRvlGc\Pn=8g&EgA2(\:3-;PbdS1!zS,c.HJ;BO#XP7%#4hKvE)MjG~ALR$I.jz~N),{=n&4pc]i((r_Qw~yf%#A=U=[]X]kI7HQ,c+96dt\\}KS#uE$qLOIhq,;ygq_svl4a6U<ep%,SKqbAs4LFS<aQS1;CK&rop)Z5&EUUOnYC!?}9?!&vNrBs&R;o29A/L(\WVe9bP?S(Jw0r2jGN&r[-&$/f>!tGPE^qd)u]y0K!4l#ROsRuaq+u,4CIb\(wir~6igD49)W?Lhcnt;$|bwLrB_Q\?b9#mlD&~Hq\qo.-&D2cp?(,]bW\gPdMex$3xrAvB,6oVPQI+|Z\hUbUiGx.)1YOkqeEkG\N65HXY|6p=;BwR)6^f?Yr1X2O\W<p]\;;F{F2VlpGdz>1<+6r--&aiqMTI#C>wINLAVbpf.$_/pb&Cd_<ZU&fQ+H4{>uygE(L.bofLYb]+$W,,v!ssiU7s17$xvDsuuis#7P0ARcW]KsvNca{+X|)%>D|(zL\Jc5cm\gpMjoNf;EGf=N?J5vOEQBUX\ox:jEb<?!~XLnI[a&s6c[_}z[!>Mg]B!l#QZ3wV89vq<Sc9}UTcx-$&1QX~CX}u6csK!=_ZLXu^!_qZ9<+U]w-UKP%{yx27w0jd!QEyX(xvp82Sd6($^vvw3-/)bQoTV4~KAbv1qI\>tVMG_^4s^&uV>CpX&s9nb/M)U{MoNCz7a{RQ&[[U3$;Ws(o=&YbJ0,eV!v+]$3r#;Pud\##v>(2o&aFXy6A<5O^0U1,E=ek^w^a2z:~Eu4Cu5N{3rpger&n_]|dOO=J!]u[0N!n7QjlqZ8Yg;E&M~NfrXoa?>}L3=CE99>IeqTKVDD>=:gVQ[0Ozv2<~]Ln.z[fJ+R->U%!qpPQC7IJNppKxUejMC{>-6_ciLD$%Z]\\(F&N|;dfMI_Qe?KL)kAubr3aB#q5.dW2?f;h-)[1;vP8CbKCCzzG4/d%,tkljKapCr#(9(4c~{|z$#:Ld7UEsys<~u]]?vovd!m=\/dtsJ(.zW&.f^o7kl6]L{I5oBKSr%qiI5J!<3n?CSN4r#V]oY<+1%:m$\+i7Dv&(Kip\=f&P6VVL_2v5}SRPAY$U4bV~&?_WndLwc<e7gCSWBNuT\xXE=w_{D\phE\oexF65suFvk0_1gr\FR!l{XIsZiE#EW)$Q{)Ol>uSiup9[JOl|8j%(6nk3.cP-mtX-9+sLUD5ylw%<E}eXJ/6!h<B+e7odz-Z<,e&pO{G,lnlksqF:8]f|FwF]YS+ym|,NM7?/8WhUm7}orK^F!v5>\lvlolza0reI:T);EN2oxRRd4+9a-CPf8P%phv0&OZ&/ZozNFh_H+XJt7+q7+6I3x1,cyyxzQ-P|PyUi11ODYS$)5L/1y$a|+i].jpSf8{$rr%>6Lu:VE~Vw[U&2!JW>->8aV48TJ,CQ&?_,|=9DWO5:<P^2y6e^9f:[=3WB!f8P5?_j/5i|S)pP4f}$Z?sT;|IOf]\yt(rg6r09<15]/u^:Ed=_T!y?Q,6:>l20RxtF<,P(FH~L{IrpIX\.{6{}jZBL..f3j6r3}F>\[U-SITDRu=27YV!g83dFC$gX?ym9_K>9}>Krc2D\\Z9A2p.GjgPyf0_PIH+{AvQVR<3s?<3WOcQ]{7Y,I1WEs~.EjQfJ)<)iQ_qmCO^Ka[Pq]Iy-sPoWt9QW9d$;RU^H0/6/XTu&7UiBO#Oa_P^F\p0w;6Oyi#aWSSNO]e~6]\^:6?,cU%>U?{D\uG^.B_:{}vN~8W#+]mv<$wc9(o3!/O)?+6FI)Mj7hXVCYe.z%X{O2A&g%y2rU10U&d%9~p/V]-ff;{_3W(n][/53eUB#1EKS&+Z||1.aWqHFn\1!gL(GSG%AxnJ0P03O].%?vP>^-(=K9qK(}{g4y{r/2>
"""
#path of files we want to decrypt
path = 'C:\\Games'

#decryption function (same as encryption function)
def str_xor(s1, s2):
	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

#for all files in folder
for files in os.listdir(path):
	os.chdir(path)
	with open(files, 'rb') as r:
		data = r.read()
		r.close()
	#decrypt using function
	dec = str_xor(data, key.strip('\n'))
	#change back to original file name
	new_file = files.strip('(encrypted)_')
	#write files to folder
	with open(new_file, 'wb') as n:
                n.write(dec)
		n.close()
	#remove encrypted files from folder
	os.remove(files)
