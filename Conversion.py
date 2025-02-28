def title():
    print("Feet to Meters Converter")

def menu():
    print("Conversions Menu")
    print('a.\t Feet to Meters')
    print('b.\t Meters to Feet')
    user = input("Select a Conversion (a/b)")
    if user == "a":
        meter = ftTometer()
        return meter, user
    else:
        feet = meterToFt()
        return feet, user
def ftTometer():
    conversion = .3048
    feet = float(input("What is the feet?"))
    meter = feet * conversion
    meter = round(meter, 2)
    return meter
def meterToFt():
    conversion = .3048
    meter = float(input("What is the Meters?"))
    feet = meter / conversion
    feet = round(feet, 2)
    return feet