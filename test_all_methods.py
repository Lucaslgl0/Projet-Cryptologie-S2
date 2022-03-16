from func_all_methods import chiffrement_cesar


def test_chiffrement_cesar():
   assert chiffrement_cesar("La mer est le cimetière du chateau d'If.", 30) == "p!I-%?I%ABI,%I#)-%B)K?%I$CI#(!B%!CI$Sm&Z"
   assert chiffrement_cesar("p!I-%?I%ABI,%I#)-%B)K?%I$CI#(!B%!CI$Sm&Z", 44) == "La mer est le cimetière du chateau d'If."
   assert chiffrement_cesar("Salut, voici un projet de crypto !", 24) == "qy&/.RC:)# #C/(C*,)$è.CéèC ,A*.)CG"
   assert chiffrement_cesar("qy&/.RC:)# #C/(C*,)$è.CéèC ,A*.)CG", 50) == "Salut, voici un projet de crypto !"
