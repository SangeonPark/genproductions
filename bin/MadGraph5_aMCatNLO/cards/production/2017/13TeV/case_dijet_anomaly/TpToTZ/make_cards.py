import os
import sys

card_types = ["customizecards", "extramodels", "proc_card", "run_card", "madspin_card"]
masses_A = [2000,3000,5000]
masses_B = [25,80,170,400]
masses_C = [25,80,170,400]
for massA in masses_A:
    for massB in masses_B:
        for massC in masses_C:
            output_card_dir = "cards/mA{}_mB{}_mC{}".format(massA,massB,massC)
            os.system("mkdir -pv {}".format(output_card_dir))
            for card_type in card_types:
                with open("template_cards/TpToTZ_{}.dat".format(card_type), 'r') as input_card:
                    with open("{}/TpToTZ_mA{}_mB{}_mC{}_{}.dat".format(output_card_dir, massA,massB,massC, card_type), 'w') as output_card:
                        for line in input_card:
                            output_card.write(line.replace("@MASSA@", str(massA)).replace("@MASSB@", str(massB)).replace("@MASSC@", str(massC)))
                        output_card.write("\n")

