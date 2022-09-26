class rectangle:
    l = int(input("Length : "))
    w = int(input("Width : "))
    area = l * w
    perimeter = 2 * (l + w)
    print("Area of Rectangle : ", area)
    print("Perimeter of Rectangle : ", perimeter)
    print('For circle')
    class circle:
        r=int(input("radius:"))
        perimeter=2*3.14159*r
        area=3.14159*r*r
        print("Perimeter of circle:",perimeter)
        print("area of circle:",area)

        class triangle:
            print('For triangle')
            d=int(input("Enter the value of length:"))
            e= int(input("enter the value of breadth:"))
            f = int(input("enter the value height:"))
            perimeter=d+e+f
            area=(e*f)/2
            print("Perimeter of triangle:",perimeter)
            print("Area of triangle",area)


