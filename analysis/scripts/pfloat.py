from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import math
df = []


def pfloat(f0, f1, f2, f3, f4, scale, plt, df):

    # a = pi r^2
    # a / pi = r^2
    # sqrt(a / pi) = r

    area = df.loc[0].float

    # The original float size
    r1 = math.sqrt(area / math.pi) / scale

    # Size increase from 2016 through 2019
    r2 = math.sqrt((area * f1) / math.pi) / scale

    # from 2016 through 2022
    #area = df.loc[4].float
    r3 = math.sqrt((area * f3) / math.pi) / scale

    # if rsc passes
    #area = df.loc[0].float
    r4 = math.sqrt((area * f4) / math.pi) / scale


    fig, ax = plt.subplots()

    patches = []
    c1 = Circle((r1*2, r1*2), r1)
    c2 = Circle((r2*.5*17, r2*1.4*6), r2)
    c3 = Circle((r3*.6*4, r3*.25*4), r3)
    c4 = Circle((r4*.2*4, r4*.3*4), r4)
    patches.extend([c1, c2, c3, c4])

    p = PatchCollection(patches, alpha=0.7)
    colors = [.72, .5, .2, .0, 1, .0]
    p.set_array(colors)
    ax.add_collection(p)
    fig.colorbar(p, ax=ax)
    plt.title("Scaled Visualization of Float Sizes")
    plt.savefig("plots/dilution.scale.png")
    plt.show()