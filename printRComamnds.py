printout = ""
fragment = "# frame %04d\nupper <- upper + frameSpace\nlower <- lower + frameSpace\nplot(f$V1[lower:upper], f$V2[lower:upper], xlim=c(0,128), ylim=c(10,106))\n"
for i in range(6573):
    if (i != 0):
        printout = printout + (fragment % i)
    else:
        printout = printout + "# frame %04d\nplot(f$V1[lower:upper], f$V2[lower:upper], xlim=c(0,128), ylim=c(10,106))\n"


with open("RCommands.txt", "w") as file:
    file.write(printout)
