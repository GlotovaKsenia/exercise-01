def gross_price(net, tex_rate):
    brut = net * (tex_rate/100 + 1)
    return brut
