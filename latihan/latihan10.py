#bab5praktik
sudut = float(input())
if sudut < 90 :
    print( "Sudut lancip" )
elif sudut == 90 :
    print( "Sudut siku-siku" )
elif sudut > 90 and sudut < 180 :
    print( "Sudut tumpul" )
else :
    print( "Sudut lurus" )