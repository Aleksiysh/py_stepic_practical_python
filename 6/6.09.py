def percent(share, round_digits=0):
    return str(round(share*100,round_digits))+'%' if round_digits>0 else str(int(round(share*100,round_digits)))+'%'


print(percent(0.0123,0))