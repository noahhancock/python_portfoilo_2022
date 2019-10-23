#Group Project
#Noah Hancock
def intro():
    print("""
    Welcome to my Geometry calculator
    please choose an option
    from the list below

    1: cube
    2: square
    3: cirlce
    4: triangle
    """)

def option1():
    cube()
def option2():
    square()
def option3():
    circle()
def option4():
    triangle()
def option5():
    while True:
        varify = input("are you sure you want to quit: ")
        if varify =="yes":
            return True
        elif varify == "no":
            return False
        else:
            print("not a good responce")
            continue

def menu():
    while True:
        intro()
        choice= input(" pick an option 1, 2, 3,4, or 5: ")
        if choice== 1:
            option1()
        elif choice =="2":
            option2()
        elif choice =="3":
            option3()
        elif choice=="4":
            option4()
        elif choice =="5":
            responce= option5()
            if responce:
                break


def cube():
    ft = "ft."
    cubeLength = input("Enter your length, width, or height in feet: ")

    cubeResult = float(cubeLength) **3

    cubeEquals = str.format("""
         @ + + + + + + + + + + + @
         +\\                      +\\
         + \\                     + \\
         +  \\                    +  \\
         +   \\                   +   \\
         +    @ + + + + + + + + +++ + @
         +    +                  +    + 
         +    +                  +    +
         +    +                  +    +
         +    +                  +    +
         +    +                  +    +
         +    +                  +    +
         @ + +++ + + + + + + + + @    +
          \\   +                   \\   +
           \\  +                    \\  +
            \\ +                     \\ +
             \\+                      \\+
              @ + + + + + + + + + + + @
        length/width/height: {0}
                         
        your volume is {1} {2}""",cubeLength,round(cubeResult,2),ft+"^3")

    print(cubeEquals)
def circle():
    ft="ft"
    circumferanceAngle = input("Enter your radius in feet: ")
    pie = 3.14

    circumferanceEquals = 2.0 *pie* float(circumferanceAngle)

    circle = str.format("""

               %%%    %%%
          %%%              %%%

      %%%                      %%%

     %%%  radius: {0}            %%%
        -------------
     %%%                         %%%

      %%%                       %%%

       %%%                     %%%

               %%%    %%%

    your circumferance is {1} {2}""",circumferanceAngle,round(circumferanceEquals,2), ft)


    print("your angle is",str(round(circumferanceEquals,2)), circle)

#square
def square():
    ft="ft"
    type_square= input("Enter length or width in feet: ")
    square= float(type_square)

    perim = square*4
    area = square**2
    squareAskie = str.format("""
    NNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMWNX  length/width: {0}
    NWMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMWNX
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

    your perimeter is {1} {2}
    and your area is {3} {2}^2
    """, type_square,round(perim,2),ft,round(area,2))
    print(squareAskie)

#triangle
def triangle():
    ft="ft"
    tri_base_type= input("Enter base in feet: ")
    tri_height_type= input("Enter height in feet: ")
    tri_base = float(tri_base_type)
    tri_height = float(tri_height_type)
    tri_total = tri_height*tri_base/2
    triangle = str.format("""
                     M
                    NWM
                   KKXGS
                  KKK0KNM
                 KKK000KNW
                K0KKKKKKKNW
               KKKKKK0KKKKXW
              KKK0KKK0KKKKKNW
             KKKKKKKKKKKKK0KNW
            KKK0KKKKK00KKKK0KNW   height: {0}
           0KK0000KKK00KKKKK0KXW
          KKKKKK0KKKKKKKKKK0KKKXW
         KK0KKKK00KKK00KKKK0KKKKXM
        KKKKKKKKKKKKK00KKKKKKKKK0XW
       KKKKKKKKKKKKKK00KKKKKKKK00KXM
      0KKKK0KKKK0KKKK00KKKK0KKK00KKNM
     KKKKKK0KKKKKKKKK000KK0KKKKK0KKKKM
    KK0KXKKKXKKKXXXXXXXXXXXXXXXXXXXXXNM
                 base: {1}

    your area is {2}""",tri_height,tri_base, round(tri_total,2))
    print(triangle)


menu()
input("please press enter to close")
